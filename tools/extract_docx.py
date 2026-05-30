#!/usr/bin/env python3
"""
extract_docx.py — Izvelk saturu no Projektēšanas rokasgrāmata .docx
un aizpilda src/ mapes Markdown failus.

Palaist no: /home/nauris/projects/paligs-buvkonstrukciju-projektesana/
Palaist ar: python3 tools/extract_docx.py
"""

from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table
from pathlib import Path
import re
import io

DOCX_PATH = Path("/home/nauris/Dropbox/Projects/Projektēšanas rokasgrāmata/K FORMA - Projektēšanas rokasgrāmata 2026.docx")
SRC_DIR = Path("/home/nauris/projects/paligs-buvkonstrukciju-projektesana/src")

SECTION_MAP = {
    "PRIEKŠVĀRDS":                                      ("01-prieksvards.md", 1),
    "IZMANTOJAMIE BŪVNORMATĪVI UN STANDARTI":           ("02-normativas.md", 1),
    "VISPĀRĪGIE PROJEKTĒŠANAS NOSACĪJUMI":              ("03-visparigie.md", 1),
    "EKSPLUATĀCIJAS ILGUMA KATEGORIJAS":                ("03-visparigie.md", 2),
    "SEKU KLASES":                                      ("03-visparigie.md", 2),
    "DROŠĪBAS KLASES":                                  ("03-visparigie.md", 2),
    "PROJEKTĒŠANAS KONTROLES LĪMENIS":                  ("03-visparigie.md", 2),
    "BŪVDARBU UZRAUDZĪBAS LĪMEŅI":                     ("03-visparigie.md", 2),
    "VISPĀRĪGIE PROJEKTA DATI":                         ("03-visparigie.md", 2),
    "SLODZES UN IEDARBES":                              ("04-slodzes/README.md", 1),
    "LIETDERĪGĀS SLODZES":                              ("04-slodzes/01-lietderigas.md", 2),
    "REKOMENDĒJAMĀS PARCIĀLO FAKTORU VĒRTĪBAS":         ("04-slodzes/01-lietderigas.md", 2),
    "KLIMATISKĀS SLODZES":                              ("04-slodzes/02-klimatiskas.md", 2),
    "SNIEGA SLODZE":                                    ("04-slodzes/02-klimatiskas.md", 3),
    "VĒJA SLODZE":                                      ("04-slodzes/02-klimatiskas.md", 3),
    "KONSTRUKCIJU PAŠSVARA UN APDARES SLODZES":         ("04-slodzes/03-pasvars.md", 2),
    "NELABVĒLĪGĀKĀS SLODZES NOTEIKŠANA":               ("04-slodzes/04-nelabveligas.md", 2),
    "IZBŪVES KLASES":                                   ("04-slodzes/05-izbuvesklases.md", 2),
    "ĒKU ROBUSTUMA NODROŠINĀJUMS":                     ("04-slodzes/06-robustums.md", 2),
    "UGUNDROŠU KONSTRUKCIJU PROJEKTĒŠANA":              ("05-uguns.md", 1),
    "KONSTRUKTĪVĀS SHĒMAS UN DARBĪBAS PRINCIPI":        ("06-shemas.md", 1),
    "KONSTRUKTĪVĀS SHĒMAS":                             ("06-shemas.md", 1),
    "PAMATI UN PAMATNE":                                ("07-pamati/README.md", 1),
    "VISPĀRĪGI":                                        ("07-pamati/01-visparigie.md", 2),
    "TEHNOLOĢIJU PIELIETOJAMĪBA":                       ("07-pamati/02-tehnologijas.md", 2),
    "GRUNŠU BLĪVUMI":                                   ("07-pamati/03-grunsis.md", 2),
    "GRUNŠU PARAMETRU KORELĀCIJAS UN APRAKSTI":         ("07-pamati/03-grunsis.md", 2),
    "MAKSIMĀLĀS ROBEŽDEFORMĀCIJAS":                     ("07-pamati/03-grunsis.md", 2),
    "PUASONA KOEFICIENTI":                              ("07-pamati/03-grunsis.md", 2),
    "GRUNŠU KLASIFIKĀCIJA PĒC DAĻIŅU SASTĀVA":         ("07-pamati/03-grunsis.md", 2),
    "GRUNŠU BLIETĒŠANA":                                ("07-pamati/03-grunsis.md", 2),
    "SEKLIE PAMATI":                                    ("07-pamati/03-grunsis.md", 2),
    "PĀĻU PAMATI":                                      ("07-pamati/04-pali.md", 2),
    "DELZSBETONA KONSTRUKCIJAS":                        ("08-dzelzsbetons/README.md", 1),
    "DZELZSBETONA KONSTRUKCIJAS":                       ("08-dzelzsbetons/README.md", 1),
    "VISPĀRĪGI PRINCIPI":                               ("08-dzelzsbetons/README.md", 2),
    "PAPILDUS PRASĪBAS PROJEKTĒŠANAI UN IZGATAVOŠANAI": ("08-dzelzsbetons/02-prasibas.md", 2),
    "LABAS DETALIZĀCIJAS PRAKSE PA ELEMENTU TIPIEM":    ("08-dzelzsbetons/03-detalizacija.md", 2),
    "VERTIKĀLO PĀRVIETOJUMU ROBEŽVĒRTĪBAS":             ("08-dzelzsbetons/04-robezvertibas.md", 2),
    "PLAISU PLATUMU ROBEŽVĒRTĪBAS":                     ("08-dzelzsbetons/04-robezvertibas.md", 2),
    "GALVENIE NACIONĀLI NOTEIKTIE PARAMETRI":           ("08-dzelzsbetons/04-robezvertibas.md", 2),
    "BETONA CIETĒŠANA":                                 ("08-dzelzsbetons/05-vide.md", 2),
    "VIDES IEDARBĪBAS KLASES":                          ("08-dzelzsbetons/05-vide.md", 2),
    "ŠĶĒRSSTIEGROJUMS":                                 ("08-dzelzsbetons/05-vide.md", 2),
    "SALIEKAMAIS DZELZSBETONS":                         ("08-dzelzsbetons/06-saliekamais.md", 2),
    "STIEGROJUMA METINĀŠANAS RISINĀJUMI PĒC DIN 4099":  ("08-dzelzsbetons/07-metinasana.md", 2),
    "TĒRAUDA KONSTRUKCIJAS":                            ("09-terauds/README.md", 1),
    "KOPŅU PROJEKTĒŠANA":                               ("09-terauds/05-kopnes.md", 2),
    "UGUNSDROŠU TĒRAUDA KONSTRUKCIJU PROJEKTĒŠANA":     ("09-terauds/06-uguns.md", 2),
    "KOKA KONSTRUKCIJAS":                               ("10-koks/README.md", 1),
    "LABĀ PRAKSE RASĒJUMU NOFORMĒŠANĀ":                 ("11-rasejumi/README.md", 1),
}

CONTEXT_DEPENDENT = {
    "FIZIKĀLĀS UN MEHĀNISKĀS ĪPAŠĪBAS": {
        "08": "08-dzelzsbetons/01-ipasibas.md",
        "09": "09-terauds/01-ipasibas.md",
        "10": "10-koks/01-ipasibas.md",
    },
    "PAPILDUS PRASĪBAS PROJEKTĒŠANAI UN IZGATAVOŠANAI": {
        "09": "09-terauds/02-prasibas.md",
    },
    "APRĒĶINS PĒC ROBEŽSTĀVOKĻU METODES": {
        "09": "09-terauds/03-aprekins.md",
    },
    "RAKSTURĪGĀS PĀRSEGUMU LAIDUMU UN AUGSTUMU ATTIECĪBAS": {
        "09": "09-terauds/03-aprekins.md",
    },
    "TĒRAUDA KONSTRUKCIJU SAVIENOJUMI": {
        "09": "09-terauds/04-savienojumi.md",
    },
    "STIPRĪBAS KLASES ATBILSTOŠI EN 338": {
        "10": "10-koks/01-ipasibas.md",
    },
    "MATERIĀLU PARCIĀLIE KOFEFICIENTI ΥM": {
        "10": "10-koks/02-koeficienti.md",
    },
    "KOEFICIENTA KMOD VĒRTĪBAS": {
        "10": "10-koks/02-koeficienti.md",
    },
    "PIEMĒRI SLODZES IEDARBĪBAS ILGUMA KLASES NOTEIKŠANAI": {
        "10": "10-koks/02-koeficienti.md",
    },
    "SIJU IZLIEČU ROBEŽLIELUMI": {
        "10": "10-koks/03-robezlielumi.md",
    },
    "ĢEOTEHNISKĀ IZPĒTE": {
        "10": "10-koks/04-geotehnika.md",
    },
    "OPTIMĀLAIS RASĒJUMA LAPAS IZKĀRTOJUMS": {
        "11": "11-rasejumi/01-lapas.md",
    },
    "RASĒJUMA LAPU IZMĒRI": {
        "11": "11-rasejumi/01-lapas.md",
    },
    "IZMĒRU LĪNIJAS": {
        "11": "11-rasejumi/02-izmeri.md",
    },
    "ELEMENTU MARĶĒJUMS, INFORMATĪVĀS NORĀDES": {
        "11": "11-rasejumi/03-markejums.md",
    },
    "ELEMENTU MARĶĒJUMA INDEKSI": {
        "11": "11-rasejumi/03-markejums.md",
    },
}

HEADING_ALIASES = {
    "FIRE DESIGN": "UGUNDROŠU KONSTRUKCIJU PROJEKTĒŠANA",
}


def normalize_heading(text: str) -> str:
    text = re.sub(r'^\d+(\.\d+)*\.?\s*', '', text.strip())
    return text.strip().upper()


def is_known_heading(text: str, chapter_prefix: str):
    norm = normalize_heading(text)
    if norm in HEADING_ALIASES:
        norm = HEADING_ALIASES[norm]
    if norm in SECTION_MAP:
        return SECTION_MAP[norm]
    if norm in CONTEXT_DEPENDENT:
        ctx = CONTEXT_DEPENDENT[norm]
        if chapter_prefix in ctx:
            return (ctx[chapter_prefix], 2)
        for prefix, path in ctx.items():
            if chapter_prefix.startswith(prefix):
                return (path, 2)
    return (None, 0)


def table_to_markdown(table) -> str:
    rows = []
    for row in table.rows:
        cells = []
        for cell in row.cells:
            cell_text = ' '.join(p.text.strip() for p in cell.paragraphs if p.text.strip())
            cell_text = cell_text.replace('|', '\\|')
            cells.append(cell_text)
        rows.append(cells)
    if not rows:
        return ""
    header = rows[0]
    lines = ['| ' + ' | '.join(header) + ' |',
             '| ' + ' | '.join(['---'] * len(header)) + ' |']
    for row in rows[1:]:
        while len(row) < len(header):
            row.append('')
        lines.append('| ' + ' | '.join(row[:len(header)]) + ' |')
    return '\n'.join(lines) + '\n'


def extract_images(para, img_dir: Path, img_counter: list) -> list:
    img_dir.mkdir(parents=True, exist_ok=True)
    refs = []
    blips = para._element.findall('.//' + qn('a:blip'))
    seen = set()
    for blip in blips:
        embed = blip.get(qn('r:embed'))
        if not embed or embed in seen:
            continue
        seen.add(embed)
        rel = para.part.rels.get(embed)
        if rel is None or 'image' not in rel.reltype:
            continue
        img_data = rel.target_part.blob
        img_counter[0] += 1
        img_name = f"img{img_counter[0]:03d}.png"
        img_path = img_dir / img_name
        try:
            from PIL import Image
            img = Image.open(io.BytesIO(img_data))
            img.save(img_path, 'PNG')
        except Exception:
            with open(img_path, 'wb') as f:
                f.write(img_data)
        rel_path = img_path.relative_to(SRC_DIR)
        refs.append(f"![Attēls]({rel_path})\n\n")
    return refs


def para_to_md(para, img_dir: Path, img_counter: list) -> str:
    has_img = para._element.findall('.//' + qn('a:blip'))
    if has_img:
        refs = extract_images(para, img_dir, img_counter)
        return ''.join(refs)
    text = para.text.strip()
    if not text:
        return ""
    style = para.style.name
    if style == 'tv213':
        return f"- {text}\n"
    return f"{text}\n\n"


def get_img_dir(file_rel: str) -> Path:
    m = re.match(r'(\d{2})', file_rel)
    ch = m.group(1) if m else "00"
    return SRC_DIR / "images" / f"ch{ch}"


def main():
    print(f"Lasām: {DOCX_PATH.name}")
    doc = Document(str(DOCX_PATH))

    file_contents: dict[str, list] = {}
    current_file = None
    chapter_prefix = "01"
    img_counter = [0]
    content_started = False

    for element in doc.element.body:
        tag = element.tag.split('}')[-1] if '}' in element.tag else element.tag

        if tag == 'p':
            para = Paragraph(element, doc)
            style = para.style.name
            if style.startswith('toc') or style == 'TOC Heading':
                continue

            text = para.text.strip()

            if not content_started:
                if normalize_heading(text) == "PRIEKŠVĀRDS":
                    content_started = True
                else:
                    continue

            new_file, new_level = is_known_heading(text, chapter_prefix)
            if new_file:
                current_file = new_file
                m = re.match(r'(\d{2})', new_file)
                if m:
                    chapter_prefix = m.group(1)
                if current_file not in file_contents:
                    file_contents[current_file] = []
                clean = re.sub(r'^\d+(\.\d+)*\.?\s*', '', text.strip())
                hashes = '#' * new_level
                file_contents[current_file].append(f"\n{hashes} {clean}\n\n")
            else:
                if current_file is None:
                    continue
                if current_file not in file_contents:
                    file_contents[current_file] = []
                img_dir = get_img_dir(current_file)
                md = para_to_md(para, img_dir, img_counter)
                if md:
                    file_contents[current_file].append(md)

        elif tag == 'tbl':
            if not content_started or current_file is None:
                continue
            if current_file not in file_contents:
                file_contents[current_file] = []
            table = Table(element, doc)
            md = table_to_markdown(table)
            if md:
                file_contents[current_file].append(f"\n{md}\n")

    written = 0
    for file_rel, lines in file_contents.items():
        out_path = SRC_DIR / file_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        content = ''.join(lines)
        content = re.sub(r'\n{4,}', '\n\n', content)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(content.strip() + '\n')
        written += 1
        print(f"  ✓ {file_rel} ({len(content.splitlines())} rindas)")

    print(f"\nPabeigts: {written} faili, {img_counter[0]} attēli")


if __name__ == '__main__':
    main()
