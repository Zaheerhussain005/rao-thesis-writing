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
