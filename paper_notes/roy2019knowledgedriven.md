# roy2019knowledgedriven

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Landslide susceptibility mapping using knowledge driven statistical models in Darjeeling District, West Bengal, India |
| **Authors** | Jagabandhu Roy, Sunil Saha |
| **Year** | 2019 |
| **Venue** | Geoenvironmental Disasters |
| **DOI** | 10.1186/s40677-019-0126-8 |
| **Citations** | 178 |
| **BibTeX key** | `\cite{roy2019knowledgedriven}` |

---

## Thesis Relevance
**Category:** methodology_analog
**Why cite:** Knowledge-driven statistical labeling â€” directly justifies your weighted-overlay label generation.
**Relevance signals:** Uses RANDOM FOREST | Uses ENSEMBLE | Topic: groundwater potential | Uses NDVI feature | Uses TWI feature | Uses TOPOGRAPHIC WETNESS feature | Uses LANDSAT feature
**Chapter placement:** Chapter 3 §3.4 (Model validation / comparison framework)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 3 §3.2 (Label Generation): "Knowledge-driven label generation via weighted overlay
  is an established methodology for spatial hazard mapping \cite{roy2019knowledgedriven};
  Roy and Saha (2019) used fuzzy-AHP and LNRF expert knowledge weights (rainfall, slope,
  aspect, geology, soil, NDVI, TWI) achieving ROC-AUC = 0.91, validating expert-knowledge
  label generation as a reliable training-label source for ML models."


---

## Abstract
Landslide is an important geological hazard in the large extent of geo-environment, damaging the human lives and properties. The present work, intends to identify the landslide susceptibility zones for Darjeeling, India, using the ensembles of important knowledge driven statistical technique i.e. fuzzy logic with Landslide Numerical Risk Factor (LNRF) and Analytical Hierarchical Process (AHP). In the study area, 326 landslides have been identified and a landslide inventory map has been prepared based on these landslides. The landslide inventory map has considered as the dependent factor and the geo-environmental factors like rainfall, slope, aspect, altitude, geology, soil texture, distance from river, lineament and road, land use/ land cover, NDVI and TWI have been considered as independent factors. Landslide susceptibility maps were prepared based on the Fuzzy- Landslide Numerical Risk Factor (LNRF) and Fuzzyanalytic hierarchy process (AHP) methods in a GIS environment. According to the results of LNRF and AHP based fuzzy logic 34 and 22% areas are highly susceptible to landslide in this district. The landslide maps of both models have been validated through ROC curve and RMSE. The areas under curves are 91% (for Fuzzy-LNRF) and 90% (for Fuzzy-AHP) and RMSE values of these models are 0.18 and 0.14 which are indicating the good accuracy of both models in the identification of landslide susceptibility zones. Moreover, the Fuzzy-LNRF model is promising and sufficient to be advised as a method to prepare landslide susceptibility map at regional scale. Keywords: Landslide numerical risk factor (LNRF), Fuzzy-AHP, Fuzzy logic (FL), Landslide susceptibility, GIS

---

## Methodology
Min Max Rainfall (mm) 1877 2334 1. 1877.38–1991.9 Natural Break 2. 1991.97–2090.54 3. 2090.45–2167.44 4. 2167.44–2239.06 5. 2239.06–2333.96 Slope (Degree) 0 79.2 1. 0–9.32 Natural Break 2. 9.32–18.64 3. 18.44–27.34 4. 27.34–36.66 5. 5. 36.66–79.23 Altitude (m) 15 3602 1. 15–422.93 Natural Break 2. 422.93–985.6 3. 985.6–1576.4 4. 1576.4–2279.73 5. 5. 2279.73–3602 Aspect – – 1. Flat (−1) Equal interval 2. North (0–22.5) 3. Northeast (22.5–67.5) 4. East (67.5–112.5) 5. Southeast (112.5–157.5) 6. South (157.5–202.5) 7. Southwest (202.5–247.5) 8. West (247.5–292.5) 9. Northwest (292.5–337.5) 10. north(337.5–360) Geology – – 1. Triassic lithological units 2. Cenozoic 3. Pliocene-Pleistocene, 4. Holocene 5. Middle-upper Pleistocene Soil texture – – 1. Gravelly loamy, soil texture classes 2. Fine loamy - Coarse Loamy 3. Gravelly loamy Skeletol 4. Gravelly Loam - Coarse Loamy 5. Coarse Loamy Distance from River (km) 0 4.33 1. 0–0.42 Natural Break 2. 0.42–1.10 3. 1.10–1.66 4. 1.66–2.26 5. 2.26–4.33 Distance from Lineament (km) 0 10.1 1. 0–1.54 Natural Break 2. 1.54–2.85 3. 2.85–4.20, 4 4. 4.20–5.75 5. 5.75–10.12 Distance from Road (km) 0 16.5 1. 0–1.74 Natural Break 2. 1.74–3.94 Roy and Saha Geoenvironmental Disasters (2019) 6:11 Page 7 of 18 is shown in the following equation (Mcbratney and Odeh 1997). A ¼ x; μA x ð Þ   for each xεX ð2Þ Where, μA is the MF (membership of x in fuzzy set A) so that: If x does not belong to A then μA = 0. If x belongs completely to A then μA = 1. If x x belongs in a certain degree to A then 0 < μA x ð Þ < 1 According to Eq. 3 MF was used for rainfall, elevation, aspect, slope, NDVI, TWI [8]. μA x ð Þ ¼ f x ð Þ ¼ 0 x≤a x ‐a=b‐a a≻x≺b 1 x≥b 8 < : 9 = ; ð3Þ Where x is the input data and a, b are the limit values. For geology, soil texture, distance from river, distance from lineament, LULC and distance from road the following MF has been used [4]. μA x ð Þ ¼ f x ð Þ ¼ 0 x≤a b ‐x=b‐a a≻x≺b 1 x≥b 8 < : 9 = ; ð4Þ Fuzzy gamma operators Several fuzzy operators exist for combining membership functions such as AND, OR, SUM, PRODUCT and GAMMA. In the present study, gamma operator has been used for combining membership functions. Fuzzy gamma operation has been calculated using eqs. (5). μγ ¼ μsum ð Þkγ: μproduct   :1−γ ð5Þ The exponent γ, which is a number from < 0, 1 > interval, allows optimization of the membership combination. Setting it to the extremes of the interval give either fuzzy algebraic sum (γ = 1) or fuzzy algebraic product (γ =

---

## Results & Findings
Application of fuzzy-LNRF model The spatial distribution of average annual rainfall of the study area ranges from 1877.38 mm to 2333.96 mm (Fig. 3a) respectively. The rainfall map has been categorized into five classes such as very low (1877 mm–1991 mm), low (1991 mm–2090 mm), moderate (2090 mm– 2167 mm), high (2167 mm–2239 mm) and very high (2239 mm–2333 mm) respectively. The high sub-class of rainfall with 36.31% area is covered the 68.29% landslides of the study area (Table 3). The LNRF values have been calculated and converted into fuzzy membership (FM) value. Here, high rainfall sub-class has attained the highest FM value i.e. 1, indicating the high risk of landslide than other sub-class of rainfall (Table 3). The spatially the slope of the study area ranges from 0 to 79.23° (Fig. 3b). It has been classified into five categories such as very low (0°-9.32°), low (9.32°-18.64°), medium (18.44° -27.34°), high (27.34° – 36.66°) and very high (36.66°-79.23°) classes based natural break classification method in GIS environment. The high and very high slope classes are covered with 31% and 28% landslides area. The fuzzy membership values of these sub-classes are nearer to 1, representing as high landslides risk areas. The altitude of the study area ranges from 15 m to 3602 m (Fig. 3c) respectively. The altitudinal map has been categorized into five classes such as very low (15 m to 422.93 m), low (422.93 m to 985.6 m), medium (985.6 m to 1576.4 m), high (1576.4 m to 2279.73 m) and very high (2279 m–3602 m). The low elevation class is covered with 51.93% landslide area (Table 3). The fuzzy membership value of 422.93 m–985.6 m elevation range is 1, representing higher landslide susceptibility than other sub-layers. Aspect of the study area has been classified into several categories such as flat, north, northeast, east, southeast, south, southwest, west and northwest. South sub-layer with 14.32% area is covered 27.04% landslide area. Geologically, the study area is composed of five geological segments namely Triassic, Cenozoic, Pliocene-Pleistocene, Holocene and Middleupper Pleistocene (Fig. 3e). Triassic geological segment with 52.75% area is encompassed with 70.21% landslide area. According to the LNRF model using fuzzy logic, the Triassic geological segment has attained the maximum LNRF and fuzzy membership value. The other sub-layers of geological segment are indicating the less probability of landslide occurrence. Pedagogically, the region is composed wit

---

## Conclusion
For the prevention of human lives and property, a short and long-term solution is necessary for mitigating the landslide risk in this region. At present day, landslide is to be considered the most serious natural hazards in the Darjeeling district. The study has been adopted the suitable multi-criteria decision making approaches like Fuzzy-AHP and Fuzzy-LNRF to outline the landslide susceptibility zones. The landslide susceptibility maps of both models have been categorized into three classes such as low, moderate and high landslide susceptibility zones. The high landslide susceptibility zone has been found in the middle and northern portions of the study area because of the presence of fragile soil, high concentration of drainage, frequent heavy rainfall and sloppy land. Among these two ensemble models, Fuzzy-LNRF is showing better acceptability than the other model. So, the study has been done by these two ensemble models help to understand the landslide hazards problem of an area. The study also provides the essential information to the planner, government, local people and researchers to take suitable steps for the reduction and the mitigation of the landslides problems in the Darjeeling district. Abbreviations AHP: Analytical hierarchical process; ASTER: Advanced space borne thermal emission and reflection radiometer; DEM: Digital elevation map; GIS: Geographical information system; LNRF: Landslide Numerical Risk Factor; LSM: Landslide susceptible map; LULC: Land use/Land cover; MCDA: Multicriteria decision approach; MF: Membership function; NDVI: Normalized differential vegetation index; OLI: Operational land imager; RMSE: Root mean square error; ROC: Receiver operating characteristic; TM: Thematic mapper; TWI: Topographical wetness index; VIF: Variance inflation factors Acknowledgments Authors would like to thanks the inhabitants of Darjeeling District because they have helped a lot during our field visit. The authors would like to give special thanks to two anonymous reviewers for their constructive and useful comments during the review process. Also we would like to cordially thank the Mr. Arnab Chatterjee, Assistant Professor, Department of English, Harishchandrapur College, Pipla, Malda for correcting the grammers and language. At last, authors would like to acknowledge all of the agencies and individuals specially, Survey of India (SOI), Geological Survey of India (GSI) and USGS for obtaining the maps and data required for the study. Authors’ c

---

## Key Statistics / Numbers Detected
- AUC values of 91%

---
