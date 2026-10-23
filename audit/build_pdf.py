"""Construit une version HTML puis PDF du rapport d'audit team_02.

Dépendances éphémères : markdown, pypdf, pymupdf.
Commande : uv run --with markdown --with pypdf --with pymupdf python audit/build_pdf.py
Navigateur utilisé : Chrome en mode headless (installé sur le poste).
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

import markdown
import pymupdf
from pypdf import PdfReader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH = os.path.join(ROOT, "audit", "rapport_audit_helpdesk_team_02.md")
HTML_PATH = os.path.join(ROOT, "audit", "rapport_audit_helpdesk_team_02.html")
PDF_PATH = os.path.join(ROOT, "audit", "rapport_audit_helpdesk_team_02.pdf")

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

CSS = r"""
:root {
  --ink: #1b2430;
  --muted: #5b6675;
  --accent: #0b5f8a;
  --accent-soft: #e8f2f8;
  --rule: #c9d5df;
  --critical: #8c1d18;
  --high: #a34a00;
  --medium: #6b5a00;
  --low: #2f5d3a;
}
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  margin: 0;
  color: var(--ink);
  font-family: "Segoe UI", "Calibri", "DejaVu Sans", Arial, sans-serif;
  font-size: 10pt;
  line-height: 1.45;
}
@page {
  size: A4;
  margin: 17mm 15mm 17mm 15mm;
}
@page :first { margin: 0; }

.cover {
  height: 297mm;
  padding: 26mm 22mm 20mm 22mm;
  background: linear-gradient(145deg, #f7fbfd 0%, #ffffff 52%, #eef6fa 100%);
  border-top: 12mm solid var(--accent);
  display: flex;
  flex-direction: column;
  page-break-after: always;
}
.cover .kicker {
  color: var(--accent);
  font-size: 10pt;
  font-weight: 700;
  letter-spacing: 2.2px;
  text-transform: uppercase;
  margin-bottom: 8mm;
}
.cover h1 {
  font-size: 38pt;
  line-height: 1.05;
  margin: 0 0 4mm 0;
  letter-spacing: -0.8px;
  color: #10202c;
}
.cover .subtitle {
  font-size: 15pt;
  color: var(--muted);
  margin: 0 0 9mm 0;
  max-width: 150mm;
}
.cover .rule {
  width: 42mm;
  height: 2.2mm;
  background: var(--accent);
  margin: 0 0 9mm 0;
}
.cover .badge {
  display: inline-block;
  background: var(--accent-soft);
  color: var(--accent);
  border: 0.4mm solid #b9d7e6;
  border-radius: 2mm;
  padding: 2.2mm 4mm;
  font-size: 8.8pt;
  font-weight: 600;
  margin-bottom: 10mm;
}
.cover table.meta {
  width: 100%;
  border-collapse: collapse;
  margin-top: 2mm;
}
.cover table.meta td {
  padding: 2.1mm 0;
  vertical-align: top;
  border-bottom: 0.25mm solid var(--rule);
  font-size: 9.3pt;
}
.cover table.meta td.label {
  width: 38mm;
  color: var(--muted);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-size: 7.8pt;
}
.cover .team {
  margin-top: 9mm;
  color: var(--ink);
  font-size: 9.3pt;
}
.cover .team strong { color: var(--accent); }
.cover .foot {
  margin-top: auto;
  border-top: 0.35mm solid var(--rule);
  padding-top: 4mm;
  color: var(--muted);
  font-size: 8pt;
  display: flex;
  justify-content: space-between;
  gap: 8mm;
}
.cover .foot .right { text-align: right; }

.toc-page {
  page-break-after: always;
}
.toc-page h2 {
  font-size: 18pt;
  color: var(--accent);
  border-bottom: 0.45mm solid var(--accent);
  padding-bottom: 2mm;
  margin: 0 0 7mm 0;
  break-before: avoid;
}
.toc-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.toc-list li {
  display: flex;
  align-items: baseline;
  border-bottom: 0.25mm solid var(--rule);
  padding: 3mm 0;
  font-size: 11pt;
}
.toc-list .t { color: var(--ink); }
.toc-list .dots {
  flex: 1;
  border-bottom: 0.2mm dotted #aebdca;
  margin: 0 2.5mm;
  position: relative;
  top: -1mm;
}
.toc-list .pg {
  color: var(--muted);
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.content h2 {
  font-size: 16pt;
  color: var(--accent);
  border-bottom: 0.45mm solid var(--accent);
  padding-bottom: 2mm;
  margin: 0 0 6mm 0;
  break-before: page;
  break-after: avoid;
}
.content h2:first-of-type { break-before: auto; }
.content h2 + h3 { break-before: auto; }
.content h3 {
  font-size: 12.2pt;
  color: #10202c;
  margin: 0 0 4mm 0;
  padding: 3mm 0 2mm 0;
  border-bottom: 0.3mm solid var(--rule);
  break-before: auto;
  break-after: avoid;
}
.content h4 { font-size: 11pt; margin: 5mm 0 2mm 0; }
.content p { margin: 0 0 3.2mm 0; text-align: justify; }
.content p:has(> strong:only-child) { break-after: avoid; }
.content ul, .content ol { margin: 0 0 3.6mm 0; padding-left: 6mm; }
.content li { margin-bottom: 1.3mm; break-inside: avoid; }
.content strong { color: #10202c; }
.content a { color: var(--accent); text-decoration: none; }
.content hr { border: 0; border-top: 0.3mm solid var(--rule); margin: 6mm 0; }
.content code {
  font-family: "Cascadia Mono", "Consolas", "DejaVu Sans Mono", monospace;
  font-size: 8.6pt;
  background: #f2f5f7;
  border: 0.2mm solid #dde5ea;
  border-radius: 1mm;
  padding: 0.2mm 1mm;
}
.content pre {
  background: #f6f8fa;
  border: 0.3mm solid #d7e0e6;
  border-left: 1.2mm solid var(--accent);
  border-radius: 1.2mm;
  padding: 3.2mm 4mm;
  margin: 0 0 4mm 0;
  white-space: pre-wrap;
  word-break: break-word;
  overflow-wrap: anywhere;
  font-size: 8.1pt;
  line-height: 1.38;
  break-inside: avoid;
}
.content pre code { background: none; border: 0; padding: 0; font-size: inherit; }
.content table {
  width: 100%;
  border-collapse: collapse;
  margin: 3mm 0 5mm 0;
  font-size: 7.6pt;
  line-height: 1.3;
}
.content th, .content td {
  border: 0.25mm solid #cfdae1;
  padding: 1.7mm 1.5mm;
  vertical-align: top;
  text-align: left;
  word-break: normal;
  overflow-wrap: break-word;
  hyphens: none;
}
.content th {
  background: var(--accent-soft);
  color: #0d3d57;
  font-weight: 700;
}
.content table.synthesis {
  table-layout: fixed;
  font-size: 7.5pt;
}
.content table.synthesis th:nth-child(1),
.content table.synthesis td:nth-child(1) { width: 5%; }
.content table.synthesis th:nth-child(2),
.content table.synthesis td:nth-child(2) { width: 21%; }
.content table.synthesis th:nth-child(3),
.content table.synthesis td:nth-child(3) { width: 20%; }
.content table.synthesis th:nth-child(4),
.content table.synthesis td:nth-child(4) { width: 18%; }
.content table.synthesis th:nth-child(5),
.content table.synthesis td:nth-child(5) { width: 8%; white-space: nowrap; font-weight: 600; }
.content table.synthesis th:nth-child(6),
.content table.synthesis td:nth-child(6) { width: 16%; white-space: nowrap; font-family: "Cascadia Mono", Consolas, monospace; font-size: 7pt; }
.content table.synthesis th:nth-child(7),
.content table.synthesis td:nth-child(7) { width: 12%; }
.content tr { break-inside: avoid; }
.content tbody tr:nth-child(even) td { background: #fafcfd; }
.content blockquote {
  margin: 3mm 0 4mm 0;
  padding: 2.5mm 4mm;
  border-left: 1.2mm solid var(--accent);
  background: #f7fbfd;
  color: var(--muted);
}
.content em { color: inherit; }
.small { font-size: 8.5pt; color: var(--muted); }
"""

COVER = """
<section class="cover">
  <div class="kicker">Rapport d'audit de sécurité</div>
  <h1>HelpDesk-AI</h1>
  <div class="subtitle">Évaluation offensive de l'agent d'assistance informatique interne de Helvetia Systems SA</div>
  <div class="rule"></div>
  <div class="badge">8 vulnérabilités confirmées &nbsp;•&nbsp; 3 critiques &nbsp;•&nbsp; 4 élevées &nbsp;•&nbsp; 1 moyenne</div>
  <table class="meta">
    <tr><td class="label">Client</td><td>Helvetia Systems SA — Direction des systèmes d'information</td></tr>
    <tr><td class="label">Prestataire</td><td>JNR 16K — Léo LECLERCQ, Edgar BOBILLON, Tomy RULLIAT, Erwan AOUCHICHE</td></tr>
    <tr><td class="label">Contact</td><td>Edgar BOBILLON</td></tr>
    <tr><td class="label">Référence</td><td>CPE-2026-REDTEAM-HELPDESK</td></tr>
    <tr><td class="label">Identifiant</td><td><strong>team_02</strong></td></tr>
    <tr><td class="label">Date</td><td>23 octobre 2026</td></tr>
    <tr><td class="label">Référentiels</td><td>OWASP Top 10 for LLM Applications (2025) — MITRE ATLAS</td></tr>
  </table>
  <div class="team"><strong>Équipe :</strong> JNR 16K &nbsp;·&nbsp; <strong>Kit :</strong> helpdesk_kit_team_02</div>
  <div class="foot">
    <div>Document confidentiel — diffusion restreinte au client et à l'équipe pédagogique.</div>
    <div class="right">team_02<br>CPE-2026-REDTEAM-HELPDESK</div>
  </div>
</section>
"""


SECTIONS = [
    "1. Résumé exécutif",
    "2. Périmètre et méthode",
    "3. Synthèse des findings",
    "4. Fiches détaillées",
    "5. Résultats négatifs",
    "6. Conclusion et recommandations prioritaires",
]


def run_chrome() -> None:
    chrome = next((p for p in CHROME_CANDIDATES if os.path.exists(p)), None)
    if not chrome:
        raise SystemExit("Chrome/Edge introuvable pour l'impression PDF.")
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=15000",
        f"--print-to-pdf={PDF_PATH}",
        "file:///" + HTML_PATH.replace("\\", "/"),
    ]
    print("Chrome :", chrome)
    subprocess.run(cmd, check=True, timeout=120)
    if not os.path.exists(PDF_PATH):
        raise SystemExit("Le PDF n'a pas été produit.")


def stamp_footer() -> None:
    """Ajoute un pied de page discret et la pagination (sauf sur la couverture)."""
    doc = pymupdf.open(PDF_PATH)
    doc.set_metadata({
        "title": "Rapport d'audit de securite - HelpDesk-AI - team_02",
        "author": "JNR 16K - Leo LECLERCQ, Edgar BOBILLON, Tomy RULLIAT, Erwan AOUCHICHE",
        "subject": "Audit de securite offensif de l'agent HelpDesk-AI - CPE-2026-REDTEAM-HELPDESK",
        "keywords": "team_02, HelpDesk-AI, OWASP LLM 2025, MITRE ATLAS, pentest",
        "creator": "JNR 16K - team_02",
        "producer": "Chrome headless + PyMuPDF",
    })
    total = len(doc)
    for i in range(1, total):
        page = doc[i]
        w, h = page.rect.width, page.rect.height
        page.draw_line((42, h - 38), (w - 42, h - 38),
                       color=(0.78, 0.83, 0.87), width=0.4)
        page.insert_text((42, h - 27), "Rapport d'audit HelpDesk-AI - team_02",
                         fontsize=7.3, fontname="helv", color=(0.38, 0.43, 0.48))
        right = f"Page {i + 1} / {total}"
        tw = pymupdf.get_text_length(right, fontname="helv", fontsize=7.3)
        page.insert_text((w - 42 - tw, h - 27), right,
                         fontsize=7.3, fontname="helv", color=(0.38, 0.43, 0.48))
    tmp = PDF_PATH + ".tmp"
    doc.save(tmp, garbage=3, deflate=True)
    doc.close()
    os.replace(tmp, PDF_PATH)
    print("Pied de page et pagination ajoutés.")


def build() -> None:
    text = open(MD_PATH, encoding="utf-8").read()
    marker = "\n## 1. Résumé exécutif"
    idx = text.find(marker)
    if idx < 0:
        raise SystemExit("Section « 1. Résumé exécutif » introuvable dans le rapport.")
    body_md = text[idx + 1:]

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists", "attr_list"],
        extension_configs={"toc": {"toc_depth": "2", "permalink": False}},
    )
    body_html = md.convert(body_md)
    # Le sommaire est inséré après un premier passage, avec les numéros de page.
    toc_html = "<!--TOC-->"

    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Rapport d'audit de sécurité — HelpDesk-AI — team_02</title>
<style>{CSS}</style>
</head>
<body>
{COVER}
<section class="toc-page">
  <h2>Sommaire</h2>
  {toc_html}
</section>
<section class="content">
{body_html}
</section>
</body>
</html>
"""
    with open(HTML_PATH, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("HTML :", HTML_PATH)

    run_chrome()

    reader = PdfReader(PDF_PATH)
    pages = len(reader.pages)
    size = os.path.getsize(PDF_PATH)
    print(f"PDF  : {PDF_PATH}")
    print(f"Pages: {pages} — Taille: {size/1024:.1f} Ko")

    # Deuxième passage : insérer le sommaire avec les numéros de page réels.
    section_pages: dict[str, int] = {}
    for title in SECTIONS:
        for i, page in enumerate(reader.pages[2:], start=3):
            if title in (page.extract_text() or ""):
                section_pages[title] = i
                break
    print("Pages des sections :", section_pages)
    items = "".join(
        f'<li><span class="t">{t}</span><span class="dots"></span>'
        f'<span class="pg">{section_pages.get(t, "?")}</span></li>'
        for t in SECTIONS
    )
    final_html = html.replace("<!--TOC-->", f'<ul class="toc-list">{items}</ul>')
    with open(HTML_PATH, "w", encoding="utf-8") as fh:
        fh.write(final_html)
    run_chrome()
    stamp_footer()
    reader = PdfReader(PDF_PATH)
    pages = len(reader.pages)
    size = os.path.getsize(PDF_PATH)
    print(f"PDF final : {pages} pages — {size/1024:.1f} Ko")

    # Vérifications de contenu : les 8 jetons et les titres de sections.
    txt = "\n".join((p.extract_text() or "") for p in reader.pages)
    tokens = sorted(set(re.findall(r"CPE\{[0-9a-fA-F]{12}\}", txt)))
    print("Jetons trouvés dans le PDF :", len(tokens))
    for t in tokens:
        print("  -", t)
    for section in ["Résumé exécutif", "Synthèse des findings", "Fiches détaillées",
                    "Résultats négatifs", "Conclusion et recommandations"]:
        print(f"  section {section!r}: {'OK' if section in txt else 'ABSENTE'}")
    if len(tokens) < 8:
        raise SystemExit("Tous les jetons ne sont pas extractibles du PDF.")


if __name__ == "__main__":
    build()
