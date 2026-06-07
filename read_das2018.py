import fitz
from pathlib import Path

doc = fitz.open(r"D:\GW-Thesis\papers\das2018pravara.pdf")
print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    print(f"\n{'='*60}")
    print(f"PAGE {i+1}")
    print('='*60)
    print(page.get_text())
doc.close()
