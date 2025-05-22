"""
Comprehensive Tutorial: Python ydata-profiling (formerly pandas-profiling) Module

Purpose:
---------
The ydata-profiling module (previously called pandas-profiling) automates Exploratory Data Analysis (EDA) in Python.
It generates an interactive, detailed HTML report from a pandas DataFrame, summarizing:
    - Data types, statistics, and distributions
    - Missing values and duplicates
    - Correlations and interactions between variables
    - Sample data and alerts about potential issues

Core Features:
--------------
- One-line generation of exhaustive data profiling reports
- Visualizations for distributions, correlations, and missing data
- Customizable reports (title, sections, minimal mode, etc.)
- Export to HTML, JSON, or display inline in Jupyter/Colab
- Supports categorical, numeric, boolean, and datetime columns

Installation:
-------------
pip install ydata-profiling

References:
-----------
- https://www.datacamp.com/tutorial/pandas-profiling-ydata-profiling-in-python-guide [1]
- https://www.influxdata.com/blog/pandas-profiling-tutorial/ [2]
"""

# Import necessary libraries
import pandas as pd
from ydata_profiling import ProfileReport  # Main class for profiling

# 1. Load your dataset
# For demonstration, we'll use the Titanic dataset from seaborn
import seaborn as sns
df = sns.load_dataset('titanic')

# 2. Generate a basic profile report
profile = ProfileReport(df, title="Titanic Data Profiling Report", explorative=True)

# 3. Display the report inline (for Jupyter/Colab)
profile.to_notebook_iframe()  # Use .to_widgets() for interactive widgets

# 4. Save the report as an HTML file
profile.to_file("titanic_profile_report.html")

# 5. Key Customizations and Functionalities

# a) Minimal Mode (faster, less detailed; good for large datasets)
minimal_profile = ProfileReport(df, minimal=True, title="Minimal Titanic Report")
minimal_profile.to_file("titanic_profile_minimal.html")

# b) Exclude Variables or Sections
profile_exclude = ProfileReport(
    df,
    title="Exclude Variables Example",
    variables={"cat": {"ignore": ["embarked", "class"]}},  # Exclude specific categorical columns
    correlations={"pearson": False}  # Disable Pearson correlation section
)
profile_exclude.to_file("titanic_profile_exclude.html")

# c) Handling Sensitive Data (redact sample, hide variable names)
profile_sensitive = ProfileReport(
    df,
    title="Sensitive Data Example",
    samples={"head": 0, "tail": 0},  # Hide sample data
    anonymize=True  # Anonymize variable names
)
profile_sensitive.to_file("titanic_profile_sensitive.html")

# d) Output as JSON (for programmatic use)
report_json = profile.to_json()
with open("titanic_profile_report.json", "w") as f:
    f.write(report_json)

# e) Profile only a subset of the data (first 100 rows)
profile_subset = ProfileReport(df.head(100), title="Subset Profile (first 100 rows)")
profile_subset.to_file("titanic_profile_subset.html")

# 6. Advanced: Compare Two DataFrames (e.g., train vs test)
# For demonstration, split Titanic dataset
df_train = df.sample(frac=0.7, random_state=42)
df_test = df.drop(df_train.index)
profile_compare = ProfileReport(df_train, title="Train Data")
profile_compare.compare(df_test, title="Test Data Comparison").to_file("titanic_profile_compare.html")

# 7. Additional Options
# - You can control the report's appearance, toggle dark mode, adjust correlation thresholds, and more.
# - See full options: https://ydata-profiling.ydata.ai/docs/master/pages/reference/profile_report.html

# 8. Clean up (optional)
del profile, minimal_profile, profile_exclude, profile_sensitive, profile_subset, profile_compare

"""
Summary:
--------
ydata-profiling streamlines EDA by generating comprehensive, customizable reports from pandas DataFrames.
It is especially useful for quickly understanding new datasets, detecting anomalies, and preparing for deeper analysis or modeling.
"""
