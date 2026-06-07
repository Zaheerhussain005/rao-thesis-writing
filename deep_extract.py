"""
Deep extraction: reads full PDF text (up to 20 pages),
identifies key sections more robustly, and writes
detailed thesis-ready notes per paper.
"""

import fitz
import json
import re
from pathlib import Path

PAPERS_DIR = Path(r"D:\GW-Thesis\papers")
NOTES_DIR  = Path(r"D:\GW-Thesis\paper_notes")

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
    "applsci-12-05560.pdf":        "sarwar2022soandrought",
    "atmosphere-14-00452.pdf":     "khan2023rainfallrunoff",
    "ijgi-09-00720.pdf":           "swain2020floodahp",
    "water-11-02656-v2.pdf":       "mallick2019fuzzyahp",
    "water-12-00471-v2.pdf":       "benjmel2020morocco",
    "water-14-00496-v2.pdf":       "waseem2022drought",
}

with open(r"D:\GW-Thesis\papers.json") as f:
    papers_data = json.load(f)
meta_by_key = {p["cite_key"]: p for p in papers_data["papers"]}


def get_full_text(pdf_path, max_pages=20):
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        if i >= max_pages:
            break
        pages.append(page.get_text())
    doc.close()
    return "\n".join(pages)


def clean(t):
    t = re.sub(r'\s+', ' ', t)
    t = re.sub(r'([a-z])-\s([a-z])', r'\1\2', t)
    return t.strip()


def grab_after(text, headers, max_chars=2500):
    """Find any of the given headers and return text after it."""
    for h in headers:
        # Case-insensitive, allow whitespace/newlines before content
        pat = re.compile(
            rf'(?:^|\n)[ \t]*{re.escape(h)}[ \t]*[\n\r]+([\s\S]{{100,{max_chars}}})',
            re.IGNORECASE
        )
        m = pat.search(text)
        if m:
            snippet = m.group(1)
            # Stop at next major section heading
            stop = re.search(
                r'\n[ \t]*(?:Introduction|Methods|Methodology|Results|Discussion|Conclusion|References|Acknowledgement)[s]?[ \t]*\n',
                snippet, re.IGNORECASE
            )
            if stop:
                snippet = snippet[:stop.start()]
            return clean(snippet[:max_chars])
    return ""


def extract_numbers(text):
    """Extract all percentage / decimal accuracy numbers with context."""
    patterns = [
        r'(?:accuracy|AUC|F1|kappa|sensitivity|specificity|precision|recall|R²|NSE|RMSE|r²)[^.]{0,60}?(\d+\.?\d*\s*%|\d\.\d{3,})',
        r'(\d+\.?\d*)\s*%\s*(?:accuracy|AUC|agreement|correct)',
        r'AUC[^.]{0,40}?(\d\.\d{2,})',
        r'kappa[^.]{0,40}?(\d\.\d{2,})',
    ]
    results = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            full = clean(m.group(0))
            if full not in results:
                results.append(full)
    return results[:20]


def find_abstract(text):
    """Find abstract block."""
    # Try explicit header
    a = grab_after(text, ['Abstract', 'ABSTRACT'], max_chars=1800)
    if a and len(a) > 150:
        return a
    # Fall back to first 1800 chars after title area
    lines = text.split('\n')
    body_start = 0
    for i, l in enumerate(lines[:30]):
        if len(l.strip()) > 80:
            body_start = i
            break
    return clean(' '.join(lines[body_start:body_start+50]))[:1800]


def find_conclusion(text):
    a = grab_after(text,
        ['Conclusions', 'Conclusion', 'CONCLUSIONS', 'CONCLUSION',
         'Summary and Conclusions', 'Summary', '5. Conclusion', '6. Conclusion',
         '7. Conclusion', '4. Conclusion'], max_chars=3000)
    return a


def find_results(text):
    a = grab_after(text,
        ['Results and Discussion', 'Results', 'RESULTS', '4. Results',
         '3. Results', '5. Results', 'Key Findings'], max_chars=3000)
    return a


def find_methods(text):
    a = grab_after(text,
        ['Materials and Methods', 'Methodology', 'Methods', 'METHODOLOGY',
         '2. Methods', '3. Methods', '2. Methodology', '3. Methodology',
         'Data and Methods'], max_chars=3000)
    return a


def thesis_relevance(cite_key, meta, full_text):
    """Build a 'relevance to our thesis' block based on key text."""
    cat = meta.get('category', '')
    desc = meta.get('description', '')

    notes = [f"**Category:** {cat}", f"**Why cite:** {desc}"]

    # Look for specific matches to our thesis context
    pothohar_kw = ['pothohar', 'pothowar', 'chakwal', 'rawalpindi', 'attock', 'jhelum', 'mianwali', 'punjab pakistan']
    ml_kw = ['xgboost', 'random forest', 'lightgbm', 'gradient boosting', 'ensemble']
    gw_kw = ['groundwater potential', 'gwpz', 'groundwater potential zone', 'groundwater delineation']
    feat_kw = ['ndvi', 'ndwi', 'twi', 'topographic wetness', 'soilgrids', 'chirps', 'srtm', 'landsat']

    text_lower = full_text.lower()

    found = []
    for kw in pothohar_kw:
        if kw in text_lower:
            found.append(f"Mentions '{kw}'")
    for kw in ml_kw:
        if kw in text_lower:
            found.append(f"Uses {kw.upper()}")
    for kw in gw_kw:
        if kw in text_lower:
            found.append(f"Topic: {kw}")
    for kw in feat_kw:
        if kw in text_lower:
            found.append(f"Uses {kw.upper()} feature")

    if found:
        notes.append("**Relevance signals:** " + " | ".join(found[:8]))

    # Chapter placement guidance
    chapter_map = {
        'gw_context':            'Chapter 1 §1.1 (Introduction — global GW crisis)',
        'foundational_ml':       'Chapter 3 §3.3 (ML Algorithms — cite when introducing each model)',
        'gw_potential_mapping':  'Chapter 2 §2.2 (Literature Review — GIS/AHP baseline methods)',
        'ml_hydrology_review':   'Chapter 2 §2.3 (ML in hydrology review) + Chapter 1 §1.2',
        'methodology_analog':    'Chapter 3 §3.4 (Model validation / comparison framework)',
        'data_sources':          'Chapter 3 §3.1 (Data Sources — mandatory dataset citation)',
        'pakistan_pothohar':     'Chapter 2 §2.1 (Study Area) + Chapter 5 §5.2 (Discussion — regional context)',
    }
    notes.append("**Chapter placement:** " + chapter_map.get(cat, 'See relevant chapter'))
    return '\n'.join(notes)


# ── Chapter-specific cite instructions ────────────────────────────────────────
CITE_INSTRUCTIONS = {
    "poggio2021soilgrids": """
**How to cite in thesis:**
- Chapter 3 §3.1: "Soil texture data were obtained from SoilGrids 2.0 \\cite{poggio2021soilgrids},
  a global dataset produced at 250 m resolution using quantile regression forests trained on
  ~240,000 soil profiles and 400+ environmental covariates."
- This is a MANDATORY citation — your top feature (r=0.836) comes from this dataset.
""",
    "jasechko2024gwdecline": """
**How to cite in thesis:**
- Chapter 1 §1.1 opening: "Groundwater resources are under increasing threat globally;
  Jasechko et al. (2024) \\cite{jasechko2024gwdecline} found rapid groundwater-level declines
  (>0.5 m/year) in 170,000 wells across 40+ countries, with accelerating depletion in 30%
  of regional aquifers over the past four decades."
- Use as the motivating global context before narrowing to Pakistan/Pothohar.
""",
    "arulbalaji2019gisahp": """
**How to cite in thesis:**
- Chapter 2 §2.2: "AHP-based weighted overlay is widely used for GWPZ delineation
  \\cite{arulbalaji2019gisahp}, employing 12 thematic layers (geology, geomorphology, LULC,
  TWI, slope, rainfall, soil, drainage density) with pairwise comparison matrices to assign weights."
- Chapter 3 §3.2: Compare your weighted-overlay label generation with this established AHP approach.
""",
    "sahin2020ensembletree": """
**How to cite in thesis:**
- Chapter 3 §3.3: "Sahin (2020) \\cite{sahin2020ensembletree} demonstrated that ensemble
  tree methods — specifically XGBoost, GBM and RF — consistently outperform single models
  for spatial susceptibility mapping, with XGBoost achieving the highest AUC values."
- Chapter 4: use as benchmark comparison for your XGBoost results.
""",
    "chang2019scaleeffects": """
**How to cite in thesis:**
- Chapter 3 §3.1: "SRTM 30 m DEM derivatives (slope, TWI) are appropriate for regional-scale
  GIS analysis \\cite{chang2019scaleeffects}; Chang et al. (2019) found that 30 m resampled
  DEM-derived topographic variables produced the highest accuracy in ML-based spatial mapping."
""",
    "das2018pravara": """
**How to cite in thesis:**
- Chapter 2 §2.2: "Das and Pardeshi (2018) \\cite{das2018pravara} integrated lithology,
  geomorphology, slope, soil, drainage density, lineament density and rainfall using
  Frequency Ratio (FR) and Influencing Factor (IF) methods for GWPZ in Pravara basin,
  achieving AUC = 0.73 with FR method."
""",
    "pande2021ahpmif": """
**How to cite in thesis:**
- Chapter 2 §2.2: "Pande et al. (2021) \\cite{pande2021ahpmif} applied AHP (AUC=0.86) and
  MIF (AUC=0.80) for GWPZ in semi-arid Mula river basin, India, using LULC, DEM, soil texture,
  NDVI, slope and groundwater depth — confirming AHP as the more effective technique."
""",
    "hafeez2025rwh": """
**How to cite in thesis:**
- Chapter 2 §2.1 (Study Area): "Hafeez et al. (2025) \\cite{hafeez2025rwh} used AHP with
  DEM, rainfall, LULC, soil and drainage density to map 6,508 rainwater harvesting sites
  across the Pothowar region (23,204 km², same five districts as this study), classifying
  44.81% as highly suitable for water storage."
- Chapter 5 §5.2: Compare your ML-predicted high-potential zones with their RWH suitability.
""",
    "roy2019knowledgedriven": """
**How to cite in thesis:**
- Chapter 3 §3.2 (Label Generation): "Knowledge-driven label generation via weighted overlay
  is an established methodology for spatial hazard mapping \\cite{roy2019knowledgedriven};
  Roy and Saha (2019) used fuzzy-AHP and LNRF expert knowledge weights (rainfall, slope,
  aspect, geology, soil, NDVI, TWI) achieving ROC-AUC = 0.91, validating expert-knowledge
  label generation as a reliable training-label source for ML models."
""",
    "waseem2024waterquality": """
**How to cite in thesis:**
- Chapter 5 §5.2 (Discussion): "Water quality surveys in Rawalpindi/Islamabad
  \\cite{waseem2024waterquality} identified widespread contamination linked to shallow
  unconfined aquifer conditions — consistent with our model's Medium-potential classification
  of peri-urban Rawalpindi district."
""",
    "khan2024afforestation": """
**How to cite in thesis:**
- Chapter 2 §2.1 or Chapter 5: "Semi-arid barren land in Attock district \\cite{khan2024afforestation}
  is associated with low vegetation cover and degraded soil structure — factors our model captures
  through low NDVI and low soil-texture scores."
""",
    "sarwar2022soandrought": """
**How to cite in thesis:**
- Chapter 2 §2.1 (Study Area): "The Soan River basin — entirely within the Pothohar Plateau —
  is characterized by recurrent hydrological drought \\cite{sarwar2022soandrought}, where
  meteorological deficits rapidly translate into reduced groundwater recharge, underscoring
  the urgency of precise groundwater potential mapping."
""",
    "khan2023rainfallrunoff": """
**How to cite in thesis:**
- Chapter 5 §5.1 (Discussion): "Khan et al. (2023) \\cite{khan2023rainfallrunoff} applied
  wavelet-coupled ML models (ANN, SVM, ANFIS) in four Pothohar basins and found that
  wavelet preprocessing significantly improved model performance for rainfall-runoff simulation
  — consistent with the strong signal from CHIRPS rainfall (r=0.514) found in this study."
- Chapter 2 §2.3: Regional ML precedent in the exact study area.
""",
    "swain2020floodahp": """
**How to cite in thesis:**
- Chapter 3 §3.2: "AHP-based multi-criteria spatial analysis has been widely validated
  for natural resource mapping \\cite{swain2020floodahp}; Swain et al. (2020) demonstrated
  cloud-based GIS-AHP susceptibility mapping achieving good prediction accuracy — the same
  framework underpins our knowledge-based label generation."
""",
    "mallick2019fuzzyahp": """
**How to cite in thesis:**
- Chapter 2 §2.2: "In semi-arid Saudi Arabia (climatically analogous to Pothohar),
  Mallick et al. (2019) \\cite{mallick2019fuzzyahp} used Fuzzy-AHP with geology, lineaments,
  geomorphology, NDVI, slope, TWI and soil to delineate GWPZ, validating with well data
  and demonstrating the transferability of geospatial GWPZ methods to arid regions."
""",
    "benjmel2020morocco": """
**How to cite in thesis:**
- Chapter 5 §5.2 (Discussion — hard-rock zones): "In hard-rock crystalline terrain,
  Benjmel et al. (2020) \\cite{benjmel2020morocco} found that lineament density and
  structural geology are primary controls on groundwater occurrence — consistent with our
  model's low-potential prediction for Margalla Hills and Kala Chitta Range hard-rock areas."
""",
    "waseem2022drought": """
**How to cite in thesis:**
- Chapter 2 §2.1: "Punjab province experiences significant spatiotemporal drought variability
  \\cite{waseem2022drought}; Waseem et al. (2022) identified a declining trend in agricultural
  water availability across Punjab between 1981–2019, highlighting the critical need for
  improved groundwater resource mapping."
""",
}


all_output = []

for filename, cite_key in FILENAME_MAP.items():
    pdf_path = PAPERS_DIR / filename
    if not pdf_path.exists():
        print(f"MISSING: {filename}")
        continue

    print(f"Deep-reading: {cite_key}...")
    meta = meta_by_key.get(cite_key, {})

    try:
        full_text = get_full_text(pdf_path, max_pages=20)
    except Exception as e:
        print(f"  ERROR: {e}")
        continue

    abstract   = find_abstract(full_text)
    methods    = find_methods(full_text)
    results    = find_results(full_text)
    conclusion = find_conclusion(full_text)
    numbers    = extract_numbers(full_text)
    relevance  = thesis_relevance(cite_key, meta, full_text)
    cite_instr = CITE_INSTRUCTIONS.get(cite_key, "See chapter placement above.")

    note = f"""# {cite_key}

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | {meta.get('title','N/A')} |
| **Authors** | {meta.get('authors','N/A')} |
| **Year** | {meta.get('year','N/A')} |
| **Venue** | {meta.get('venue','N/A')} |
| **DOI** | {meta.get('doi','N/A')} |
| **Citations** | {meta.get('citations','N/A')} |
| **BibTeX key** | `\\cite{{{cite_key}}}` |

---

## Thesis Relevance
{relevance}

---

## How to Cite in Your Thesis
{cite_instr}

---

## Abstract
{abstract[:1800] if abstract else 'Not extracted.'}

---

## Methodology
{methods[:2500] if methods else 'Not extracted.'}

---

## Results & Findings
{results[:2500] if results else 'Not extracted.'}

---

## Conclusion
{conclusion[:2500] if conclusion else 'Not extracted.'}

---

## Key Statistics / Numbers Detected
{chr(10).join('- ' + n for n in numbers) if numbers else '- See full paper for quantitative results.'}

---
"""
    note_path = NOTES_DIR / f"{cite_key}.md"
    note_path.write_text(note, encoding="utf-8")
    all_output.append(note)
    print(f"  -> {note_path.name}")


# ── Write the master combined notes file ─────────────────────────────────────
combined = Path(r"D:\GW-Thesis\ALL_PAPER_NOTES.md")

toc = """# ALL PAPER NOTES — Thesis Reference Guide
*ML-Based Groundwater Potential Mapping, Pothohar Plateau*
*Generated from 17 full PDFs*

## Quick Chapter Reference

| Chapter | Papers to Cite |
|---------|----------------|
| Ch.1 Introduction | `jasechko2024gwdecline` (global GW crisis) |
| Ch.2 Literature Review | `arulbalaji2019gisahp`, `das2018pravara`, `pande2021ahpmif`, `mallick2019fuzzyahp`, `benjmel2020morocco` |
| Ch.2 Study Area | `hafeez2025rwh`, `khan2023rainfallrunoff`, `sarwar2022soandrought`, `waseem2022drought`, `waseem2024waterquality`, `khan2024afforestation` |
| Ch.3 Methodology (Data) | `poggio2021soilgrids` (MANDATORY — SoilGrids), `chang2019scaleeffects` (SRTM 30m) |
| Ch.3 Methodology (ML) | `sahin2020ensembletree` (XGBoost vs RF benchmark) |
| Ch.3 Label Generation | `roy2019knowledgedriven`, `swain2020floodahp` (knowledge-driven labeling) |
| Ch.4 Results | All ML papers for comparison context |
| Ch.5 Discussion | `hafeez2025rwh`, `benjmel2020morocco`, `khan2023rainfallrunoff` |

---

"""

combined.write_text(toc + "\n\n---\n\n".join(all_output), encoding="utf-8")
print(f"\nSaved: {combined}")
print(f"Individual notes: {NOTES_DIR}")
print(f"Total: {len(all_output)} papers")
