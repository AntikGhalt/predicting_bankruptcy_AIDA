# Machine Learning for Italian Enterprise Bankruptcy Prediction

This repository contains the code and analysis for the Master's thesis, "Comparing Machine-Learning Models for Enterprise Bankruptcy Prediction," completed at Sapienza University of Rome.

## Project Overview

This thesis develops and assesses a machine learning framework for one-year-ahead corporate bankruptcy prediction in Italy. Using a comprehensive dataset of financial statements from the Moody's AIDA database, the project tackles the core challenge of **extreme class imbalance**, where bankruptcies represent just **0.127%** of firm-year observations.

The research proceeds in two phases:
1.  **Phase 1:** A comparative study of six different machine learning algorithms on a balanced pilot sample to identify the most promising model architectures.
2.  **Phase 2:** An in-depth analysis using the top-performing models (XGBoost and LightGBM) on the full, unfiltered population of ~190,000 Italian enterprises.

The final, tuned XGBoost model achieves a test ROC-AUC of **0.947** and provides a practical, high-efficiency tool for risk assessment.

## Key Methodological Highlights

* **Extreme Imbalance Handling:** The project's core challenge was the 1-in-800 bankruptcy rate. The final solution involved treating the majority-class down-sampling ratio as a tunable hyperparameter within the optimization search, which ultimately converged on using 100% of the healthy firm data combined with a `scale_pos_weight` of 777.
* **Metric Selection Validation:** A dedicated experiment was conducted to compare four different optimization metrics (ROC-AUC, PR-AUC, Partial PR-AUC, and Precision@90Recall). The results empirically validated that for this dataset, optimizing for **ROC-AUC** produced the most stable and highest-performing models on the unseen test set, weighing in on recent debates in the machine learning literature.
* **Temporal Validation:** A strict chronological split (Training: 2016-2018, Validation: 2019, Test: 2020-2021) was used to ensure the model was always evaluated on data "from the future," providing a realistic estimate of its real-world performance.

## Key Results

* **Final Model Performance:** The tuned **XGBoost** model was the top performer, achieving a **ROC-AUC of 0.947** on the full, imbalanced test set.
* **Practical Efficiency Gain:** At a 90% recall target, the model identifies nine out of ten bankruptcies while requiring investigation of only **11.1%** of healthy firms—an **8-fold efficiency gain** over random selection.
* **Risk Reduction:** The model effectively screens out low-risk companies, reducing the bankruptcy rate among the population of firms predicted as "healthy" by **nine-fold** (from 0.127% to 0.014%).
* **Feature Insights:** While financial ratios were important, geographic coordinates (`latitude` and `longitude`) emerged as top predictors by split count, indicating that local economic patterns are a significant driver of bankruptcy risk in Italy.

## Repository Structure

This repository is organized into two main components, corresponding to the two phases of the thesis.

* `phase1_code/`
    * Contains the code and notebooks for the preliminary analysis on the **balanced pilot sample**.
    * This includes the implementation and comparison of all six machine learning models (Logistic Regression, SVM, Random Forest, Neural Network, XGBoost, LightGBM).
    * The code here includes the hierarchical imputation and feature scaling pipeline that was necessary for this comparative phase.

* `phase2_code/`
    * Contains the code and notebooks for the main analysis on the **full, imbalanced population**.
    * This includes the 700-trial Optuna hyperparameter searches for XGBoost and LightGBM, which simultaneously tuned model parameters and the data sampling ratio.
    * This folder also contains the code for the metric selection experiment and the generation of the final results, feature importances, and visualizations.

## Data Source

The analysis is based on firm-level financial statement data from the **AIDA (Analisi Informatizzata Delle Aziende Italiane) database**, provided by Moody's Analytics. Due to its proprietary nature, the raw data cannot be included in this repository.

## Dataset Splits

The project uses a strict chronological split for all experiments. The datasets created from the source data can be conceptualized as follows:

```
DATA/
├── phase1_balanced_data/
│   ├── training_set.csv      # Years 2016-2018. Balanced 1:1 ratio of bankrupt to healthy firms.
│   ├── validation_set.csv    # Year 2019. Balanced 1:1 ratio.
│   └── test_set.csv          # Years 2020-2021. Balanced 1:1 ratio.
│
└── phase2_full_population/
    ├── training_set.csv      # Years 2016-2018. Full unfiltered population (~497k obs, 0.128% bankrupt).
    ├── validation_set.csv    # Year 2019. Full unfiltered population (~178k obs, 0.138% bankrupt).
    └── test_set.csv          # Years 2020-2021. Full unfiltered population (~367k obs, 0.127% bankrupt).
```

## Dependencies & Setup

The project was implemented in Python 3. The primary libraries used include:
* `pandas` & `numpy` for data manipulation
* `scikit-learn` for preprocessing and baseline models
* `tensorflow` for the neural network
* `xgboost`
* `lightgbm`
* `optuna` for hyperparameter optimization
* `matplotlib` & `seaborn` for plotting

## How to Run

1.  **Obtain Data:** As the source data is proprietary, you will need to acquire access to the AIDA database and extract the variables as described in Chapter 2 of the thesis.
2.  **Phase 1:** Navigate to the `phase1_code/` directory and run the notebooks in sequential order to reproduce the balanced sample analysis.
3.  **Phase 2:** Navigate to the `phase2_code/` directory and run the notebooks to reproduce the full population analysis, optimization, and final results.

## Citation

If you use this work, please cite it as:

Refuto, P. (2025). *Comparing Machine-Learning Models for Enterprise Bankruptcy Prediction* (Master's thesis). Sapienza University of Rome, Rome, Italy.
