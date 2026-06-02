from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv(os.path.expanduser('~/projects/project-4-etl-pipeline/.env'))

EIA_API_KEY = os.environ.get('EIA_API_KEY', '')

dag = DAG(
    'energy_price_pipeline',
    description='EIA US Energy Price ETL Pipeline',
    schedule_interval='@monthly',
    start_date=datetime(2024, 1, 1),
    catchup=False
)

RAW_PATH = os.path.expanduser(
    '~/projects/project-4-etl-pipeline/raw_energy_data.csv')
CLEAN_PATH = os.path.expanduser(
    '~/projects/project-4-etl-pipeline/clean_energy_data.csv')


def extract():
    print("Extracting EIA energy price data...")
    url = f"https://api.eia.gov/v2/electricity/retail-sales/data/?api_key={EIA_API_KEY}&data[]=price&facets[sectorid][]=RES&sort[0][column]=period&sort[0][direction]=desc&length=100"
    response = requests.get(url)
    data = response.json()
    records = data['response']['data']
    df = pd.DataFrame(records)
    df['extracted_at'] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    df.to_csv(RAW_PATH, index=False)
    print(f"Extracted {len(df)} records saved to {RAW_PATH}")


def transform():
    print("Transforming data...")
    df = pd.read_csv(RAW_PATH)
    df = df[['period', 'stateid', 'stateDescription',
             'price', 'price-units', 'extracted_at']]
    df = df.rename(columns={
        'period': 'month',
        'stateid': 'state_code',
        'stateDescription': 'state_name',
        'price': 'avg_price_cents_kwh',
        'price-units': 'units'
    })
    df['avg_price_cents_kwh'] = pd.to_numeric(
        df['avg_price_cents_kwh'], errors='coerce')
    df = df.dropna(subset=['avg_price_cents_kwh'])
    df = df.sort_values('month', ascending=False)
    df.to_csv(CLEAN_PATH, index=False)
    print(f"Transformed data saved to {CLEAN_PATH}")


def analyze():
    print("Analyzing energy prices...")
    df = pd.read_csv(CLEAN_PATH)
    print("\n=== US RESIDENTIAL ELECTRICITY PRICE ANALYSIS ===")
    print(f"Total records: {len(df)}")
    print(f"Date range: {df['month'].min()} to {df['month'].max()}")
    print(f"Extracted at: {df['extracted_at'].iloc[0]}")
    latest = df[df['month'] == df['month'].max()]
    print(f"\nTop 5 most expensive states:")
    top5 = latest.nlargest(5, 'avg_price_cents_kwh')[
        ['state_name', 'avg_price_cents_kwh']]
    print(top5.to_string(index=False))
    print(f"\nTop 5 cheapest states:")
    bottom5 = latest.nsmallest(5, 'avg_price_cents_kwh')[
        ['state_name', 'avg_price_cents_kwh']]
    print(bottom5.to_string(index=False))
    national_avg = latest['avg_price_cents_kwh'].mean()
    print(f"\nNational average: {national_avg:.2f} cents/kWh")


extract_task = PythonOperator(
    task_id='extract', python_callable=extract, dag=dag)
transform_task = PythonOperator(
    task_id='transform', python_callable=transform, dag=dag)
analyze_task = PythonOperator(
    task_id='analyze', python_callable=analyze, dag=dag)
