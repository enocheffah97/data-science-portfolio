# Retail Sales Exploratory Data Analysis

## Overview

**Author:** Enoch Effah | **Date:** May 2026

Exploratory data analysis of 9,994 retail orders from a US-based superstore (2015-2018). The goal was to identify key drivers of profitability and uncover patterns in sales, discounts, and regional performance.

## Business Questions

- Which product category generates the most profit?
- Which region is most and least profitable?
- Does discounting hurt or help profit?
- How have sales trended over time?

## Key Findings

- **Technology** leads in profitability with a healthy margin
- **Furniture** generates $740K in sales but only ~$18K in profit — needs investigation
- **Central region** has the worst profit margin (7.92%) despite outselling the South ($501K vs $391K)
- **Discounts above 40%** consistently generate losses — weak negative correlation of -0.22 - there are other factors at play
- **Q4 seasonality** is clear and predictable every year

## Tools Used

- Python (pandas, matplotlib, seaborn)
- Jupyter Notebook
- Git & GitHub

## Dataset

[Sample Superstore Dataset — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

## How to Run

1. Clone this repository
2. Install dependencies: `pip install pandas matplotlib seaborn jupyter`
3. Open `analysis.ipynb` in Jupyter Notebook or VS code
4. Run all cells in order
