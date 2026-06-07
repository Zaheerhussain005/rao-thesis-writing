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
