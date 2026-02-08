#!/usr/bin/env python3
"""
Convert partition and sharding.docx to Markdown with extracted images.
Uses only stdlib (zipfile, xml.etree.ElementTree).
"""
import zipfile
import xml.etree.ElementTree as ET
import os
import re

DOCX_PATH = "partition and sharding.docx"
OUT_MD = "partition-sharding.md"
OUT_DIR = "."
IMG_PREFIX = "partition-sharding"

# OOXML namespaces
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def qname(prefix, local):
    return "{%s}%s" % (NS[prefix], local)


def get_rels(zipf):
    """Parse document.xml.rels: rId -> target path (for images)."""
    rels = {}
    try:
        with zipf.open("word/_rels/document.xml.rels") as f:
            tree = ET.parse(f)
            for rel in tree.getroot():
                rid = rel.get("Id")
                typ = rel.get("Type", "")
                target = rel.get("Target", "")
                if "image" in typ and target:
                    rels[rid] = target  # e.g. media/image1.jpeg
    except KeyError:
        pass
    return rels


def extract_images(zipf, out_dir):
    """Extract word/media/* to out_dir with names partition-sharding-1.jpeg etc. Return rId -> local filename."""
    rid_to_file = {}
    rels = get_rels(zipf)
    for rid, target in rels.items():
        # target is like "media/image1.jpeg"
        full_path = "word/" + target
        try:
            data = zipf.read(full_path)
        except KeyError:
            continue
        base = os.path.basename(target)  # image1.jpeg
        num = re.search(r"image(\d+)", base, re.I)
        ext = os.path.splitext(base)[1]
        if num:
            local_name = f"{IMG_PREFIX}-{num.group(1)}{ext}"
        else:
            local_name = f"{IMG_PREFIX}-{base}"
        out_path = os.path.join(out_dir, local_name)
        with open(out_path, "wb") as f:
            f.write(data)
        rid_to_file[rid] = local_name
    return rid_to_file


def text_of_para(p):
    """Collect all w:t text from a paragraph (including inside w:r)."""
    parts = []
    for t in p.iter(qname("w", "t")):
        if t.text:
            parts.append(t.text)
        if t.tail:
            parts.append(t.tail)
    return "".join(parts).replace("\xa0", " ").strip()


def get_embed_rid(drawing):
    """From a w:drawing element, find a:blip @r:embed and return the rId."""
    for blip in drawing.iter(qname("a", "blip")):
        embed = blip.get(qname("r", "embed"))
        if embed:
            return embed
    return None


def is_heading(text):
    """Heuristic: short line or numbered section like '1. What is Partitioning?'"""
    if not text or len(text) > 120:
        return False
    if re.match(r"^\d+\.\s+\w", text):
        return True
    if re.match(r"^[A-Z][a-z]+(\s+[A-Za-z]+)*\s*$", text) and len(text) < 80:
        return True
    return False


def is_code_line(line):
    """Likely a line of code (SQL, etc.)."""
    line = line.strip()
    if not line:
        return False
    code_starts = ("CREATE ", "SELECT ", "INSERT ", "ALTER ", "DROP ", "PARTITION ", "VALUES ", "WHERE ", ");", "',")
    return any(line.startswith(s) or line.endswith(s) for s in code_starts) or ("(" in line and ")" in line and ("INT" in line or "TEXT" in line or "BIGINT" in line))


def parse_body(zipf, rid_to_file):
    with zipf.open("word/document.xml") as f:
        tree = ET.parse(f)
    root = tree.getroot()
    body = root.find(qname("w", "body"))
    if body is None:
        return []

    items = []

    def process_paragraph(p):
        text = text_of_para(p)
        drawing = p.find(".//" + qname("w", "drawing"))
        if drawing is not None:
            rid = get_embed_rid(drawing)
            if rid and rid in rid_to_file:
                items.append(("image", rid_to_file[rid]))
        if text:
            items.append(("text", text))

    for child in body:
        if child.tag == qname("w", "p"):
            process_paragraph(child)
        elif child.tag == qname("w", "tbl"):
            # Walk table: tbl -> tr -> tc -> p (and p may contain drawing)
            for tr in child.findall(".//" + qname("w", "tr")):
                for tc in tr.findall(qname("w", "tc")):
                    for p in tc.findall(qname("w", "p")):
                        process_paragraph(p)
    return items


def items_to_markdown(items):
    md = []
    in_code = False
    code_buf = []

    i = 0
    while i < len(items):
        kind, value = items[i]
        if kind == "image":
            if in_code:
                md.append("```")
                md.append("")
                md.extend(code_buf)
                md.append("")
                in_code = False
                code_buf = []
            md.append("")
            md.append(f"![Image]({value})")
            md.append("")
        elif kind == "text":
            text = value
            if is_code_line(text) or (code_buf and (text.startswith("    ") or text.startswith("--") or "PARTITION" in text or "CREATE" in text or "INSERT" in text or "SELECT" in text or ");" in text or "VALUES" in text)):
                if not in_code:
                    in_code = True
                    code_buf = []
                code_buf.append(text)
            else:
                if in_code:
                    md.append("```")
                    md.append("")
                    md.extend(code_buf)
                    md.append("")
                    in_code = False
                    code_buf = []
                if is_heading(text):
                    # Numbered section -> ## or ###
                    if re.match(r"^\d+\.\s+", text):
                        md.append("")
                        md.append("## " + text)
                        md.append("")
                    else:
                        md.append("")
                        md.append("### " + text)
                        md.append("")
                elif text:
                    md.append(text)
                    md.append("")
        i += 1

    if in_code:
        md.append("```")
        md.append("")
        md.extend(code_buf)
        md.append("")

    return "\n".join(md).strip()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    docx_path = DOCX_PATH
    if not os.path.isfile(docx_path):
        print("File not found:", docx_path)
        return

    with zipfile.ZipFile(docx_path, "r") as z:
        rid_to_file = extract_images(z, OUT_DIR)
        items = parse_body(z, rid_to_file)

    md_content = items_to_markdown(items)
    title = "# Sharding vs. Partitioning"
    intro = """Sharding and partitioning are two of the most commonly confused concepts in system design.
At first glance, they may seem similar, and people often use them interchangeably. But they are not.
Both are techniques to **divide and scale large databases**; however, they differ in how the data is divided.
"""
    full_md = title + "\n\n" + intro + "\n\n---\n\n" + md_content

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(full_md)
    print("Wrote", OUT_MD)
    print("Extracted", len(rid_to_file), "images.")


if __name__ == "__main__":
    main()
