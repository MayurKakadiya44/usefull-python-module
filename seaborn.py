# ---
# title: Seaborn Tutorial
# description: A comprehensive tutorial on the Python Seaborn module, demonstrating key functionalities for data visualization.
# ---

# --- Introduction to the Seaborn Module ---
# Seaborn is a Python data visualization library built on top of Matplotlib, designed to create attractive and informative statistical graphics.
# Purpose: Simplifies the creation of complex visualizations with a high-level interface, focusing on statistical data exploration and presentation.
# Core features:
# - Provides high-level functions for common statistical plots (e.g., scatter, line, box, violin, heatmap).
# - Integrates seamlessly with Pandas DataFrames for easy data handling.
# - Offers built-in themes and color palettes for aesthetically pleasing visuals.
# - Supports advanced visualizations like pair plots, facet grids, and regression plots.
# - Enhances Matplotlib plots with less code and better defaults.
# - Requires installation: `pip install seaborn`
# - Seaborn has a total of 22 built-in datasets available for use, which are commonly used for practicing data visualization and analysis tasks

# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn theme for better aesthetics
sns.set_theme(style="darkgrid")  # Options: darkgrid, whitegrid, dark, white, ticks

# --- 1. Loading Sample Datasets ---
# Seaborn provides built-in datasets for testing
print("--- Loading Sample Datasets ---")
tips = sns.load_dataset("tips")  # Sample dataset: restaurant tips
iris = sns.load_dataset("iris")  # Sample dataset: iris flowers
print("Tips dataset head:\n", tips.head())
print("\nIris dataset head:\n", iris.head())

# --- 2. Basic Plotting: Scatter Plot ---
print("\n--- Scatter Plot ---")
# Scatter plot with hue and size for categorical differentiation
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", size="size")
plt.title("Scatter Plot: Tips vs Total Bill")
plt.show()

# --- 3. Categorical Plots: Bar Plot and Count Plot ---
print("\n--- Categorical Plots ---")
# Bar plot: Average tip by day
sns.barplot(data=tips, x="day", y="tip", hue="sex")
plt.title("Bar Plot: Average Tip by Day and Sex")
plt.show()

# Count plot: Frequency of categories
sns.countplot(data=tips, x="day", hue="time")
plt.title("Count Plot: Orders by Day and Time")
plt.show()

# --- 4. Distribution Plots: Histogram, KDE, and Box Plot ---
print("\n--- Distribution Plots ---")
# Histogram with kernel density estimate (KDE)
sns.histplot(data=tips, x="total_bill", kde=True, bins=20)
plt.title("Histogram with KDE: Total Bill Distribution")
plt.show()

# KDE plot: Smoothed density
sns.kdeplot(data=tips, x="tip", hue="sex", fill=True)
plt.title("KDE Plot: Tip Distribution by Sex")
plt.show()

# Box plot: Distribution summary
sns.boxplot(data=tips, x="day", y="tip", hue="smoker")
plt.title("Box Plot: Tips by Day and Smoker Status")
plt.show()

# --- 5. Violin Plot: Combining Density and Box Plot ---
print("\n--- Violin Plot ---")
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)
plt.title("Violin Plot: Total Bill by Day and Sex")
plt.show()

# --- 6. Pair Plot: Visualizing Pairwise Relationships ---
print("\n--- Pair Plot ---")
# Pair plot for iris dataset, showing relationships between numerical variables
sns.pairplot(data=iris, hue="species", diag_kind="kde")
plt.suptitle("Pair Plot: Iris Dataset", y=1.02)
plt.show()

# --- 7. Heatmap: Correlation and Matrix Visualizations ---
print("\n--- Heatmap ---")
# Calculate correlation matrix for numerical columns
corr = tips.select_dtypes(include=np.number).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Heatmap: Correlation Matrix of Tips Dataset")
plt.show()

# --- 8. Facet Grid: Multi-Plot Grids for Subgroups ---
print("\n--- Facet Grid ---")
# Facet grid: Scatter plots for each combination of smoker and time
g = sns.FacetGrid(tips, col="smoker", row="time")
g.map(sns.scatterplot, "total_bill", "tip")
g.set_titles(col_template="Smoker: {col_name}", row_template="Time: {row_name}")
plt.suptitle("Facet Grid: Tips by Smoker and Time", y=1.02)
plt.show()

# --- 9. Regression Plots ---
print("\n--- Regression Plots ---")
# Linear regression plot with confidence intervals
sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex", height=5)
plt.title("Regression Plot: Tips vs Total Bill by Sex")
plt.show()

# --- 10. Customizing Aesthetics: Themes and Palettes ---
print("\n--- Customizing Aesthetics ---")
# Set custom color palette
sns.set_palette("husl")  # Options: deep, muted, husl, Set1, Set2, etc.
sns.boxplot(data=tips, x="day", y="tip")
plt.title("Box Plot with Custom HUSL Palette")
plt.show()

# Reset theme and use context for different plot scales
sns.set_context("talk")  # Options: paper, notebook, talk, poster
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Scatter Plot with 'Talk' Context")
plt.show()

# --- 11. Joint Plot: Combining Scatter and Distributions ---
print("\n--- Joint Plot ---")
# Joint plot with scatter and marginal histograms
sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter", marginal_kws={"bins": 20})
plt.suptitle("Joint Plot: Total Bill vs Tip", y=1.02)
plt.show()

# --- 12. Advanced: Catplot for Flexible Categorical Plots ---
print("\n--- Catplot ---")
# Catplot: Flexible categorical plot (e.g., box plot by day and time)
sns.catplot(data=tips, x="day", y="tip", hue="sex", col="time", kind="box", height=5)
plt.suptitle("Catplot: Tips by Day, Sex, and Time", y=1.02)
plt.show()

# --- 13. Handling Missing Data ---
print("\n--- Handling Missing Data ---")
# Create a dataset with missing values
tips_with_na = tips.copy()
tips_with_na.loc[0:5, "tip"] = np.nan
# Box plot ignores missing values by default
sns.boxplot(data=tips_with_na, x="day", y="tip")
plt.title("Box Plot with Missing Data")
plt.show()

# --- 14. Saving Plots ---
print("\n--- Saving Plots ---")
# Save a plot to a file
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Scatter Plot: Saved to File")
plt.savefig("scatter_plot.png", dpi=300, bbox_inches="tight")
print("Plot saved as 'scatter_plot.png'")
plt.close()

# --- 15. Error Handling and Edge Cases ---
print("\n--- Error Handling ---")
# Handle invalid column names
try:
    sns.scatterplot(data=tips, x="nonexistent", y="tip")
except ValueError as e:
    print("Error: Invalid column name:", e)

# Handle empty data
try:
    empty_df = pd.DataFrame()
    sns.histplot(data=empty_df, x="col")
except ValueError as e:
    print("Error: Empty DataFrame:", e)

# --- 16. Working with Custom Data ---
print("\n--- Custom Data ---")
# Create a custom DataFrame
custom_data = pd.DataFrame({
    "x": np.random.randn(100),
    "y": np.random.randn(100) * 2,
    "category": np.random.choice(["A", "B"], 100)
})
sns.scatterplot(data=custom_data, x="x", y="y", hue="category")
plt.title("Scatter Plot: Custom Random Data")
plt.show()
