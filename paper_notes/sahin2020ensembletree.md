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
