# Retail Customer & Category SQL Analysis

## Overview

**Author:** Enoch Effah | **Date:** May 2026

This project analyzes customer profitability, product category
performance, and regional trends using SQL and Python. Data was
loaded into a MySQL database and queried directly into Python
for visualization. The goal was to find out where the company
is losing money and why.

## Business Questions

- Who are our most and least profitable customers?
- Which product categories and sub-categories generate the most losses?
- Which region and category combination is most and least profitable?

## Key Findings

- **Sean Miller** is the highest spending customer ($25,043) but
  generates a -$1,980 loss — high sales does not mean high value
- **Tables** is the worst sub-category at -8.56% profit margin
- **Furniture underperforms in every region** — this is a company-wide
  pricing problem, not a regional one
- **Central + Furniture** is the worst region/category combination
  at -1.59% margin
- **West + Office Supplies** leads at 24.01% — the benchmark for
  the rest of the business

## Tools Used

- MySQL (database setup, querying, data cleaning)
- Python (pandas, matplotlib, seaborn)
- Jupyter Notebook
- Git & GitHub

## Dataset

Same Superstore dataset loaded into MySQL locally.
Original source:
[Sample Superstore — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

## How to Run

1. Clone this repository
2. Set up MySQL and import `superstore.csv` into a database
   called `superstore_db`
3. Create a `.env` file with your MySQL password:
   `MYSQL_PASSWORD=yourpassword`
4. Install dependencies:
   `pip install pandas matplotlib seaborn mysql-connector-python python-dotenv`
5. Open `analysis.ipynb` and run all cells
