"""
Reads all PDFs in D:\GW-Thesis\papers\ and extracts structured thesis notes.
Output: D:\GW-Thesis\paper_notes\<cite_key>.md  +  D:\GW-Thesis\ALL_PAPER_NOTES.md
"""

import fitz  # PyMuPDF
import os
import json
import re
from pathlib import Path

PAPERS_DIR = Path(r"D:\GW-Thesis\papers")
NOTES_DIR  = Path(r"D:\GW-Thesis\paper_notes")
NOTES_DIR.mkdir(exist_ok=True)

# Map filenames to cite_keys
FILENAME_MAP = {
    "poggio2021soilgrids.pdf":     "poggio2021soilgrids",
    "jasechko2024gwdecline.pdf":   "jasechko2024gwdecline",
    "arulbalaji2019gisahp.pdf":    "arulbalaji2019gisahp",
    "sahin2020ensembletree.pdf":   "sahin2020ensembletree",
    "chang2019scaleeffects.pdf":   "chang2019scaleeffects",
    "das2018pravara.pdf":          "das2018pravara",
    "pande2021ahpmif.pdf":         "pande2021ahpmif",
    "hafeez2025rwh.pdf":           "hafeez2025rwh",
    "roy2019knowledgedriven.pdf":  "roy2019knowledgedriven",
    "waseem2024waterquality.pdf":  "waseem2024waterquality",
    "khan2024afforestation.pdf":   "khan2024afforestation",
    # MDPI papers with original filenames
    "applsci-12-05560.pdf":        "sarwar2022soandrought",
    "atmosphere-14-00452.pdf":     "khan2023rainfallrunoff",
    "ijgi-09-00720.pdf":           "swain2020floodahp",
    "water-11-02656-v2.pdf":       "mallick2019fuzzyahp",
    "water-12-00471-v2.pdf":       "benjmel2020morocco",
    "water-14-00496-v2.pdf":       "waseem2022drought",
}

# Load papers.json for metadata
with open(r"D:\GW-Thesis\papers.json") as f:
    papers_data = json.load(f)

meta_by_key = {p["cite_key"]: p for p in papers_data["papers"]}


def clean(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'([a-z])-\s+([a-z])', r'\1\2', text)  # fix hyphenated line breaks
    return text.strip()


def extract_text_by_sections(pdf_path, max_pages=20):
    """Extract text from first max_pages of a PDF."""
    doc = fitz.open(pdf_path)
    pages_text = []
    for i, page in enumerate(doc):
        if i >= max_pages:
            break
        pages_text.append(page.get_text())
    doc.close()
    return "\n".join(pages_text)


def find_section(full_text, keywords, chars=2000):
    """Find a named section and return up to `chars` characters."""
    for kw in keywords:
        pattern = re.compile(
            rf'(?i)(?:^|\n)\s*{re.escape(kw)}[:\s]{{0,20}}\n([\s\S]{{200,{chars}}})',
        )
        m = pattern.search(full_text)
        if m:
            return clean(m.group(1))
    return ""


def extract_key_numbers(text):
    """Pull out accuracy/AUC/F1/kappa/correlation numbers."""
    patterns = [
        r'accuracy[:\s]+(\d+\.?\d*\s*%)',
        r'AUC[:\s]+(\d+\.?\d*)',
        r'F1[:\s]+(\d+\.?\d*)',
        r'kappa[:\s]+(\d+\.?\d*)',
        r'R²[:\s]+(\d+\.?\d*)',
        r'correlation[:\s]+(\d+\.?\d*)',
        r'precision[:\s]+(\d+\.?\d*\s*%)',
        r'recall[:\s]+(\d+\.?\d*\s*%)',
        r'sensitivity[:\s]+(\d+\.?\d*\s*%)',
        r'specificity[:\s]+(\d+\.?\d*\s*%)',
        r'ROC.AUC[:\s]+(\d+\.?\d*)',
    ]
    found = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            found.append(m.group(0).strip())
    return list(dict.fromkeys(found))[:15]  # deduplicate, max 15


CHAPTER_NOTES = {
    "foundational_ml":       "Chapter 3 (Methodology - ML algorithms)",
    "gw_potential_mapping":  "Chapter 2 (Literature Review) + Chapter 3 (Methodology)",
    "ml_hydrology_review":   "Chapter 1 (Introduction) + Chapter 2 (Literature Review)",
    "methodology_analog":    "Chapter 3 (Methodology - justification)",
    "data_sources":          "Chapter 3 (Methodology - Data Sources)",
    "gw_context":            "Chapter 1 (Introduction - motivation)",
    "pakistan_pothohar":     "Chapter 2 (Study Area) + Chapter 5 (Discussion)",
}

all_notes = []

for filename, cite_key in FILENAME_MAP.items():
    pdf_path = PAPERS_DIR / filename
    if not pdf_path.exists():
        print(f"MISSING: {filename}")
        continue

    print(f"Reading: {cite_key}...")
    meta = meta_by_key.get(cite_key, {})

    try:
        full_text = extract_text_by_sections(pdf_path, max_pages=20)
    except Exception as e:
        print(f"  ERROR reading PDF: {e}")
        continue

    # Extract abstract
    abstract = find_section(full_text,
        ["Abstract", "ABSTRACT", "Summary", "SUMMARY"], chars=1500)
    if not abstract:
        abstract = clean(full_text[:1500])

    # Extract conclusion
    conclusion = find_section(full_text,
        ["Conclusion", "CONCLUSION", "Conclusions", "CONCLUSIONS",
         "Summary and Conclusion"], chars=2000)

    # Extract study area
    study_area = find_section(full_text,
        ["Study Area", "STUDY AREA", "Study area", "Research Area"], chars=1000)

    # Extract methods
    methods = find_section(full_text,
        ["Methodology", "METHODOLOGY", "Methods", "METHODS",
         "Materials and Methods", "Data and Methods"], chars=2000)

    # Extract results
    results = find_section(full_text,
        ["Results", "RESULTS", "Results and Discussion",
         "RESULTS AND DISCUSSION"], chars=2000)

    # Key numbers
    numbers = extract_key_numbers(full_text)

    category = meta.get("category", "unknown")
    chapter_use = CHAPTER_NOTES.get(category, "General reference")

    # Build note
    note = f"""# {cite_key}

## Metadata
- **Title:** {meta.get('title', 'N/A')}
- **Authors:** {meta.get('authors', 'N/A')}
- **Year:** {meta.get('year', 'N/A')}
- **Venue:** {meta.get('venue', 'N/A')}
- **DOI:** {meta.get('doi', 'N/A')}
- **Citations:** {meta.get('citations', 'N/A')}
- **Category:** {category}
- **Use in Thesis:** {chapter_use}
- **BibTeX key:** `\\cite{{{cite_key}}}`

## Why This Paper Matters for Your Thesis
{meta.get('description', 'N/A')}

## Abstract / Summary
{abstract[:1400] if abstract else 'Not extracted.'}

## Study Area
{study_area[:900] if study_area else 'Not explicitly stated.'}

## Methodology (Relevant Points)
{methods[:1800] if methods else 'Not extracted.'}

## Key Results & Findings
{results[:1800] if results else 'Not extracted.'}

## Conclusion
{conclusion[:1800] if conclusion else 'Not extracted.'}

## Key Numbers / Statistics Found
{chr(10).join('- ' + n for n in numbers) if numbers else '- See full paper'}

---
"""
    # Save individual note
    note_path = NOTES_DIR / f"{cite_key}.md"
    note_path.write_text(note, encoding="utf-8")
    all_notes.append(note)
    print(f"  Saved: {note_path.name}")

# Save combined file
combined_path = Path(r"D:\GW-Thesis\ALL_PAPER_NOTES.md")
header = """# All Paper Notes — ML Groundwater Potential Mapping Thesis
Generated from PDF extraction. Use these notes to write thesis chapters.

**Quick navigation:**
- Chapter 1 (Introduction): jasechko2024gwdecline
- Chapter 2 (Literature Review): arulbalaji2019gisahp, arabameri2018shahroud, das2018pravara, pande2021ahpmif, mallick2019fuzzyahp, benjmel2020morocco
- Chapter 3 (Methodology): poggio2021soilgrids, sahin2020ensembletree, chang2019scaleeffects, roy2019knowledgedriven, swain2020floodahp
- Chapter 4 (Results): sahin2020ensembletree (comparison benchmark)
- Chapter 5 (Discussion): hafeez2025rwh, khan2023rainfallrunoff, sarwar2022soandrought, waseem2022drought, waseem2024waterquality, khan2024afforestation
- Appendix: All data-source papers

---

"""
combined_path.write_text(header + "\n\n".join(all_notes), encoding="utf-8")
print(f"\nAll notes saved to: {combined_path}")
print(f"Individual notes in: {NOTES_DIR}")
print(f"Total papers processed: {len(all_notes)}")
