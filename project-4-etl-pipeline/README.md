# Project 4 — EIA US Energy Price ETL Pipeline

## Overview

**Author:** Enoch Effah | **Date:** June 2026

Automated ETL pipeline that extracts US residential electricity price data
from the EIA API, transforms it with pandas, and analyzes price trends
across all 50 states. Scheduled monthly with Apache Airflow on WSL2.

## Business Context

Tesla Energy's Powerwall value proposition depends on electricity price
volatility. States with high prices = best Powerwall markets. This pipeline
tracks exactly that — automatically, every month.

## Key Findings (March 2026)

- **Most expensive:** Hawaii at 42.23 cents/kWh
- **Cheapest:** North Dakota at 11.95 cents/kWh
- **National average:** 19.45 cents/kWh
- Hawaii pays 3.5x more than North Dakota — directly maps to Tesla Powerwall ROI

## Pipeline Architecture

- **Extract:** Pulls 100 records from EIA API (residential sector, sorted by date)
- **Transform:** Cleans columns, renames fields, converts types, adds timestamp
- **Analyze:** Prints top 5 most/least expensive states and national average

## Tools Used

- Python (pandas, requests, python-dotenv)
- Apache Airflow 2.7.2
- WSL2 (Ubuntu)
- EIA Open Data API

## Setup

1. Clone this repository
2. Install WSL2 and Ubuntu
3. Install Apache Airflow 2.7.2 with Python 3.11
4. Create `.env` file: `EIA_API_KEY=your_key_here`
5. Get free API key at: https://www.eia.gov/opendata/register.php
6. Copy DAG file to `~/airflow/dags/`
7. Trigger in Airflow UI at `http://localhost:8080`
