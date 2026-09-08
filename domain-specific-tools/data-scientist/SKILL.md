---
name: data-scientist
description: Guides the AI to perform professional data analysis, machine learning, and data visualization using Python. Use when the user provides data files, asks for insights from a dataset, or needs a machine learning model built.
---

When performing data analysis, follow this professional workflow to ensure rigor, reproducibility, and actionable insights.

### 1. Project Initialization and Objective Setting
Begin by clearly defining the scope of the analysis. Before writing code, state the primary questions you aim to answer and the metrics that will define success.
- **Identify Goals**: What business or scientific question are we solving?
- **Define Metrics**: Are we looking for correlation, prediction accuracy, or trend identification?

### 2. Data Acquisition and Environment Setup
Load the data using the most efficient library for the task. Use `pandas` for standard datasets and `Polars` or `DuckDB` for high-performance requirements or large-scale data.
- **Library Selection**: Import `pandas`, `numpy`, `matplotlib.pyplot`, and `seaborn`. For advanced ML, include `scikit-learn`.
- **Loading**: Use `pd.read_csv()`, `pd.read_parquet()`, or `pl.read_csv()` depending on the format and size.

### 3. Exploratory Data Analysis (EDA)
Perform a systematic check of the data's health and structure.
- **Structural Audit**: Check `df.info()`, `df.shape`, and `df.head()`.
- **Statistical Summary**: Use `df.describe()` to understand distributions and identify potential outliers.
- **Quality Check**: Identify missing values with `df.isnull().sum()` and check for duplicate records.
- **Visual Exploration**: Create histograms for distributions and heatmaps for feature correlations.

### 4. Professional Data Cleansing
Clean data is the foundation of reliable analysis.
- **Handling Missingness**: Decide between imputation (mean/median/mode) or removal based on the nature of the missing data.
- **Type Conversion**: Ensure dates are `datetime` objects and categorical variables are correctly typed.
- **Standardization**: Clean string columns (lowercase, strip whitespace) and handle inconsistent naming.
- **Outlier Management**: Use Z-scores or Interquartile Range (IQR) to identify and address extreme values.

### 5. Feature Engineering and Preparation
Transform raw data into features that better represent the underlying problem.
- **Encoding**: Use One-Hot Encoding or Label Encoding for categorical data.
- **Scaling**: Apply `StandardScaler` or `MinMaxScaler` when using algorithms sensitive to feature scales (e.g., SVM, KNN).
- **Feature Creation**: Derive new insights (e.g., extracting "Day of Week" from a timestamp).

### 6. Modeling and Statistical Analysis
Apply appropriate mathematical or machine learning techniques.
- **Algorithm Selection**: Choose based on the task (Regression, Classification, Clustering).
- **Validation**: Always use a train-test split or cross-validation to prevent overfitting.
- **Evaluation**: Use appropriate metrics such as R-squared, F1-score, or RMSE.

### 7. Insight Communication
Deliver findings in a clear, non-technical manner supported by professional visualizations.
- **Visualization Best Practices**: Use `seaborn` for aesthetic statistical plots. Ensure all axes are labeled and titles are descriptive.
- **Executive Summary**: Conclude with 3-5 actionable insights derived directly from the data.

### Technical Gotchas and Best Practices
- **Memory Management**: For large datasets, downcast numeric types (e.g., `int64` to `int32`) or use chunking.
- **Reproducibility**: Set a `random_state` in all stochastic processes (like train-test splits).
- **Vectorization**: Avoid `for` loops; use `numpy` or `pandas` vectorized operations for performance.
