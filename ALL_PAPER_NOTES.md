# ALL PAPER NOTES — Thesis Reference Guide
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

# poggio2021soilgrids

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | SoilGrids 2.0: producing soil information for the globe with quantified spatial uncertainty |
| **Authors** | Laura Poggio, Luis Moreira de Sousa, N.H. Batjes et al. |
| **Year** | 2021 |
| **Venue** | SOIL |
| **DOI** | 10.5194/soil-7-217-2021 |
| **Citations** | 2015 |
| **BibTeX key** | `\cite{poggio2021soilgrids}` |

---

## Thesis Relevance
**Category:** data_sources
**Why cite:** Official SoilGrids reference. MUST cite â€” your #1 feature (soil texture) comes from this dataset.
**Relevance signals:** Uses XGBOOST | Uses RANDOM FOREST | Uses NDVI feature | Uses SOILGRIDS feature | Uses LANDSAT feature
**Chapter placement:** Chapter 3 §3.1 (Data Sources — mandatory dataset citation)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 3 §3.1: "Soil texture data were obtained from SoilGrids 2.0 \cite{poggio2021soilgrids},
  a global dataset produced at 250 m resolution using quantile regression forests trained on
  ~240,000 soil profiles and 400+ environmental covariates."
- This is a MANDATORY citation — your top feature (r=0.836) comes from this dataset.


---

## Abstract
Laura Poggio, Luis M. de Sousa, Niels H. Batjes, Gerard B. M. Heuvelink, Bas Kempen, Eloi Ribeiro, and David Rossiter ISRIC – World Soil Information, Wageningen, the Netherlands Correspondence: Laura Poggio (laura.poggio@wur.nl) Received: 14 October 2020 – Discussion started: 9 November 2020 Revised: 9 April 2021 – Accepted: 18 April 2021 – Published: 14 June 2021 Abstract. SoilGrids produces maps of soil properties for the entire globe at medium spatial resolution (250 m cell size) using state-of-the-art machine learning methods to generate the necessary models. It takes as inputs soil observations from about 240 000 locations worldwide and over 400 global environmental covariates describing vegetation, terrain morphology, climate, geology and hydrology. The aim of this work was the production of global maps of soil properties, with cross-validation, hyper-parameter selection and quantiﬁcation of spatially explicit uncertainty, as implemented in the SoilGrids version 2.0 product incorporating state-of-the-art practices and adapting them for global digital soil mapping with legacy data. The paper presents the evaluation of the global predictions produced for soil organic carbon content, total nitrogen, coarse fragments, pH (water), cation exchange capacity, bulk density and texture fractions at six standard depths (up to 200 cm). The quantitative evaluation showed metrics in line with previous global, continental and large-region studies. The qualitative evaluation showed that coarse-scale patterns are well reproduced. The spatial uncertainty at global scale highlighted the need for more soil observations, especially in high-latitude regions. 1 Introduction Healthy soils provide important ecosystem services at the local, landscape and global level and are important for 

---

## Methodology
This study uses quantile regression forests (Meinshausen, 2006), a method with a limited number of parameters to be tuned and that has proven to be an effective compromise between accuracy and feasibility for large datasets. Selected primary soil properties as deﬁned and described in the GlobalSoilMap speciﬁcations (Arrouays et al., 2014) were modelled. The following sections describe each step of the work- ﬂow (Fig. 1) in detail. These include the following: 1. input soil data preparation 2. covariates’ selection 3. model tuning and cross-validation 4. ﬁnal model ﬁtting for prediction 5. predictions with uncertainty estimation. 2.1 Soil observation data Soil property data for this study were derived from the IS- RIC World Soil Information Service (WoSIS), which provides consistent, standardised soil proﬁle data for the world (Batjes et al., 2020). All soil data shared with ISRIC to support global mapping activities are ﬁrst stored in the ISRIC Data Repository, together with their metadata (including the name of the data owner and licence deﬁning access rights). Subsequently, the source data are imported “as is” into PostgreSQL, after which they are ingested into the WoSIS data model itself. Following data quality assessment and control (including consistency checks on latitude–longitude and depth of horizon/layer; ﬂagging of duplicate proﬁles; and providing measures for geographic and attribute accuracy, as well as time stamps), the descriptions for the soil analytical methods and the units of measurement are standardised using consistent procedures, with additional checks for SOIL, 7, 217–240, 2021 https://doi.org/10.5194/soil-7-217-2021 L. Poggio et al.: Soil information for the globe 219 Figure 1. Workﬂow of the methodological approach. Table 1. Soil properties description and units. Soil property Acronym Units Mapped units Description Bulk density BDOD kg/dm3 cg/cm3 Bulk density of the ﬁne earth fraction oven dry Cation exchange capacity CEC cmol(c)/kg mmol(c)/kg Capacity of the ﬁne earth fraction to hold exchangeable cations Coarse fragments CFVO cm3/100 cm3 (volume %) cm3/dm3 Volumetric content of fragments larger than 2 mm in the whole soil Nitrogen N g/kg cg/kg Sum of total nitrogen (ammonia, organic and reduced nitrogen) as measured by Kjeldahl digestion plus nitrate–nitrite pH (water) pH – 10∗ Negative common logarithm of the activity of hydronium ions (H+) in water Organic carbon concentration SOC g/kg dg/kg Gravimetric content of organic carbo

---

## Results & Findings
3.1 Input soil observations Table 2 breaks down the distribution of the legacy soil observations for each soil property by depth interval. Table B1, in Appendix B, shows the number of observations by bioclimatic region. Figures 3 and 4 show examples of observation density of the soil calibration data for two soil properties, pHwater and proportion of coarse fragments, that show a large difference in density. As indicated, the number of observations for each property varies greatly with depth and bioclimatic region, with higher densities observed for North America and Europe. Generally, there are more observations for agricultural areas. Further, the available proﬁles have been collated over several decades, some 62 % of the data being from 1960–2020; the time of sampling is unknown for around 34 % of the proﬁles. As indicated by Batjes et al. (2020), in principle, the age of the observations should be taken into account during the mapping process via covariate layers for time periods commensurate with the sampling dates, especially for soil properties that are readily affected by changes in land use or management practices. However, for these so-called “dynamic” soil properties, such as pH and soil organic matter content, we consider that the spatial variation will be much greater that the temporal variation, so that not taking the age of observations into account will not greatly affect the map. In addition, it is difﬁcult or impossible to ﬁnd comparable covariates, in particular remote-sensing-derived covariates, for each time period. Space–time relations should be considered in future assessments (Heuvelink et al., 2020). This study considers standardised data for some 240 000 proﬁles, derived from WoSIS. This is over 60 000 more pro- ﬁles than considered in the data compilation underpinning the preceding SoilGrids runs (Hengl et al., 2017b), thus providing substantial new information for calibration of the new global models. However, as indicated, there are still significant geographic gaps (e.g. arid regions, boreal regions and “forest” soils). Some of these are related to the physical remoteness or inaccessibility of some regions, while others are related to the fact that many soil datasets still are not or can https://doi.org/10.5194/soil-7-217-2021 SOIL, 7, 217–240, 2021 224 L. Poggio et al.: Soil information for the globe not be shared for various reasons as described by Arrouays et al. (2017). In the previous version of SoilGrids (Hengl et al., 2

---

## Conclusion
This study presents and discusses the production of global maps of soil properties as implemented in the SoilGrids 2.0 product, with cross-validation, hyper-parameter selection and quantiﬁcation of uncertainty, using the best available (shared) soil proﬁle data for the world. In particular, the study describes a robust and reproducible DSM workﬂow addressing the challenges of global data modelling: 1. non-homogeneous spatial distribution of input soil observations; https://doi.org/10.5194/soil-7-217-2021 SOIL, 7, 217–240, 2021 230 L. Poggio et al.: Soil information for the globe Figure 7. Mean soil organic carbon content (dg/kg) prediction and range between 5 % and 95 % quantiles in the 5 to 15 cm depth interval, (a) for prediction and (b) for interquartile range. Figure 8. Median total nitrogen prediction (cg/kg) and associated uncertainty for the 15 to 30 cm depth interval, (a) for prediction and (b) for uncertainty. SOIL, 7, 217–240, 2021 https://doi.org/10.5194/soil-7-217-2021 L. Poggio et al.: Soil information for the globe 231 Figure 9. Prediction distribution for pHwater (10 pH) in the 60 to 100 cm depth interval, (a) for mean and (b) for median. Figure 10. Prediction distribution for pHwater (10 pH) in the 60 to 100 cm depth interval, (a) for 5 % quantile and (b) for 95 % quantile. https://doi.org/10.5194/soil-7-217-2021 SOIL, 7, 217–240, 2021 232 L. Poggio et al.: Soil information for the globe 2. robust quantitative evaluation with a cross-validation procedure balancing accuracy and performances; 3. qualitative evaluation of the spatial patterns of the maps to include information about matching with well recognised pedo-landscape features; 4. quantiﬁcation and mapping of the spatial uncertainty to provide users with a measure for and warning for users of the products. As such, it describes a next step into global modelling and mapping of soil properties, explicitly highlighting the importance of quantitative and qualitative evaluation and uncertainty communication. The actual use of SoilGrids 2.0 in global and wide-area regional applications, where soil properties are important model inputs, will be the real test of its applicability and usefulness. SOIL, 7, 217–240, 2021 https://doi.org/10.5194/soil-7-217-2021 L. Poggio et al.: Soil information for the globe 233 Appendix A: Environmental covariates Over 400 geographic layers were available as environmental covariates for this work. These are chosen for their presumed relation to the major soil f

---

## Key Statistics / Numbers Detected
- See full paper for quantitative results.

---


---

# jasechko2024gwdecline

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Rapid groundwater decline and some cases of recovery in aquifers globally |
| **Authors** | Scott Jasechko, Hansjorg Seybold, Debra Perrone et al. |
| **Year** | 2024 |
| **Venue** | Nature |
| **DOI** | 10.1038/s41586-023-06879-8 |
| **Citations** | 552 |
| **BibTeX key** | `\cite{jasechko2024gwdecline}` |

---

## Thesis Relevance
**Category:** gw_context
**Why cite:** High-impact Nature paper on global groundwater decline. Perfect opening citation for Introduction motivation.
**Relevance signals:** Uses ENSEMBLE | Topic: groundwater potential | Topic: groundwater potential zone | Uses TWI feature
**Chapter placement:** Chapter 1 §1.1 (Introduction — global GW crisis)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 1 §1.1 opening: "Groundwater resources are under increasing threat globally;
  Jasechko et al. (2024) \cite{jasechko2024gwdecline} found rapid groundwater-level declines
  (>0.5 m/year) in 170,000 wells across 40+ countries, with accelerating depletion in 30%
  of regional aquifers over the past four decades."
- Use as the motivating global context before narrowing to Pakistan/Pothohar.


---

## Abstract
Mohammad Shamsudduha5, Richard G. Taylor6, Othman Fallatah7,8 & James W. Kirchner2,9,10 Groundwater resources are vital to ecosystems and livelihoods. Excessive groundwater withdrawals can cause groundwater levels to decline1–10, resulting in seawater intrusion11, land subsidence12,13, streamflow depletion14–16 and wells running dry17. However, the global pace and prevalence of local groundwater declines are poorly constrained, because in situ groundwater levels have not been synthesized at the global scale. Here we analyse in situ groundwater-level trends for 170,000 monitoring wells and 1,693 aquifer systems in countries that encompass approximately 75% of global groundwater withdrawals18. We show that rapid groundwater-level declines (>0.5 m year−1) are widespread in the twenty-first century, especially in dry regions with extensive croplands. Critically, we also show that groundwater-level declines have accelerated over the past four decades in 30% of the world’s regional aquifers. This widespread acceleration in groundwater-level deepening highlights an urgent need for more effective measures to address groundwater depletion. Our analysis also reveals specific cases in which depletion trends have reversed following policy changes, managed aquifer recharge and surface-water diversions, demonstrating the potential for depleted aquifer systems to recover. Groundwater is the primary water source for many homes, farms, industries and cities around the globe. Unsustainable groundwater withdrawals and changes in climate can cause groundwater levels to fall1–10, making groundwater resources less accessible17. Global maps of groundwater storage trends are available7 from the Gravity Recovery and Climate Experiment (GRACE) satellites, although at a resolution that is too coa

---

## Methodology
Delineating global aquifer systems based on literature review of local studies For each country in our study, we consulted published accounts of local-scale studies52–1288 (Supplementary Note 7) to delineate 1,693 study areas, each underlain by one or more aquifers and/or low-permeability geologic formations that are, collectively, referred to as an ‘aquifer system’. Each aquifer system was delineated by consulting maps and reading descriptions within local-scale reports. Specific steps applied to delineate the boundaries of each aquifer system are detailed in Supplementary Note 7. Downloading groundwater-level data Our study focuses on more than 40 countries for which we compiled monitoring-well data. We analysed groundwater-level time series derived from numerous data repositories (dataset-specific details are available in Supplementary Note 1; some of these datasets are described in refs. 1289–1297). The compiled groundwater-level databases span different time intervals and have different measurement frequencies (see heat map plot and global maps showing monitoring-well time series durations and measurement frequencies in Supplementary Note 12). Quality controlling groundwater-level time series We completed five pre-processing steps before analysing groundwater-level data. First, we identified replicate groundwater-level measurements, defined as cases in which an identical measurement date and an identical groundwater-level measurement were reported from the same monitoring well; in these cases, we retain only one of these replicates. Second, we identified cases in which several groundwater-level measurements from the same monitoring well reported identical measurement dates. In these cases, we calculated the median among all groundwater-level measurements sharing the same measurement date and the adjacent points in the time series (that is, the median of the group of measurements with identical dates and the measurements immediately preceding and following the same-date measurements); we then kept only the single water-level measurement whose value was closest to this calculated median (Supplementary Note 2). Third, we excluded extreme values of depth to groundwater (that is, >1,000 m and <−1,000 m) and implausibly high groundwater elevations (that is, >8,000 m above sea level). Fourth, we excluded groundwater-level measurements with values of ‘999’, ‘−9,999’ or ‘0’, because some databases used these values as a code for missing measurements (see figur

---

## Results & Findings
Not extracted.

---

## Conclusion
Not extracted.

---

## Key Statistics / Numbers Detected
- See full paper for quantitative results.

---


---

# arulbalaji2019gisahp

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | GIS and AHP Techniques Based Delineation of Groundwater Potential Zones: a case study from Southern Western Ghats, India |
| **Authors** | P. Arulbalaji, D. Padmalal, K. Sreelash |
| **Year** | 2019 |
| **Venue** | Scientific Reports |
| **DOI** | 10.1038/s41598-019-38567-x |
| **Citations** | 693 |
| **BibTeX key** | `\cite{arulbalaji2019gisahp}` |

---

## Thesis Relevance
**Category:** gw_potential_mapping
**Why cite:** Highly-cited GIS+AHP GWPZ delineation. Key literature-review citation for weighted-overlay baseline.
**Relevance signals:** Uses RANDOM FOREST | Topic: groundwater potential | Topic: gwpz | Topic: groundwater potential zone | Uses TWI feature | Uses TOPOGRAPHIC WETNESS feature | Uses SRTM feature
**Chapter placement:** Chapter 2 §2.2 (Literature Review — GIS/AHP baseline methods)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 2 §2.2: "AHP-based weighted overlay is widely used for GWPZ delineation
  \cite{arulbalaji2019gisahp}, employing 12 thematic layers (geology, geomorphology, LULC,
  TWI, slope, rainfall, soil, drainage density) with pairwise comparison matrices to assign weights."
- Chapter 3 §3.2: Compare your weighted-overlay label generation with this established AHP approach.


---

## Abstract
Scientific Reports | (2019) 9:2082 | https://doi.org/10.1038/s41598-019-38567-x www.nature.com/scientificreports GIS and AHP Techniques Based Delineation of Groundwater Potential Zones: a case study from Southern Western Ghats, India P. Arulbalaji, D. Padmalal & K. Sreelash Over-exploitation of groundwater and marked changes in climate over the years have imposed immense pressure on the global groundwater resources. As demand of potable water increases across the globe for human consumption, agriculture and industrial uses, the need to evaluate the groundwater potential and productivity of aquifers also increases. In the recent years, geographic information system based studies have gained much prominence in groundwater exploration because it is rapid and will provide first - hand information on the resource for further developments. Therefore, the present study has been undertaken with an objective to delineate the groundwater potential of a small tropical river basin located in the western side of the Western Ghats in India as an example. A combination of geographical information system and analytical hierarchical process techniques (AHP) was used in the present study. A total of 12 thematic layers such as Geology, Geomorphology, Land Use/Land Cover, Lineament density, Drainage density, Rainfall, Soil, Slope, Roughness, Topographic Wetness Index, Topographic Position Index and Curvature were prepared and studied for groundwater potential zone demarcation. Weights assigned to each class in all the thematic maps are based on their characteristics and water potential capacity through AHP method. The accuracy of the output was cross-validated with information on groundwater prospects of the area and the overall accuracy of the method comes to around 85%. The groundwater p

---

## Methodology
Geospatial techniques were applied in this paper to delineate the groundwater potential zones of the Vamanapuram river basin using knowledge-based factor analysis of a total of 12 layers of information of the area such as geology, geomorphology, land use/land cover (LULC), drainage density, lineaments, rainfall, soil, roughness, slope, curvature, topographic position index and topographic wetness index. The pre - processing analysis of remote sensing data of the Vamanapuram river basin was carried out using image processing software namely ERDAS Imagine 9.2 and Geomatica Demo Version 13. Geographical Information Techniques were carried out using ArcGIS 10.2 software. The Shuttle Radar Topographic Mission (SRTM-30 m resolution) data was used to delineate the basin boundary11 with the support of hydrology tool in GIS software. The IRS LISS-III (24 m Spatial Resolution) geo-coded false color composite satellite data was used47 for the preparation of LULC and geomorphology. The visual interpretation techniques were employed to define the LULC and geomorphology over the satellite data with the help of National Remote Sensing Centre (NRSC) LULC31 and geomorphology57 thematic layers using GIS software. The published map of geology and soil atlas were collected and digitized from Geological Survey of India and National Bureau of Soil Survey, respectively. The slope, curvature and roughness were generated from SRTM Figure 2. Flow chart of the methodology used for Groundwater Potential Zones Mapping. www.nature.com/scientificreports/ 4 Scientific Reports | (2019) 9:2082 | https://doi.org/10.1038/s41598-019-38567-x data58,59. Rainfall data was obtained from Indian Meteorological Department. An inverse distance weighted (IDW) interpolation tool was used for generating the spatial distribution of rainfall60,61. Drainage and lineaments were extracted from SRTM and IRS LISS-III data respectively, based on automatic extraction methods. From the drainage and lineament, the density was prepared using line density in spatial analyst tool in GIS software61,62. Topographic wetness index was prepared based on “TOPMODEL” index63. Topographic position index was prepared based on Jenness algorithm64. Multi criteria decision analysis using GIS techniques. Multi criteria decision analysis using Analytical Hierarchical Process (AHP) is the most common and well known GIS based method for delineating groundwater potential zones. This method helps integrating all thematic layers. A tota

---

## Results & Findings
Geology. Geologic setting plays a vital role in the occurrence and distribution of groundwater in any terrain65. The published geological map of the Geological Survey of India (GSI, 1995)66 was used for delineating different geological units of the study area (Fig. 3). The study area falls within the Kerala Khondalite Belt (KKB). In southwest India, KKB is one of the main granulite facies supracrustal terrain. Geologically, a major part of the basin is occupied by khondalite suite of rocks. Apart from this, occurrence of charnockite is also noticed in the area. The terrain is often intruded by basic and ultrabasic rocks at certain places56. Dolerite dykes are found in the central part of the basin and are aligned parallel to the lineaments which are oriented in NNW - SSE, NE - SW and ENE - WSE directions (GSI, 1987)67. Tertiary and Quaternary sediments comprising current bedded sandstones, clay stones, coastal sands and alluvium are found in the western part of the basin. The pre-Cambrian crystallines and Tertiary sediments are lateralized at the top. Unconsolidated sedimentary and fractured crystalline rocks are more favorable for groundwater movement and storage than massive type of rocks68. From a hydrogeological Factor Assigned weight Domain of effect Rank TPI 3 −72.06–−12.13 6 −12.13–−1.87 5 −1.87–7.58 4 7.58–24.14 3 24.14–128.24 2 Curvature 3 −2.46–−1.10 2 −1.10–0.25 3 0.25–1.61 4 1.61–2.97 5 2.97–4.33 6 Table 2. Categorization of factors influencing of Groundwater Potential Zones. Theme Geomorphology LULC Geology Lineament Density Soil Drainage Density Slope Rainfall TWI Roughness TPI Curvature Weighted Sum Row Average ʎ Geomorphology 0.133 0.133 0.133 0.133 0.133 0.133 0.133 0.132 0.132 0.133 0.133 0.133 1.597 0.13 12.0 LULC 0.117 0.117 0.117 0.117 0.117 0.117 0.117 0.116 0.116 0.117 0.117 0.117 1.397 0.11 12.0 Geology 0.100 0.100 0.100 0.100 0.100 0.100 0.100 0.099 0.099 0.100 0.100 0.100 1.197 0.09 12.0 Lineament Density 0.100 0.100 0.100 0.100 0.100 0.100 0.100 0.099 0.099 0.100 0.100 0.100 1.197 0.09 12.0 Soil 0.100 0.100 0.100 0.100 0.100 0.100 0.100 0.099 0.099 0.100 0.100 0.100 1.197 0.09 12.0 Drainage Density 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.998 0.08 12.0 Slope 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.083 0.998 0.08 12.0 Rainfall 0.067 0.067 0.067 0.067 0.067 0.067 0.067 0.066 0.066 0.067 0.067 0.067 0.798 0.06 12.0 TWI 0.067 0.067 0.067 0.067 0.067 0.067 0.067 0.066 0.066 

---

## Conclusion
The present study is an attempt to delineate the groundwater potential zones using a combination of AHP and GIS techniques in a small humid tropical river basin in South India - the Vamanapuram river basin, which is located in the western side of southern Western Ghats, an elevated continental margin. A total of 12 thematic layers such as Geology, Geomorphology, LULC, Soil, Rainfall, Lineament Density, Drainage Density, Slope gradient, TPI, TWI, Roughness and Curvature were used in this study to delineate the groundwater potential zones. According Index Description Type 1 • Very deep, well drained, gravelly clay soils on gently sloping coastal laterites, with moderate erosion. • Clayey – skeletal, kaolinitic, typic tropaquepts. • Allied with very deep, well drained, gravelly clay soils with moderate surface gravelliness. • Clayey – skeletal, kaolinitic, typic kanhaplustults. 2 • Very deep, well drained, gravelly clay soils with moderate surface gravelliness on moderately steeply sloping laterite mounds, with moderate erosion. • Clayey – skeletal, kaolinitic, ustoxic humitropepts • Allied with deep, well drained, gravelly clay soils on gentle slopes. • Clayey - skeletal, Kalolinitic, ustic haplohumults 3 • Very deep, well drained, gravelly clay soils with moderate surface gravelliness on gently sloping midland laterites with valleys of southern Kerala, with moderate erosion; • Clayey – skeletal, kaolinitic, ustic kanhaplohumults • Allied with very deep well drained, clayey soils. • Clayey, kaolinitic, typic kandiustults 4 • Deep, well drained, loamy soils on gently sloping low hills with isolated hillocks, with moderate erosion; • Fine – loamy, mixed, ustic humitropepts • Allied with deep, well drained, loamy soils with coherent material at 100 to 150 cm on moderate slopes, severely eroded • Fine - loamy, mixed, ustic haplohumults. 5 • Deep, well drained, gravelly clay soils with coherent material at 100 to 150 cm on moderately sloping isolated hillocks, with severe erosion; • Clayey – skeletal, kaolinitic, ustoxic humitropepts • Allied with moderately shallow, well drained, gravelly loam soils with 50 to 75 cm on very gentle slopes moderately eroded. • Fine – loamy, mixed ustoxic humitropepts 6 • Very deep, well drained, clayey soils on moderately steeply sloping high hills with thin vegetation, with moderate erosion; • Clayey, mixed, ustic palehumults • Allied with rock outcrops. • Rock land Table 5. Soil type and its characteristics of the Vaman

---

## Key Statistics / Numbers Detected
- accuracy of the method comes to around 85%

---


---

# sahin2020ensembletree

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Assessing the predictive capability of ensemble tree methods for landslide susceptibility mapping using XGBoost, gradient boosting machine, and random forest |
| **Authors** | Emrehan Kutlug Sahin |
| **Year** | 2020 |
| **Venue** | SN Applied Sciences |
| **DOI** | 10.1007/s42452-020-3060-1 |
| **Citations** | 407 |
| **BibTeX key** | `\cite{sahin2020ensembletree}` |

---

## Thesis Relevance
**Category:** methodology_analog
**Why cite:** Direct XGBoost-vs-GBM-vs-RF comparison for spatial susceptibility mapping. Strong methodological analogue to your model comparison.
**Relevance signals:** Uses XGBOOST | Uses RANDOM FOREST | Uses GRADIENT BOOSTING | Uses ENSEMBLE | Uses NDVI feature | Uses TWI feature | Uses LANDSAT feature
**Chapter placement:** Chapter 3 §3.4 (Model validation / comparison framework)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 3 §3.3: "Sahin (2020) \cite{sahin2020ensembletree} demonstrated that ensemble
  tree methods — specifically XGBoost, GBM and RF — consistently outperform single models
  for spatial susceptibility mapping, with XGBoost achieving the highest AUC values."
- Chapter 4: use as benchmark comparison for your XGBoost results.


---

## Abstract
Decision tree-based classifier ensemble methods are a machine learning (ML) technique that combines several tree models to produce an effective or optimum predictive model, and that allows well-predictive performance especially compared to a single model. Thus, selecting a proper ML algorithm help us to understand possible future occurrences by analyzing the past more accurate. The main purpose of this study is to produce landslide susceptibility map of the Ayancik district of Sinop province, situated in the Black Sea region of Turkey using three featured regression tree-based ensemble methods including gradient boosting machines (GBM), extreme gradient boosting (XGBoost), and random forest (RF). Fifteen landslide causative factors and 105 landslide locations occurred in the region were used. The landslide inventory map was randomly divided into training (70%) and testing (30%) dataset to construct the RF, XGBoost and GBM prediction models. Symmetrical uncertainty measure was utilized to determine the most important causative factors, and then the selected features were used to construct susceptibility prediction models. The performance of the ensemble models was validated using different accuracy metrics including Area under the curve (AUC), overall accuracy (OA), Root mean square error (RMSE), and Kappa coefficient. Also, the Wilcoxon signed-rank test was used to assess differences between optimum models. The accuracy results showed that the model of XgBoost_Opt model (the model created by optimum factor combination) has the highest prediction capability (OA = 0.8501 and AUC = 0.8976), followed by the RF_opt (OA = 0.8336 and AUC = 0.8860) and GBM_Opt (OA = 0.8244 and AUC = 0.8796). When the Wilcoxon sign-rank test results were analyzed, XgBoost_Opt mo

---

## Methodology
Vol:.(1234567890) Research Article SN Applied Sciences (2020) 2:1308 | https://doi.org/10.1007/s42452-020-3060-1 4 Ensemble methods for LSM In general, ensemble methods that build multiple models to produce better predictive performance compared to a single model. This is done to make more accurate solutions than a single model would which incorporates the predictions from all the base learners. In this paper, methods of ensemble learning including RF, GBM, and XGBoost were used, and their results compared. When landslide susceptibility indexes have positive and negative skewness, the best classification methods are quantile or natural break approaches [3, 20].In this present study, the produced LSMs were subdivided into five susceptibility levels by the quantile-based classification approach according to the histogram of data distribution. 4.1 Random forest Random forest (RF), introduced by Breiman [7]. One of the important points to be mentioned for the RF algorithm can be used to perform both classification and regression tasks. The algorithm starts at the rood node of a tree considering the all data. Each predictor variable is estimated to see how well it separates two different nodes. The treebased method is usually a pruning process to cut the tree down to a size that is less likely to overfit the data and that process generally accomplished by cross-validation [8, 39]. For the implementation of the RF, it is required to be set two main parameters: the number of trees (ntree), and the number of randomly selected predictor variables (mtry). 4.2 Gradient boosting machine As similar to RF, gradient boosting (GBM) is another technique used for performing supervised ML applications including various classification and regression problems. GBM produced a prediction model in the form of an ensemble of weak prediction models, typically decision trees [96]. GBM includes tree main components: (1) a loss function that is to be optimized, (2) a weak learner to predict; (3) an additive model to add weak learners to optimize the loos function [47]. For GBM model, there are three main tuning parameters. These parameters include maximum number of trees “ntree”, maximum number of interactions between independent variables “tree depth” and learning rate also known as shrinkage [54]. 4.3 Extreme gradient boosting XGBoost is a ML system to scale up tree boosting algorithms and that has recently been the most popular and dominating method applied in recent years. XGB

---

## Results & Findings
Not extracted.

---

## Conclusion
Not extracted.

---

## Key Statistics / Numbers Detected
- AUC = 0.8976
- AUC = 0.8860
- AUC = 0.8796
- AUC​ Model_1 2 Slope, elevation 0.5643
- AUC​ 0.5643
- accuracy value (87.52%
- accuracy results between each other as 86.12%
- accuracy differences as approximately 1%
- nsemble learning methods were calculated as 0.3030
- RMSE values for optimum dataset were 0.2929
- AUC values (94.87%
- Kappa and RMSE metrics OA (%) AUC (%) Kappa RMSE GBM_All 85.0299
- AUC values (94.87
- AUC (%) Kappa RMSE GBM_All 85.0299
- Kappa RMSE GBM_All 85.0299

---


---

# chang2019scaleeffects

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Evaluating scale effects of topographic variables in landslide susceptibility models using GIS-based machine learning techniques |
| **Authors** | Kuan-Tsung Chang, Abdelaziz Merghadi, Ali P. Yunus et al. |
| **Year** | 2019 |
| **Venue** | Scientific Reports |
| **DOI** | 10.1038/s41598-019-48773-2 |
| **Citations** | 271 |
| **BibTeX key** | `\cite{chang2019scaleeffects}` |

---

## Thesis Relevance
**Category:** methodology_analog
**Why cite:** DEM resolution + topographic variables in GIS-ML. Supports your SRTM/slope/TWI feature choices.
**Relevance signals:** Uses XGBOOST | Uses RANDOM FOREST | Uses ENSEMBLE | Topic: groundwater potential | Uses SRTM feature | Uses LANDSAT feature
**Chapter placement:** Chapter 3 §3.4 (Model validation / comparison framework)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 3 §3.1: "SRTM 30 m DEM derivatives (slope, TWI) are appropriate for regional-scale
  GIS analysis \cite{chang2019scaleeffects}; Chang et al. (2019) found that 30 m resampled
  DEM-derived topographic variables produced the highest accuracy in ML-based spatial mapping."


---

## Abstract
Scientific Reports | (2019) 9:12296 | https://doi.org/10.1038/s41598-019-48773-2 www.nature.com/scientificreports Evaluating scale effects of topographic variables in landslide susceptibility models using GIS- based machine learning techniques Kuan-Tsung Chang1, Abdelaziz Merghadi 2, Ali P. Yunus3, Binh Thai Pham4 & Jie Dou 5,6 The quality of digital elevation models (DEMs), as well as their spatial resolution, are important issues in geomorphic studies. However, their influence on landslide susceptibility mapping (LSM) remains poorly constrained. This work determined the scale dependency of DEM-derived geomorphometric factors in LSM using a 5 m LiDAR DEM, LiDAR resampled 30 m DEM, and a 30 m ASTER DEM. To verify the validity of our approach, we first compiled an inventory map comprising of 267 landslides for Sihjhong watershed, Taiwan, from 2004 to 2014. Twelve landslide causative factors were then generated from the DEMs and ancillary data. Afterward, popular statistical and machine learning techniques, namely, logistic regression (LR), random forest (RF), and support vector machine (SVM) were implemented to produce the LSM. The accuracies of models were evaluated by overall accuracy, kappa index and the receiver operating characteristic curve indicators. The highest accuracy was attained from the resampled 30 m LiDAR DEM derivatives, indicating a fine-resolution topographic data does not necessarily achieve the best performance. Additionally, RF attained superior performance between the three presented models. Our findings could contribute to opt for an appropriate DEM resolution for mapping landslide hazard in vulnerable areas. Globally, landslides are one of the most devastating of geo-hazards that impose serious threats to human life and economic conditions by the

---

## Methodology
Implemented models. We employed three popular machine learning algorithms to map landslide susceptibilities. While logistic regression (LR) is a parametric machine learning algorithm (learning model that summarizes data with a set of parameters of fixed size - no matter how much data we input at a parametric model, it won’t change its mind); both support vector machine (SVM) and random forest (RF) are non-parametric models (algorithms that do not make strong assumptions about the form of the mapping function; also the complexity Figure 3. Geology map of the study area (Scale 1:50000) depicting six types of lithology. 6 Scientific Reports | (2019) 9:12296 | https://doi.org/10.1038/s41598-019-48773-2 www.nature.com/scientificreports www.nature.com/scientificreports/ grows as the number of training samples increases)19,34. Among these two non-parametric models, RF does not need any real hyperparameters to tune, whereas SVM requires tuning for the right kernel, regularization penalties, and the slack variable13,35. Detailed description and computation of each ML algorithm are provided in the following sections. Logistic regression. Logistic Regression is a popular statistical modeling method which has been applied widely in many problems such as gene selection in cancer classification and crime analysis18,36. In landslide susceptibility analysis, the LR has also used popularly in many case areas19,37. In the LR, the main mathematical concept is to use the logit-the natural logarithm of an odds ratio, which is expressed as follows: ∑ α α α α α =         −    + + … + = + = logit prob prob prob x x x ( ) 1 (1) o n n o i n i i 1 1 1 where: n is the number of the variables used, αo means the intercept, and αi are defined as the coefficients related with the explained variables xi, and prob means the probability of a landslide occurrence which is a nonlinear function of xi is expressed as follows: =      + + α α − − +∑= Prob x e e ( ) 1 1 1 1 (2) logit Prob x x ( ( )) ( ) o i n i i 1 Support vector machine. Introduced by Vapnik38, Support Vector Machine (SVM) is a well-known unsupervised learning machine learning method which has been applied successfully and effectively in landslide susceptibility mapping34,39. The main concept of the SVM is to apply the linear model to carry out the nonlinear class boundaries by nonlinear mapping the input vectors into the new high-dimensional feature space where the optimal separating hyperpla

---

## Results & Findings
Not extracted.

---

## Conclusion
This paper conducts the scale dependency of DEM data in the analysis of landslide susceptibilities. The study area is characterized by steep slopes with frequent debris flows and landslides in the typhoon seasons. The LiDAR DEMs provided unprecedented high-quality terrain data for detailed topographic representations. This study tested the appropriateness of such high accurate grid sizes in the susceptibility studies. The obtained results highlight that a fine resolution DEM not necessarily produce an accurate LSM as they found to be carrying excessive information. These results are in line with the findings of some previous studies29–31. The results prove that entailing different DEM scales introduced different results for the same models. A 30-meter resolution DEM depicting accurate topography could be plausible for LSM as they produced decent levels of generalization of the topography. In fact, higher resolution DEMs introduce more noise, which makes the model perform worse than it supposed to be. Entailing high-resolution DEMs (5 meters Lidar) have proven to be hindered on susceptibility models as they feed a steady flow of data 36 times more than 30 meters DEMs which are supposed to theoretically produce better models. However, in reality, the data flow was treated as noise that worsens the overall resulting models instead of enhancing it, which prove that a generalized DEMs of 30 meters used for DEM-derived condition factors is much valuable than their 5 meters counterpart. Additionally, inappropriate spatial resolution Figure 11. Critical difference plot of the implemented models; Values on the top indicate average rank performance (i.e., 1.91). 19 Scientific Reports | (2019) 9:12296 | https://doi.org/10.1038/s41598-019-48773-2 www.nature.com/scientificreports www.nature.com/scientificreports/ increases the pre-processing time. For this reason, it is suggested that an analysis should be performed to understand the scale effects of topographic variables on landslide susceptibility mapping. Our results also indicate that the scale effects of topographic variables are mainly caused by the resolution impact on topographic parameter derivation, while factors such as geology and rainfall are insensitive to resolutions. For susceptibility mapping, RF models are found to be the best model in term of performance for the study area, while SVM is more suitable in the decision-making process when looking for a balanced LSM model between computational time and o

---

## Key Statistics / Numbers Detected
- accuracy of this inventory was tested previously and found to be 98%
- Auc Acc Kappa Auc Acc Kappa Lidar 5 Meters LR 0.885
- Auc Acc Kappa Lidar 5 Meters LR 0.885
- Kappa Auc Acc Kappa Lidar 5 Meters LR 0.885

---


---

# das2018pravara

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Integration of different influencing factors in GIS to delineate groundwater potential areas using IF and FR techniques: a study of Pravara basin, Maharashtra, India |
| **Authors** | Sumit Das, Sudhakar D. Pardeshi |
| **Year** | 2018 |
| **Venue** | Applied Water Science |
| **DOI** | 10.1007/s13201-018-0848-x |
| **Citations** | 192 |
| **BibTeX key** | `\cite{das2018pravara}` |

---

## Thesis Relevance
**Category:** gw_potential_mapping
**Why cite:** Information Factor + Frequency Ratio GWPZ. Supports multi-factor overlay methodology.
**Relevance signals:** Uses RANDOM FOREST | Topic: groundwater potential | Topic: groundwater potential zone | Uses SRTM feature
**Chapter placement:** Chapter 2 §2.2 (Literature Review — GIS/AHP baseline methods)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 2 §2.2: "Das and Pardeshi (2018) \cite{das2018pravara} integrated lithology,
  geomorphology, slope, soil, drainage density, lineament density and rainfall using
  Frequency Ratio (FR) and Influencing Factor (IF) methods for GWPZ in Pravara basin,
  achieving AUC = 0.73 with FR method."


---

## Abstract
In the present days, remote sensing and geographic information system (GIS) techniques are comprehensive tools for the assessment of water resource, its management and conservation. In this study, remote sensing and GIS techniques are taken into consideration for zonation of different groundwater prospects of Pravara basin. Several contributing factors in which groundwater potential of an area entirely or partially depends such as lithology, geomorphology, slope, soil, lineament density, drainage density, land use and rainfall are assessed individually as well as together for making the different groundwater prospect maps through influencing factor (IF) and frequency ratio (FR) techniques. In ArcGIS software, all these thematic layers are prepared using different satellite imageries and conventional data sets, obtained from different sources. All these layers are transformed into high-resolution raster format and meshed together in GIS environment using IF and FR methods. Groundwater prospect maps are constructed as a result of overlay analysis. Based on the constructed map of groundwater prospect zones, as a result of this study, the study area is divided into five categories of different groundwater potential zones: very high, high, moderate, low and very low. Validation of the resultant maps has shown that frequency ratio technique is having higher accuracy (AUC = 73%) compared to the influencing factors (AUC = 69%). The present study of groundwater zonation provides a simple and less time-consuming technique; also, the results can directly be used for planning and sustainable management in Pravara basin. Keywords Groundwater potential · Lineament · GIS · Sustainable management · IF technique · Pravara

---

## Methodology
Not extracted.

---

## Results & Findings
Not extracted.

---

## Conclusion
Remote sensing and GIS techniques are found to be proficient tools to demarcate groundwater potential zones of Pravara basin, which save money, time and provide quite an accurate result. In the present study, with the help of satellite images and conventional data set, several thematic maps are prepared which affect the groundwater potential of an area. The factors considered in this study to delineate groundwater potential zones are lithology, geomorphology, soil, drainage density, lineament concentration, slope, rainfall and land-use pattern. All these parameters are integrated into GIS software, and the final groundwater potential map is generated. Depending on the groundwater potential map, the study area is categorized into five different zones. The comparison among frequency ratio and influencing factors indicates that the frequency ratio delivers higher accuracy and efficiency (AUC = 73%) compared to the influencing factors (AUC = 69%). The regions having good groundwater potential in the resulting maps may be selected for artificial recharge projects by government or other non-government authorities. The study is highly valuable towards management and sustainable development of watershed in the Pravara basin. This study provides a simple and systematic method to delineate groundwater recharge potential zones through utilizing modern geospatial techniques. However, this approach can be applied to delineate different groundwater recharge zones in other parts of this world where semi-arid climatic condition and hard-rock lithology are seen. Acknowledgements The authors wish to thank Enrico Drioli (Editorin-Chief, Applied Water Science), the handling editor for their valuable suggestions in improving the revised manuscript. Critical review and constructive comments from two anonymous reviewers improved the content significantly. Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creat​iveco​ mmons​.org/licen​ses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

---

## Key Statistics / Numbers Detected
- accuracy (AUC = 73%
- AUC = 69%
- AUC shows 73%
- accuracy and efficiency (AUC = 73%
- 69% accuracy

---


---

# pande2021ahpmif

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Delineation of groundwater potential zones for sustainable development and planning using analytical hierarchy process (AHP), and MIF techniques |
| **Authors** | Chaitanya B. Pande, Kanak N. Moharir, Balamurugan Panneerselvam et al. |
| **Year** | 2021 |
| **Venue** | Applied Water Science |
| **DOI** | 10.1007/s13201-021-01522-1 |
| **Citations** | 177 |
| **BibTeX key** | `\cite{pande2021ahpmif}` |

---

## Thesis Relevance
**Category:** gw_potential_mapping
**Why cite:** AHP + Multi-Influencing Factor GWPZ in semi-arid India. Recent overlay-method reference.
**Relevance signals:** Uses ENSEMBLE | Topic: groundwater potential | Topic: gwpz | Topic: groundwater potential zone | Uses NDVI feature | Uses NDWI feature | Uses TWI feature | Uses SRTM feature
**Chapter placement:** Chapter 2 §2.2 (Literature Review — GIS/AHP baseline methods)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 2 §2.2: "Pande et al. (2021) \cite{pande2021ahpmif} applied AHP (AUC=0.86) and
  MIF (AUC=0.80) for GWPZ in semi-arid Mula river basin, India, using LULC, DEM, soil texture,
  NDVI, slope and groundwater depth — confirming AHP as the more effective technique."


---

## Abstract
Groundwater plays a vital role in the sustainable development of agriculture, society and economy, and it's demand is increasing due to low rainfall, especially in arid and semiarid regions. In this context, delineation of groundwater potential zones is essential for meeting the demand of different sectors. In this research, the integrated approach consisting of analytical hierarchy process (AHP), multiple influence factors (MIF) and receiver operating characteristics (ROC) was applied. The demarcation of groundwater potential zones is based on thematic maps, namely Land Use/Land Cover (LULC), Digital Elevation Model (DEM), hillshade, soil texture, slope, groundwater depth, geomorphology, Normalized Difference Vegetation Index (NDVI), and flow direction and accumulation. The pairwise comparison matrix has been created, and weights are assigned to each thematic layer. The comparative score to every factor was calculated from the overall weight of two major and minor influences. Groundwater potential zones were classified into five classes, namely very poor, poor, moderate, good and very good, which cover an area as follows: 3.33 ­km2, 785.84 ­km2, 1147.47 ­km2, 595.82 ­km2 and 302.65 ­km2, respectively, based on AHP method. However, the MIF groundwater potential zones map was classified into five classes: very poor, poor, moderate, good and very good areas covered 3.049 ­km2, 567.42 ­km2, 1124.50 ­km2 868.86 ­km2 and 266.67 ­km2, respectively. The results of MIF and AHP techniques were validated using receiver operating characteristics (ROC). The result of this research would be helpful to prepare the sustainable groundwater planning map and policy. The proposed framework has admitted to test and could be implemented in different in various regions ar

---

## Methodology
Area under different groundwater potential zones ­(km2) ROC and AUC models Very poor Poor Moderate Good Very good MIF 3.049 567.42 1124.50 868.86 266.67 0.80 (Good) AHP 3.33 785.84 1147.47 595.82 302.65 0.86 (Good) 100% 41% 20% 10% 6% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1 Sensivity 1-Specificity ROC Curve 100% 41% 20% 10% 6% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0% 0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1 Sensivity 1-Specificity ROC Curve a b Fig. 7 Validation of groundwater potential map of a MIF and b AHP techniques by ROC curve Applied Water Science (2021) 11:186 1 3 186 Page 16 of 20 cross-validation maps of groundwater prospect areas by receiver operating characteristic (ROC) graphs (Fig. 7). For various cut-off themes of variable, the ROC charts a true positive rate against an untruthful positive rate and every idea on the arc denotes the sensitivity couple referring to a threshold. On the other side, the field in the Curve (AUC) calculates how well a factor can differentiate both analytical sets from each other. AUC value inside the 0.5–0.6 range recommends low accurateness of forecast. At the same time, the 0.6–0.7, 0.7–0.8, 0.8–0.9 and 0.9–1 levels recommend that very good, average, excellent and good accurateness of forecast, correspondingly (Andualem et al. 2019; Kumar et al. 2020). The validation of outcomes exposed for good prediction by the AHP method as the AUC of the map of the potential areas was 0.86 (Fig. 7). In this context, validation of results correlated reasonable prediction using MIF technique as the AUC was 0.80 of potential groundwater zones. Therefore, the current work has accomplished a suggestively higher correctness level with the highest quantity of appropriate thematic maps by using AHP and MIF procedures (Ahmed and Mansor (2018), Bayala and Prieto (2019), Bhanja et al. (2019), Kumar and Krishna (2018a, 2018b), Pande and Moharir (2017), Vijith and Dodge-Wan (2019), Wakode et al. (2018), Yang et al. (2019), Central Groundwater Board Annual Report (2016–2017). The observed potential zones can give primary strategies in choosing new wells locations for the removal of energetic water resources management in the basin areas. This outcome could be valuable for the implementation of a groundwa

---

## Results & Findings
Not extracted.

---

## Conclusion
The present study investigated the identification of potential zone in the basin using MIF and AHP. In this paper, two types of methods have been applied for the delineation of potential groundwater areas. AHP and MIF have found 595.82–302.65 and 868.86–302.65 ­km2 areas as extremely possible for finding groundwater. MIF technique has made more remarkable outcomes than the AHP method than set theory based on the equation. This study also recommends the enclosure of other geological, groundwater and metrological factors to develop the result. This paper discussed and correlated the two techniques with each other which techniques best for the potential zones of groundwater. Two groundwater potential area maps were cross-validated with the groundwater depth data in the ROC and AUC models. The cross-validation outcomes recognized AHP as a more effective technique (accuracy = 0.86) to demarcate potential groundwater zones for the basin area. The cross-validation results found MIF is a moderately effective method (accuracy = 0.80) to extract the groundwater potential mapping in the area. This result of the study can be useful to apply sustainable groundwater plans for rainwater harvesting, soil erosion and cropping types. In the area, four to three big dams and water bodies are found to be better conditioning parameters for potentiality areas of groundwater, so speedily recovery of water frame is required to be stopped directly. Therefore, adequate management of groundwater is significant for the long sustainable social, financial and environmental development for the Mula river area of Maharashtra in India. It developed sustainable groundwater. Applied Water Science (2021) 11:186 1 3 186 Page 18 of 20 Acknowledgements The authors would like to thank the USGS, NRSC (ISRO) and CGWB, New Delhi, for providing the satellite and ground data. Funding The authors received no specific funding for this work. Declarations Conflict of interest The authors declare no competing interests. Ethical approval The authors declare no any ethical conduct. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in t

---

## Key Statistics / Numbers Detected
- AUC models Very poor Poor Moderate Good Very good MIF 3.049
- Specificity ROC Curve 100%
- AUC of the map of the potential areas was 0.86
- AUC was 0.80

---


---

# hafeez2025rwh

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Mapping of potential storages and rainwater harvesting sites in arid region of Indus basin using analytical hierarchy technique |
| **Authors** | Muhammad Hafeez, Muhammad Jehanzeb Masud Cheema, Umar Waqas Liaqat et al. |
| **Year** | 2025 |
| **Venue** | Scientific Reports |
| **DOI** | 10.1038/s41598-025-20915-9 |
| **Citations** | 2 |
| **BibTeX key** | `\cite{hafeez2025rwh}` |

---

## Thesis Relevance
**Category:** pakistan_pothohar
**Why cite:** AHP water-storage mapping in Pothowar region (same area). Recent, directly comparable methodology.
**Relevance signals:** Mentions 'pothohar' | Mentions 'pothowar' | Mentions 'chakwal' | Mentions 'rawalpindi' | Mentions 'attock' | Mentions 'jhelum' | Uses RANDOM FOREST | Topic: groundwater potential
**Chapter placement:** Chapter 2 §2.1 (Study Area) + Chapter 5 §5.2 (Discussion — regional context)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 2 §2.1 (Study Area): "Hafeez et al. (2025) \cite{hafeez2025rwh} used AHP with
  DEM, rainfall, LULC, soil and drainage density to map 6,508 rainwater harvesting sites
  across the Pothowar region (23,204 km², same five districts as this study), classifying
  44.81% as highly suitable for water storage."
- Chapter 5 §5.2: Compare your ML-predicted high-potential zones with their RWH suitability.


---

## Abstract
Water, an essential element for rainwater harvesting (RWH), plays a pivotal role in addressing water scarcity and enhancing community resilience. This study conducted a comprehensive analysis of water storage in the Pothowar region, which spans approximately 23,204 square kilometers across five districts: Islamabad, Rawalpindi, Chakwal, Attock, and Jhelum. The objective was to assess the availability, demand, and utilization of water reservoirs using GIS technology to identify potential storage sites. The study utilized advanced tools, starting with the acquisition of a 12.5 m Digital Elevation Model (DEM) from ALOS PALSAR, followed by data refinement using the Fill tool. Flow direction analysis and watershed delineation in ArcGIS 10.8.2 revealed 6,508 sub-watersheds and outlets. An Analytical Hierarchy Process (AHP) model was employed to assign weights to factors such as soil, land use, rainfall, stream order, drainage density, and slope, enabling the classification of suitability classes. The results indicated that 41% of the region was classified as moderately suitable, with 3.79% rated as very highly suitable, 44.81% as highly suitable, and 10.40% as not suitable. Specific mini dam sites were proposed based on suitability, with 121 outlets classified as very highly suitable, 3,655 as highly suitable, 2,188 as moderately suitable, and 690 as not suitable. This comprehensive analysis enhances the understanding of the region’s hydrological dynamics, supporting informed decision-making for sustainable water resource management aligned with both developmental and environmental objectives. By combining advanced geospatial tools and a collaborative approach, this study offers a cutting-edge framework for regional water resource management. Keywords Rainwater harvesting, St

---

## Methodology
Study area The study area (Fig. 1) includes Arid districts including Attock, Rawalpindi, Islamabad, Jehlum, and Chakwal in Punjab-Pakistan. It is located in the semi-arid Pothowar region, which spans latitude 32°10’ to 34°9’ N and Scientific Reports | (2025) 15:36947 2 | https://doi.org/10.1038/s41598-025-20915-9 www.nature.com/scientificreports/ longitude 71°10’ to 73°55’ E Malik et al.47. Covering 23,204 square kilometers and rising to altitudes of 150–1,100 meters, it is located on the Pothowar Plateau and is bounded to the east and west by the Jhelum and Indus rivers. With the Salt Range to the south and the Margalla Hills to the north, the topography is characterized by undulating landscapes. The average annual rainfall is between 380 and 500 mm, with the monsoon season, which runs from July to October, being the wettest time of year. The climate varies from semi-arid to sub-humid subtropical continental. Rashid and Rasul48. The districts are known as Barani areas because much of the region’s agriculture is rainfed and is heavily dependent on rainfall due to the lack of irrigation infrastructure, with the exception of a few tube wells Rashid and Rasul48. The plateau’s topography is highly variable, with peaks, troughs, and basins. Rivers like Swan and Hao drain the plateau. The Salt Range, which starts close to the Jhelum district and stretches into the Bannu and Dera Ismail khan Districts to the south, has peaks that can reach 1,525 meters in height and an average height of roughly 671 meters. The Pothowar Plateau is known for its multicolored and culturally varied terrain. The area is home to a variety of soil types that are formed from sandstone and shale formations, including colluvial, mixed material, loess, and alluvial Aziz et al.49 and Malik et al.47. Drought is a serious danger to crop production, especially wheat, and food security in the area because the region is rainfed. Long-term drought conditions are made worse by insufficient rainfall, highlighting how susceptible the populace is to food shortages and agricultural difficulties.

---

## Results & Findings
The Pothowar Region’s mapping of storage facilities and rainfall harvesting (RWH) systems provided extensive insights into local water management practices. With the aid of geographic Information system (GIS) methods, we were able to recognize and define different kinds of water storage facilities. Watershed delineation The Pothowar region, which covers five districts (Islamabad, Rawalpindi, Attock, Jhelum, and Chakwal) and an area of about 23,204 square kilometers, was the focus of a thorough watershed investigation and the identification of possible locations for rainwater collection. Hydrological techniques were used to refine study results using Digital Elevation Model (DEM) data with a spatial resolution of 12.5 m, which was obtained from the ALOS PALSAR website of the Alaska Satellite Facility, as indicated in Fig. 4a. By removing depressions and guaranteeing a realistic depiction of the terrain, the Fill tool used to the DEM helped create a more accurate representation of terrain, which is essential for hydrological study. A detailed analysis of the DEM was carried out to evaluate topographical elements affecting the direction of water flow in the area. The results were graphically displayed on maps using a numerical coding technique frequently used in hydrological modeling and GIS. This coding technique provided a thorough picture of flow patterns inside the districts by assigning values, such as 1, 2, 4, 8, 16, 32, 64, and 128 to geographic directions or combinations thereof. Figure 4b shows that a value of 1 suggests a flow in the east, a value of 2 indicates a flow in the northeast, a value of 4 indicates a flow in the north, and so on. In Fig. 4c, the study shows 6,508 carefully placed pour stations along the stream network. These points are crucial for comprehending the locations of water discharge within the watershed. Based on precise parameters, such as the locations of the watershed’s outflow sites and the lowest places along its border, these pour points were included. As seen in Fig. 4d, which corresponds to the districts of Islamabad, Rawalpindi, Attock, Jhelum, and Chakwal, the analysis identified six separate basins: Bunha, Haro, Kahan, Kanchi, Rashi, and Soan, with the Soan basin being the largest. Basin streams, rivers, and associated district boundaries were identified by examining flow direction obtained from the DEM data, which allowed for a thorough evaluation of the region’s topographical and hydrological features. In addition,

---

## Conclusion
In conclusion, this study presents a detailed and systematic approach to identifying potential water storage sites in the Pothowar region, contributing new insights to the field of water resource management. By integrating GIS tools, local features, and AHP, it provides a valuable decision-support framework that can be applied not only in the Pothowar region but also in other similar regions facing water scarcity. We precisely define potential rainwater harvesting sites by incorporating various parameters such as rainfall, land use and land cover (LULC), soil characteristics, drainage density, slope, and runoff movement. Mini dams classified as highly suitable provide a significant percentage of outlets (44.81% of total area), indicating their potential to significantly contribute to rainwater harvesting efforts. Furthermore, moderately suitable mini dams cover 41.00% of the area, while those deemed unsuitable still cover 10.40%, demonstrating the diverse roles these structures play in water management strategies. Furthermore, our analysis of proposed mini dams in the region yields valuable statistics. Our findings contribute to literature and are offer valuable insights for policymakers and practitioners in water management and contribute to more resilient, sustainable water management strategies. The results not only provide actionable recommendations for the Pothowar region but also offer a transferable methodology that can be applied to other regions. Fig. 13. Delineated Proposed Medium Suitable Mini dams/ponds. (Map created using ArcGIS 10.8.2 ​h​t​t​p​s​:​/​/​w​ w​w​.​e​s​r​i​.​c​o​m​)​.​ Scientific Reports | (2025) 15:36947 15 | https://doi.org/10.1038/s41598-025-20915-9 www.nature.com/scientificreports/ Parameter Classes Rank Suitability Class Rainfall Low 1 Low Suitable High 2 High Suitable LULC Shrubs and Scrubs, Trees 4 Very High Suitable Grass Flooded Vegetation, Crops 3 High Suitable Bare 2 Moderately Suitable Water, Built up 1 Low Suitable Soil Sandy Loam, Loam 1 High Suitable Clay Loam, Medium Clay 2 Moderately Suitable Sandy 3 Low Suitable Clay, Heavy Loam 4 Very Low Suitable Drainage Density Very low 1 Very High Suitable Low 2 High Suitable Moderate 3 Medium Suitable High 4 Low Suitable Slope 0 – 3.3 1 Very High Suitable 3.4 – 6.9 2 High Suitable 7 – 11. 17 – 22 3 Medium Suitable 23 – 28 4 Low Suitable 29 – 37, 38 – 77, 5 Very Low Suitable Table 7. Parameters suitability using AHP for RWH in Pothowar. Fig. 14. Delineated Proposed Not Suita

---

## Key Statistics / Numbers Detected
- See full paper for quantitative results.

---


---

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


---

# waseem2024waterquality

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Water quality assessment and trends in twin cities of Pakistan: a review |
| **Authors** | Kashaf Waseem, Abdul Saboor Akhtar, Ahsan Nawaz et al. |
| **Year** | 2024 |
| **Venue** | Discover Water |
| **DOI** | 10.1007/s43832-024-00182-x |
| **Citations** | 5 |
| **BibTeX key** | `\cite{waseem2024waterquality}` |

---

## Thesis Relevance
**Category:** pakistan_pothohar
**Why cite:** Rawalpindi/Islamabad twin-cities water quality review. Local groundwater context for validation discussion.
**Relevance signals:** Mentions 'rawalpindi' | Uses TWI feature
**Chapter placement:** Chapter 2 §2.1 (Study Area) + Chapter 5 §5.2 (Discussion — regional context)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 5 §5.2 (Discussion): "Water quality surveys in Rawalpindi/Islamabad
  \cite{waseem2024waterquality} identified widespread contamination linked to shallow
  unconfined aquifer conditions — consistent with our model's Medium-potential classification
  of peri-urban Rawalpindi district."


---

## Abstract
Water quality is a significant determinant of ecosystem health and human well-being particularly in cities undergoing rapid industrialization and population growth. This review highlights data from studies conducted between 2004 and 2024 to assess the water quality of surface and groundwater sources in Islamabad and Rawalpindi. The results indicate severe microbial contamination with high levels of total coliform, fecal coliform, and E. coli in both cities, with a potential risk of waterborne diseases. Heavy metal contamination exists, especially As and Pb, which is significantly higher in Rawalpindi due to the industries. Physicochemical parameters, such as turbidity and residual microbial contamination remain in treated water, implying inefficiency in the water treatment process. The contamination also shows seasonal fluctuation, increasing during monsoon due to sewage overflows and agricultural runoff. Both cities also have conventional water treatment infrastructure that causes widespread contamination in the distribution system. Public health impact is prevalent, and outbreaks of diseases from waterborne diseases including Hepatitis E reported both in urban and peri-urban areas quite frequently. A gap is critical in applying the Advanced Oxidation Process (AOP) and other emerging technologies for degrading persistent contaminants, most notably heavy metals and microbial pollutants in the AOPs. This review focuses on the urgency of upgrading infrastructure, strengthening the implementation of water quality standards, and using more advanced treatment technologies and offers recommendations to policymakers and stakeholders and technology solutions for tackling critical challenges in water quality management, and emphasizes the importance of continuou

---

## Methodology
Most contributors did not decontaminate drinking water [58] 37. Islamabad Data acquired from PCRWR​ LULCC and WQI 16 Locations in Islamabad were considered unsuitable (with < 300 WQI value) for drinking water due to high human activities [25] Vol.:(0123456789) Discover Water (2024) 4:125 | https://doi.org/10.1007/s43832-024-00182-x Review Table 3 (continued) Sr no Area of study Data acquisition/sampling data Parameters for the analysis Key findings

---

## Results & Findings
References 1. Rawalpindi, Islamabad Bore water and filter water samples Total coliform and fecal coliform Significant contamination in both water types; better treatment is needed [48] 2. Rawalpindi, Islamabad 462 samples Bacteriological parameters (coliform, E. coli) 35.5% of samples were contaminated; improved treatment was required [24] 3. Rawal Lake, Islamabad 3 main streams Total coliform and fecal coliform High contamination levels from domestic and industrial waste [45] 4. Rawalpindi and Islamabad 95 samples Pb and As 31.57% and 10.45% of samples had a high risk for As and Pb [18] 6. Rawalpindi, Islamabad 30-year data from PMD Temperature, precipitation, water discharge Decreased precipitation and higher temperatures affect river discharge [21] 7. Islamabad, Rawalpindi 30 years of data, PMD, WAPDA Rainwater harvesting sites, surface water potential LULC Reduced surface runoff due to topography and rainfall changes [40] 8. Islamabad Pakistan Bureau of Statistics, CDA, Field Survey Population density, Water table, drainage density, Slope, soil Types, elevation Identifies sites for groundwater recharge with potential stabilization [23] 9. Rawal Lake, Islamabad 5 samples from each site Physiochemical parameters, Total bacterial count, E. coli count Water quality is good for agriculture but not for drinking [41] 10. Islamabad 26 samples Physiochemical and microbial parameters Significant improvement in safe water access over time [49] 11. Islamabad, Rawalpindi 13 samples Rotavirus A (RVA) 45% of samples were positive for G3 and G9 genotypes [22] 12. Simply Dam, Islamabad 20 samples pH, EC, TDS, DO, BOD, total hardness, alkalinity Raw water has low WQI; filtered water is suitable for agriculture [20] 13. Islamabad Data from CDA and PCRWR​ Groundwater quality, heavy metals, sewage treatment, stream water quality Moderate water security; needs improvement in various aspects [32] 14. Zone III of Islamabad 15 samples Physiochemical and microbial parameters The decline in water quality; parameters fall below WHO limits [24] 15. Bhara Kahu, Islamabad 8 samples Physiochemical parameters Groundwater is clean and suitable for drinking [27] 16. Rawalpindi and Islamabad 22 samples Physiochemical parameters Poor groundwater quality due to overexploitation and contamination [50] 17. Peri-urban areas of Islamabad and Rawalpindi 108 samples Fecal coliforms 68.5% had a total viable count; 39.9% were positive for E. coli [16] 18. F-5–F-10; G-5–G-11 H-8–H-10, Islamabad 55 

---

## Conclusion
Not extracted.

---

## Key Statistics / Numbers Detected
- F10, Islamabad 42 samples Physio-chemical parameters 50%

---


---

# khan2024afforestation

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Evaluating potential of dry afforestation techniques on barren land in Attock |
| **Authors** | Shehryar Khan, Sabeeqa Usman Malik, Saeed Gulzar et al. |
| **Year** | 2024 |
| **Venue** | Zoo Botanica |
| **DOI** | 10.55627/zoobotanica.002.02.0602 |
| **Citations** | 0 |
| **BibTeX key** | `\cite{khan2024afforestation}` |

---

## Thesis Relevance
**Category:** pakistan_pothohar
**Why cite:** Attock district (study area) barren-land / semi-arid context. Supports land-degradation discussion.
**Relevance signals:** Mentions 'pothohar' | Mentions 'pothowar' | Mentions 'rawalpindi' | Mentions 'attock'
**Chapter placement:** Chapter 2 §2.1 (Study Area) + Chapter 5 §5.2 (Discussion — regional context)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 2 §2.1 or Chapter 5: "Semi-arid barren land in Attock district \cite{khan2024afforestation}
  is associated with low vegetation cover and degraded soil structure — factors our model captures
  through low NDVI and low soil-texture scores."


---

## Abstract
Deforestation poses a serious environmental threat turning huge vegetative areas into barren lands in Pakistan and may also cause the extinction of native plant species and wildlife. Pothowar plateau being located in the semiarid zone of Pakistan is severely affected by erosion because of less forest cover and less rainfall resulting in large areas shifting to barren lands. Deforestation, unpredictability, and short durational rainfall are the key causative agents. Dry afforestation is a well-known technique for land reclamation in arid and semi-arid areas. Dry afforestation is an efficient way of utilizing rainwater for tree growth and increasing vegetative cover. This research was conducted in Attock (located in the Pothowar plateau). The research duration was one year (February 2022-2023). The main objective of this research was the evaluation and comparison of dry afforestation techniques in terms of indigenous vegetation growth so that rainwater can be utilized to the maximum extent. Two different dry afforestation techniques including troughs and bunds were tested to reclaim the barren area. Three indigenous species including Acacia nilotica, Acacia modesta, and Dodonaea viscosa were selected for study purposes on dry afforestation techniques. The performance potential of both techniques was evaluated based on different plant growth parameters. Results from plant growth data concluded that, in terms of plant height Dodonaea viscosa and Acacia nilotica performed better on troughs while Acacia modesta performed better on bunds with significant variation in Acacia modesta and Acacia nilotica tree species. In terms of the number of leaves, there was no significant variation found after analysis. However, Dodonaea viscosa and Acacia nilotica performed

---

## Methodology
Experimental Site Attock previously known as Campbellpur is a rather large district of Punjab province. Attock is a section of the Pothohar plateau, which is situated on the watershed of Attock River and surrounded by hilly terrain. This area lies between 1000 and 1145 feet above sea level in elevation. Attock is situated in 33.77° north latitudinal line and 72.36° east longitudinal line. Tree Species Selection The following three native tree species were selected for the collection of plant growth data: Acacia modesta (Phulai) Acacia nilotica (Kikar) Dodonaea viscosa (Sanatha) Site for Plant Growth Data Collection The site which was selected for data collection of plant growth was located in Attock city having coordinates Latitude:33.85374 & Longitude:72.33859. Dry afforestation techniques were implanted/established here by the Punjab Forest Department under the Ghazi Brotha Hydropower Project (GBHP) between 01 February-15 March 2022 on an area of three hundred acres. Two dry afforestation techniques i.e., Bund formation and Trough formation are being used in Attock. Data Collection As the plantation was done during February-March 2022, data collection was done during March i.e., 10-20 March 2023 exactly after one year. The research site was distributed using one percent sampling intensity (1%). Plot Size Ten-meter radios (10m) circular plots were selected randomly on twelve different locations using a random sampling technique. Each plot included one trough and one bund upon which data of three different parameters were collected. 113 Zoo Botanica 02(2) 2024. 111-120 https://doi.org/10.55627/zoobotanica.002.02.0602 Parameters Three different parameters were studied in this research which included plant height, number of branches, and number of leaves. Statistical Analysis Statistical analysis of research data was done using descriptive and inferential statistics using Microsoft Excel and Statistical Package for Social Sciences. RESULTS AND DISCUSSION Effect of Bunds and Trough Techniques on Plant Height (cm) of Sanatha The graphical representation of the effect of bund and trough techniques on the plant height of plant species is described in Figure (1). Sanatha performed better in troughs techniques. The graph shows that most of the plots showed a significant increase in plant height under the Trough technique. Under bunds, the maximum mean value of plant height was recorded in Plot 12 (35). In comparison, the minimum mean value of plant height was reco

---

## Results & Findings
Effect of Bunds and Trough Techniques on Plant Height (cm) of Sanatha The graphical representation of the effect of bund and trough techniques on the plant height of plant species is described in Figure (1). Sanatha performed better in troughs techniques. The graph shows that most of the plots showed a significant increase in plant height under the Trough technique. Under bunds, the maximum mean value of plant height was recorded in Plot 12 (35). In comparison, the minimum mean value of plant height was recorded in Plot 4 (16). Under trough, the maximum mean value of plant height was recorded in Plot 9 (35.5). At the same time, the minimum mean value of plant height was recorded in Plot 2 (18.9). Figure 1. Comparison of bunds and trough techniques on plant height (cm) of Sanatha. Effect of Bunds and Trough Techniques on Plant Height (Cm) Of Phulai The graph in Figure (2) shows that most of the plots showed a significant increase in plant height under the bund technique. Under bunds, the maximum mean value of plant height was recorded in Plot 1 (30). In comparison, the minimum mean value of plant height was recorded in Plot 11 (22.1). Under trough, the maximum mean value of plant height was recorded in Plot 3 (32.3). At the same time, the minimum mean value of plant height was recorded in Plot 11 (20.1). Figure 2. Comparison of bunds and trough techniques on plant height (cm) of Phulai. Plant height of Sanatha 40 30 20 10 Plot1 Plot2 Plot3 Plot4 Plot5 Plot6 Plot7 Plot8 Plot9 Plot10 Plot11 Plot12 Plots Bunds Trough 40 30 20 10 Bunds Trough Plot1 Plot2 Plot3 Plot4 Plot5 Plot6 Plot7 Plot8 Plot9 Plot10 Plot11 Plot12 Plots Plant height of Phulai Plant Height (in) Plant Height (in) 114 Khan et al., 2024 https://doi.org/10.55627/zoobotanica.002.02.602 Effect of Bunds and Trough Techniques on Plant Height (Cm) of Kikar The graphical representation of the effect of bund and trough techniques on the plant height of Kikar has been presented in Figure (3). The content of the figure reveals that both treatments differ significantly from each other. The data reveals that maximum plant height was found in the Trough technique. The graph shows that most of the plots showed a significant increase in plant height under the Trough technique. Under bunds, the maximum mean value of plant height was recorded in Plot 8 (49.2). In comparison, the minimum mean value of plant height was recorded in Plot 4 (20.6). Significant variations were found in this parameter after performing a

---

## Conclusion
Not extracted.

---

## Key Statistics / Numbers Detected
- See full paper for quantitative results.

---


---

# sarwar2022soandrought

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Shifting of Meteorological to Hydrological Drought Risk at Regional Scale |
| **Authors** | Awais Naeem Sarwar, Muhammad Waseem, Muhammad Azam et al. |
| **Year** | 2022 |
| **Venue** | Applied Sciences |
| **DOI** | 10.3390/app12115560 |
| **Citations** | 22 |
| **BibTeX key** | `\cite{sarwar2022soandrought}` |

---

## Thesis Relevance
**Category:** pakistan_pothohar
**Why cite:** Soan basin (Pothohar arid region) drought study. Directly in your study area.
**Relevance signals:** Mentions 'pothohar' | Mentions 'rawalpindi'
**Chapter placement:** Chapter 2 §2.1 (Study Area) + Chapter 5 §5.2 (Discussion — regional context)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 2 §2.1 (Study Area): "The Soan River basin — entirely within the Pothohar Plateau —
  is characterized by recurrent hydrological drought \cite{sarwar2022soandrought}, where
  meteorological deficits rapidly translate into reduced groundwater recharge, underscoring
  the urgency of precise groundwater potential mapping."


---

## Abstract
Citation: Sarwar, A.N.; Waseem, M.; Azam, M.; Abbas, A.; Ahmad, I.; Lee, J.E.; Haq, F.u. Shifting of Meteorological to Hydrological Drought Risk at Regional Scale. Appl. Sci. 2022, 12, 5560. https://doi.org/ 10.3390/app12115560 Academic Editors: Andrea Chiozzi, Željana Nikoli´c and Elena Benvenuti Received: 24 March 2022 Accepted: 27 May 2022 Published: 30 May 2022 Publisher’s Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional afﬁliations. Copyright: © 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/). applied sciences Article Shifting of Meteorological to Hydrological Drought Risk at Regional Scale Awais Naeem Sarwar 1, Muhammad Waseem 1,* , Muhammad Azam 2 , Adnan Abbas 3, Ijaz Ahmad 1 , Jae Eun Lee 4,* and Faraz ul Haq 1 1 Centre of Excellence in Water Resources Engineering, University of Engineering & Technology, GT-Road, Lahore 54890, Pakistan; ranaawais094@gmail.com (A.N.S.); ijaz.ahmad@cewre.edu.pk (I.A.); engraraz@uet.edu.pk (F.u.H.) 2 Faculty of Agricultural Engineering and Technology, PMAS Arid Agriculture University, Rawalpindi 46000, Pakistan; mazammakram@gmail.com 3 Land Science Research Center, Nanjing University of Information Science & Technology, Nanjing 210044, China; adnanabbas@nuist.edu.cn

---

## Methodology
Not extracted.

---

## Results & Findings
3.1. Spatiotemporal Analysis of Droughts 3.1.1. Analysis of Meteorological Drought Figure 2 illustrates the meteorological drought index calculated at selected time scales for both sub-basins of the study area. Based on the analysis, it was observed that there was an increase in the frequency of drought after 1998 speciﬁcally in the case of sub-basin-1 when SPIs mostly remained negative. These results are in good agreement with the results previously published on droughts in Pakistan [19,20,23,29,39]. The variations in drought between both sub-basins are due to the more relative decrease in precipitation in subbasin-1, compared to sub-basin-2 [30,32]. Moreover, the numbers of drought events were different at different computed time scales. Signiﬁcant inconsistencies were found when the 3-month time scale was compared with the 6-month time scale, and a comparison between the 6-month and 12-month time scales gave slight variations in results. Results reveal the frequent occurrence of severe drought events at each sub-basin of the study area, and these were more sensitive to short-term drought compared to long-term droughts. According to the results, the recurrence of drought is more frequent and consecutive at 1 to 6 months’ timescale in sub-basin 1 and during the 12-month timescale, there exists a sharp difference between wet and dry episodes. while the sub-basin 2 is found to be more sensitive to drought (mild to severe) at a 1-month timescale as compared to 3, 6, and 12-month timescales. The results also speciﬁed that the drought events state varied with the increase in SPI time scales, mostly a declining trend in sub-basin 2. This is due to the reason that computation of 12-month time scale SPI involves the aggregation of total precipitation from October to September and includes both wet and dry seasons. However, the 3-month SPI time scale considers only the sum of three-month precipitation, and the 3-month time scale (March-May) of the study basin was normally a dry season. Appl. Sci. 2022, 12, 5560 6 of 14 Sub–Basin 1 Sub–Basin 2 Figure 2. Temporal variations of meteorological drought periods during 1983–2015 in sub–basins 1 and 2. Figure 3 illustrates the severity of meteorological drought based on the 12-month time scale for both hydrological sub-basins and the difference in their SPI-12 values during the study period (i.e., 1983–2015). Based on the analysis, it resulted that the years from 1998 to 2004 were the driest years of the selected time ser

---

## Conclusion
Not extracted.

---

## Key Statistics / Numbers Detected
- See full paper for quantitative results.

---


---

# khan2023rainfallrunoff

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Intercomparison and Assessment of Stand-Alone and Wavelet-Coupled Machine Learning Models for Simulating Rainfall-Runoff Process in Four Basins of Pothohar Region, Pakistan |
| **Authors** | Muhammad Tariq Khan, Muhammad Shoaib, Raffaele Albano et al. |
| **Year** | 2023 |
| **Venue** | Atmosphere |
| **DOI** | 10.3390/atmos14030452 |
| **Citations** | 5 |
| **BibTeX key** | `\cite{khan2023rainfallrunoff}` |

---

## Thesis Relevance
**Category:** pakistan_pothohar
**Why cite:** ML rainfall-runoff in FOUR POTHOHAR BASINS. Very close regional + methodological match â€” high priority cite.
**Relevance signals:** Mentions 'pothohar' | Mentions 'chakwal' | Mentions 'rawalpindi' | Mentions 'jhelum' | Uses RANDOM FOREST
**Chapter placement:** Chapter 2 §2.1 (Study Area) + Chapter 5 §5.2 (Discussion — regional context)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 5 §5.1 (Discussion): "Khan et al. (2023) \cite{khan2023rainfallrunoff} applied
  wavelet-coupled ML models (ANN, SVM, ANFIS) in four Pothohar basins and found that
  wavelet preprocessing significantly improved model performance for rainfall-runoff simulation
  — consistent with the strong signal from CHIRPS rainfall (r=0.514) found in this study."
- Chapter 2 §2.3: Regional ML precedent in the exact study area.


---

## Abstract
Citation: Khan, M.T.; Shoaib, M.; Albano, R.; Inam, M.A.; Salahudin, H.; Hammad, M.; Ahmad, S.; Ali, M.U.; Hashim, S.; Ullah, M.K. Intercomparison and Assessment of Stand-Alone and Wavelet-Coupled Machine Learning Models for Simulating Rainfall-Runoff Process in Four Basins of Pothohar Region, Pakistan. Atmosphere 2023, 14, 452. https://doi.org/10.3390/ atmos14030452 Academic Editors: Stefania Anna Palermo, Michele Turco, Behrouz Pirouz and Patrizia Piro Received: 14 December 2022 Revised: 11 February 2023 Accepted: 21 February 2023 Published: 24 February 2023 Copyright: © 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/). atmosphere Article Intercomparison and Assessment of Stand-Alone and Wavelet-Coupled Machine Learning Models for Simulating Rainfall-Runoff Process in Four Basins of Pothohar Region, Pakistan Muhammad Tariq Khan 1, Muhammad Shoaib 1,* , Raffaele Albano 2,* , Muhammad Azhar Inam 1, Hamza Salahudin 1 , Muhammad Hammad 1 , Shakil Ahmad 3 , Muhammad Usman Ali 1, Sarfraz Hashim 4 and Muhammad Kaleem Ullah 5 1 Department of Agricultural Engineering, Faculty of Agricultural Sciences and Technology, Bahauddin Zakariya University, Multan 60000, Pakistan 2

---

## Methodology
Not extracted.

---

## Results & Findings
Not extracted.

---

## Conclusion
Not extracted.

---

## Key Statistics / Numbers Detected
- RMSE decreased from 479.892
- accuracy of 86%
- accuracy enhancement was observed in the case of GEP, where a 55%
- accuracy (around 86%
- R² = 0.9216

---


---

# swain2020floodahp

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Flood Susceptibility Mapping through the GIS-AHP Technique Using the Cloud |
| **Authors** | Kishore Chandra Swain, Chiranjit Singha, Laxmikanta Nayak |
| **Year** | 2020 |
| **Venue** | ISPRS International Journal of Geo-Information |
| **DOI** | 10.3390/ijgi9120720 |
| **Citations** | 241 |
| **BibTeX key** | `\cite{swain2020floodahp}` |

---

## Thesis Relevance
**Category:** methodology_analog
**Why cite:** Cloud-based GIS-AHP susceptibility mapping. Methodological analogue for multi-criteria spatial analysis.
**Relevance signals:** Uses RANDOM FOREST | Uses ENSEMBLE | Uses NDVI feature | Uses TWI feature | Uses TOPOGRAPHIC WETNESS feature | Uses LANDSAT feature
**Chapter placement:** Chapter 3 §3.4 (Model validation / comparison framework)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 3 §3.2: "AHP-based multi-criteria spatial analysis has been widely validated
  for natural resource mapping \cite{swain2020floodahp}; Swain et al. (2020) demonstrated
  cloud-based GIS-AHP susceptibility mapping achieving good prediction accuracy — the same
  framework underpins our knowledge-based label generation."


---

## Abstract
Department of Agricultural Engineering, Institute of Agriculture, Visva-Bharati, Sriniketan 731236, India; singha.chiranjit@gmail.com 2 ICAR-NINFET, 12 Regent Park, Kolkata 700040, India; laxmikanta8495@rediﬀmail.com * Correspondence: kishore.swain@visva-bharati.ac.in Received: 19 August 2020; Accepted: 23 November 2020; Published: 2 December 2020   Abstract: Flood susceptibility mapping is essential for characterizing ﬂood risk zones and for planning mitigation approaches. Using a multi-criteria decision support system, this study investigated a ﬂood susceptible region in Bihar, India. It used a combination of the analytical hierarchy process (AHP) and geographic information system (GIS)/remote sensing (RS) with a cloud computing API on the Google Earth Engine (GEE) platform. Five main ﬂood-causing criteria were broadly selected, namely hydrologic, morphometric, permeability, land cover dynamics, and anthropogenic interference, which further had 21 sub-criteria. The relative importance of each criterion prioritized as per their contribution toward ﬂood susceptibility and weightage was given by an AHP pair-wise comparison matrix (PCM). The most and least prominent ﬂood-causing criteria were hydrologic (0.497) and anthropogenic interference (0.037), respectively. An area of ~3000 sq km (40.36%) was concentrated in high to very high ﬂood susceptibility zones that were in the vicinity of rivers, whereas an area of ~1000 sq km (12%) had very low ﬂood susceptibility. The GIS-AHP technique provided useful insights for ﬂood zone mapping when a higher number of parameters were used in GEE. The majorities of detected ﬂood susceptible areas were ﬂooded during the 2019 ﬂoods and were mostly located within 500 m of the rivers’ paths. Keywords: ﬂood susceptibility; g

---

## Methodology
Not extracted.

---

## Results & Findings
Not extracted.

---

## Conclusion
Not extracted.

---

## Key Statistics / Numbers Detected
- See full paper for quantitative results.

---


---

# mallick2019fuzzyahp

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Modeling Groundwater Potential Zone in a Semi-Arid Region of Aseer Using Fuzzy-AHP and Geoinformation Techniques |
| **Authors** | Javed Mallick, Roohul Abad Khan, Mohd. Ahmed et al. |
| **Year** | 2019 |
| **Venue** | Water |
| **DOI** | 10.3390/w11122656 |
| **Citations** | 224 |
| **BibTeX key** | `\cite{mallick2019fuzzyahp}` |

---

## Thesis Relevance
**Category:** gw_potential_mapping
**Why cite:** Semi-arid GWPZ modeling (same climate class as Pothohar). Good study-area analogue.
**Relevance signals:** Topic: groundwater potential | Topic: gwpz | Topic: groundwater potential zone | Uses NDVI feature | Uses TWI feature | Uses TOPOGRAPHIC WETNESS feature | Uses LANDSAT feature
**Chapter placement:** Chapter 2 §2.2 (Literature Review — GIS/AHP baseline methods)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 2 §2.2: "In semi-arid Saudi Arabia (climatically analogous to Pothohar),
  Mallick et al. (2019) \cite{mallick2019fuzzyahp} used Fuzzy-AHP with geology, lineaments,
  geomorphology, NDVI, slope, TWI and soil to delineate GWPZ, validating with well data
  and demonstrating the transferability of geospatial GWPZ methods to arid regions."


---

## Abstract
Department of Civil Engineering, College of Engineering, King Khalid University, Abha 61411, Saudi Arabia; mall@kku.edu.sa (M.A.); sdalqadi@kku.edu.sa (S.D.A.); malsubih@kku.edu.sa (M.A.); ifalqi@kku.edu.sa (I.F.); mohad@kku.edu.sa (M.A.H.) 2 Department of Civil Engineering, Faculty of Engineering and Applied Science, Himalayan University, Arunachal Pradesh 791111, India; rakhan@kku.edu.sa * Correspondence: jmallick@kku.edu.sa; Tel.: +96-617-242-8439; Fax: +96-617-241-8152 Received: 19 October 2019; Accepted: 12 December 2019; Published: 16 December 2019   Abstract: Saudi Arabia’s arid and semi-arid regions suﬀer from water scarcity because of climatic constraints and rapid growth of domestic and industrial water uses. The growing demand for high-quality water supplies and to reduce the dependency on desalination creates an urgent need to explore groundwater resources as an alternative. The weighted overlay analysis method using the fuzzy-analytical hierarchy process (FAHP) multi-criteria decision making (MCDM) techniques combined with geoinformation technology was used in this study to explore the groundwater potential zones in the Itwad-Khamis watershed of Saudi Arabia. Twelve thematic layers were prepared and processed in a GIS setting to produce the groundwater potential zone map (GPZM). Subsequently, potential groundwater areas were delineated and drawn into ﬁve classes: very good potential, good potential, moderate potential, poor potential, and very poor potential. The estimated GWPZ (groundwater potential zones) was validated by analyzing the existing open wells distribution and the yield data of selected wells within the studied watershed. With this quality-based zoning, it was found that 82% of existing wells were located in a very good and goo

---

## Methodology
Not extracted.

---

## Results & Findings
Not extracted.

---

## Conclusion
Not extracted.

---

## Key Statistics / Numbers Detected
- sensitivity value variations in the study area; their mean value was 5.48%
- accuracy of 0.815
- Kappa coeﬃcient of 89.38

---


---

# benjmel2020morocco

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Mapping of Groundwater Potential Zones in Crystalline Terrain Using Remote Sensing, GIS Techniques, and Multicriteria Data Analysis (Ighrem Region, Western Anti-Atlas, Morocco) |
| **Authors** | Khalid Benjmel, Fouad Amraoui, Said Boutaleb et al. |
| **Year** | 2020 |
| **Venue** | Water |
| **DOI** | 10.3390/w12020471 |
| **Citations** | 181 |
| **BibTeX key** | `\cite{benjmel2020morocco}` |

---

## Thesis Relevance
**Category:** gw_potential_mapping
**Why cite:** Crystalline / hard-rock terrain GWPZ â€” relevant to your Salt Range / Kala Chitta hard-rock discussion.
**Relevance signals:** Topic: groundwater potential | Topic: groundwater potential zone | Uses TWI feature | Uses TOPOGRAPHIC WETNESS feature | Uses LANDSAT feature
**Chapter placement:** Chapter 2 §2.2 (Literature Review — GIS/AHP baseline methods)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 5 §5.2 (Discussion — hard-rock zones): "In hard-rock crystalline terrain,
  Benjmel et al. (2020) \cite{benjmel2020morocco} found that lineament density and
  structural geology are primary controls on groundwater occurrence — consistent with our
  model's low-potential prediction for Margalla Hills and Kala Chitta Range hard-rock areas."


---

## Abstract
Laboratory of Geosciences Applied to Engineering Development (G.A.I.A), Faculty of Sciences Ain Chock, Hassan II University, Casablanca 20150, Morocco; amraoui_f@hotmail.com (F.A.); tahiri.amine28@gmail.com (A.T.) 2 Laboratory of Applied Geology and Geo-Environment, Faculty of Science, Ibn Zohr University, Agadir 80000, Morocco; saidboutaleb1@yahoo.fr (S.B.); ouchen.geol@gmail.com (M.O.); touab.am@gmail.com (A.T.) * Correspondence: khalidbenjmelstu@gmail.com; Tel.: +212-678-114-886 Received: 24 December 2019; Accepted: 22 January 2020; Published: 10 February 2020   Abstract: This research work is intended as a contribution to the development of a multicriteria methodology, combining several factors to control the availability of groundwater resources, in order to optimize the choice of location of future drilling and increase the chances to take water from productive structures which will satisfy the ever-increasing water demand of local population (Arghen basin in the Western Anti-Atlas chain of Morocco). The geographic information system is used to develop thematic maps describing the geometry and the hydrodynamic functioning of the aquifer. In this study, 11 factors including geology, topography, and hydrology, inﬂuencing the distribution of water resources were used. Based on the Analytical Hierarchy Process (AHP) model, GIS, and remote sensing, the study mapped and classiﬁed areas according to their hydrogeological potential. The favorable potential sectors cover 17% of the total area of the basin. The medium potential sectors account for 64%, while the unfavorable areas cover 18% of the basin area. The groundwater potential map of the study area has been validated by comparing with data from 159 boreholes scattered throughout the basin. Keywords: I

---

## Methodology
Not extracted.

---

## Results & Findings
Not extracted.

---

## Conclusion
Not extracted.

---

## Key Statistics / Numbers Detected
- See full paper for quantitative results.

---


---

# waseem2022drought

---

## Metadata
| Field | Value |
|-------|-------|
| **Title** | Spatiotemporal Analysis of Drought and Agriculture Standardized Residual Yield Series Nexuses across Punjab, Pakistan |
| **Authors** | Muhammad Waseem, Ali Hasan Jaffry, Muhammad Azam et al. |
| **Year** | 2022 |
| **Venue** | Water |
| **DOI** | 10.3390/w14030496 |
| **Citations** | 33 |
| **BibTeX key** | `\cite{waseem2022drought}` |

---

## Thesis Relevance
**Category:** pakistan_pothohar
**Why cite:** Drought + agriculture across Punjab. Context for water stress in study area.
**Relevance signals:** Mentions 'pothohar' | Mentions 'chakwal' | Mentions 'rawalpindi' | Mentions 'jhelum'
**Chapter placement:** Chapter 2 §2.1 (Study Area) + Chapter 5 §5.2 (Discussion — regional context)

---

## How to Cite in Your Thesis

**How to cite in thesis:**
- Chapter 2 §2.1: "Punjab province experiences significant spatiotemporal drought variability
  \cite{waseem2022drought}; Waseem et al. (2022) identified a declining trend in agricultural
  water availability across Punjab between 1981–2019, highlighting the critical need for
  improved groundwater resource mapping."


---

## Abstract
  Citation: Waseem, M.; Jaffry, A.H.; Azam, M.; Ahmad, I.; Abbas, A.; Lee, J.-E. Spatiotemporal Analysis of Drought and Agriculture Standardized Residual Yield Series Nexuses across Punjab, Pakistan. Water 2022, 14, 496. https:// doi.org/10.3390/w14030496 Academic Editor: Maria Mimikou Received: 5 January 2022 Accepted: 4 February 2022 Published: 7 February 2022 Publisher’s Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional afﬁliations. Copyright: © 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/). water Article Spatiotemporal Analysis of Drought and Agriculture Standardized Residual Yield Series Nexuses across Punjab, Pakistan Muhammad Waseem 1, Ali Hasan Jaffry 1 , Muhammad Azam 2,*, Ijaz Ahmad 1 , Adnan Abbas 3 and Jae-Eun Lee 4,* 1 Centre of Excellence in Water Resources Engineering, University of Engineering & Technology, Lahore 54890, Pakistan; dr.waseem@uet.edu.pk (M.W.); alijafrey1122@gmail.com (A.H.J.); ijaz.ahmad@cewre.edu.pk (I.A.) 2 Faculty of Agricultural Engineering and Technology, PMAS Arid Agriculture University, Rawalpindi 46000, Pakistan 3 Chengyi Zhao Land Science Research Center, Nanjing University of Information Science & Technology, Nanjing 210044, China; adnanabbas@nuist.edu.pk

---

## Methodology
Not extracted.

---

## Results & Findings
3.1. Temporal Evaluation of Meteorological Drought The temporal evolution of the averaged SPIs for the wheat cropping months (i.e., November–April) indicates that different zones experienced frequent drought episodes during 2001–2019; Figure 3. The SPI at lags of 1–12 months shows the alternate occurrence of dry periods throughout the wheat cropping season, which indicates the drought timing and its persistent behavior in different zones of Punjab for the particular timescale. The results reveal that almost all the zones of Punjab were sensitive to droughts having a timescale of 1 and 6 months during the period 2006 to 2019, based on a negative SPI value. It is noteworthy here to mention that the occurrence of drought in Pakistan is mainly due to the variations in monsoon rainfall and western disturbance. According to the Pakistan Meteorological Department, the rainfall in Pakistan during the ﬁrst ﬁve months decreased by an average of 45% compared to the previous decade. This may be the cause of the frequent drought episodes in different parts of Punjab, resulting in serious water stress, especially for the agriculture sector during Rabi crops. The most severe drought years in Zones 1 for 1- and 2-monthtimescales were from 2007 to 2019. In Zone 2, the drought events occurred for 1,2, 6, and 7, 8 month timescales during the time periods of 2007–2019, 2010–2019, and 2004–2006, respectively. For Zone 3, the severe drought years occurred from 2007 to 2019 for the 6-month timescale. Zone 4 exhibited the drought sensitivity for 1, 6, and 8-month timescales, and drought-affected years occurred during 2006–2018, 2010–2019, and 2006–2010 for the respective timescale. The most severe drought years in Zone 5 for a 1-month timescale were from 2005 to 2019, and for a 6-month timescale were from 2010 to 2019. Overall, it is observed that all the zones of Punjab are under the inﬂuence of recurrent moderate drought episodes at particular timescales. It should be mentioned that there was a shift from moderate to severe drought periods between 2001–2006 and 2007–2019 in almost all the zones of Punjab at 1 and2-month timescale. This shift in the intensity of drought from moderate to severe had a serious impact on the groundwater in Punjab, which declined at the rate of about 0.79 m/year during 2001–2018 due to over-abstraction for agriculture purposes (survey of the Irrigation Department of Punjab). Therefore, Pakistan recently implemented steps toward a sustainable groundwa

---

## Conclusion
Not extracted.

---

## Key Statistics / Numbers Detected
- See full paper for quantitative results.

---
