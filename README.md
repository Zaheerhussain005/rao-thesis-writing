# ML-Based Groundwater Potential Mapping — Pothohar Plateau, Pakistan

M.Sc. thesis project applying machine learning to identify groundwater potential zones (GWPZ) across the Pothohar Plateau, Punjab, Pakistan (~25,000 km²).

## Overview

This study integrates multi-source geospatial data with ensemble machine learning models to produce a groundwater potential map for the Pothohar Plateau — a semi-arid region spanning five districts (Rawalpindi, Chakwal, Attock, Jhelum, Mianwali) where rainfed agriculture is critically dependent on groundwater.

**Key features used:** Elevation, Slope, Aspect, TWI, NDVI, NDWI, Rainfall, Soil texture, LST (nine features, 30 m resolution, ~37 million valid pixels)

**Models evaluated:** Random Forest, XGBoost, LightGBM, and a soft-voting Ensemble (5-fold cross-validation, ROC-AUC, Cohen's κ). XGBoost was the best model (99.12% test accuracy, AUC 0.9998).

## Repository Structure

```
.
├── main.tex                     # Root LaTeX document
├── settings.tex                 # LaTeX packages and formatting
├── references.bib               # BibTeX bibliography
│
├── chapters/                    # Thesis chapter source files
│   ├── 01_introduction.tex
│   ├── 02_literature_review.tex
│   ├── 03_methodology.tex
│   ├── 04_results.tex
│   ├── 05_discussion.tex
│   └── 06_conclusion.tex
│
├── preliminary/                 # Front matter
│   ├── title_page.tex
│   ├── abstract.tex
│   ├── acknowledgement.tex
│   └── ...
│
├── appendices/                  # Appendix files
│
├── figures/                     # Generated maps and plots (PNG)
│
├── paper_notes/                 # Structured notes on reference papers (Markdown)
│
├── papers.json                  # Paper metadata index
│
├── ALL_PAPER_NOTES.md           # Consolidated literature notes
├── THESIS_KNOWLEDGE_BASE.md     # Chapter-by-chapter writing guide
│
├── deep_extract.py              # PDF data extraction script
├── extract_paper_notes.py       # Paper note generation script
├── mcp_thesis_papers.py         # MCP server for paper search
└── generate_methodology_figures.py
```

## Compiling the Thesis

Requires a LaTeX distribution (TeX Live, MiKTeX, or Overleaf). **This document uses XeLaTeX** (for `fontspec`); it will *not* build with pdfLaTeX.

```bash
xelatex main
bibtex  main
xelatex main
xelatex main
```

On **Overleaf**: upload the repository, then set Menu → Compiler → **XeLaTeX**
(the `% !TEX program = xelatex` line in `main.tex` usually sets this automatically).

## Study Area

The Pothohar Plateau lies in northern Punjab between the Indus and Jhelum rivers. Annual rainfall ranges from 380–500 mm (mostly monsoon, July–October). Groundwater is the primary water source for both domestic use and barani (rainfed) agriculture.

## Dependencies

Python scripts require:
```
geopandas, rasterio, scikit-learn, xgboost, matplotlib, numpy, pandas
```
