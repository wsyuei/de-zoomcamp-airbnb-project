# Project Airbnb Tokyo

## Overview
This project is presented as part of the Data Engineering Zoomcamp by DataTalks.Club. It exclusively utilizes data sourced from https://insideairbnb.com/get-the-data/, focusing solely on Airbnb listings from Tokyo, Japan.


### Problem Statement:
This project aims to analyze Airbnb listings in Tokyo, Japan, focusing on the distribution of neighborhoods, room types, and trends in average price fluctuations over the years. By understanding these aspects, we aim to provide valuable insights for hosts to optimize their offerings and pricing strategies, and for guests to make informed decisions when planning their stays in Tokyo.

## Data Pipeline
The pipeline for this project will operate in batch mode, designed to run periodically on a quarterly basis.

## Technologies
Cloud: GCP
Infrastructure as code (IaC): Terraform
Workflow orchestration: Mage
Data Warehouse: BigQuery
Batch Processing: DBT Cloud
Data Visualisation: Google Looker

## Content 
### Creating a pipeline for processing this dataset and putting it to a datalake
Workflow Orchestration:
![screenshot1](/screenshots/image3.png)
The process includes using Mage to extract, transform, and load data from an API to Google Cloud Storage (GCS).
1. Load data locally from the dataset, specify the data types and last_review as parse_date. 
2. Preprocess and clean the data, remove duplicate and blank rows and columns as well as price with blank values. Format last_review column from datetime to date.
3. Partition the data using last_review date.
4. Export partitioned data parquet file to GCS bucket.
5. The pipeline is set to be executed once a month on the 1st of every month.
![screenshot2](/screenshots/image4.png)

### Creating a pipeline for moving the data from the lake to a data warehouse
1. Create a dataset on BigQuery.
2. Load raw data to Bigquery from Google Cloud Storage Bucket.
3. Dataset name: example_de_zoomcamp_dataset
4. Run query below to build a table with all available data.
5. Table name: airbnb_tokyo
![screenshot3](/screenshots/image5.png)

### Transforming the data in the data warehouse: prepare it for the dashboard
Use DBT to load the data to BigQuery.
1. Staging:
  - Load data source from dataset_airbnb_tokyo.
  - Build a staging model.
  - Define the data types and rename columns.
  - Exposing the output of a dbt model in a warehouse as a view.
2. Core:
  - Contain only related production ready data.
  - Exposing the output of a dbt model in a warehouse as a table to Bigquery.
![screenshot4](/screenshots/image5.png)
3. Environment and Job Triggers:
  - The production environment will be set up as well as the job of deploy the pipeline once a week on Monday.
![screenshot5](/screenshots/image1.png)

### Building a dashboard to visualize the data
1. Open fact_airbnb_tokyo dataset in BigQuery and select Explore in Looker
2. Build dashboard as below:
3. Link: https://lookerstudio.google.com/s/ivQQ5nt5vPI 
![screenshot6](/screenshots/image6.png)

## Reproducibility:
1. Create a new project on Google Cloud with name: example-de-zoomcamp
2. Setup service account for project:
  1. Go to IAM & Admin > Service Accounts.
  2. Create Service account 
  3. Enter Service account name: airbnb. 
  4. Create and continue.
  5. Grant this service account access to project : Viewer, Storage Object Admin, Storage Admin, BigQuery Admin
  6. Continue > Done.
  7. Go to Manage Key> Add New Key> Json> Create. 
3. Rename the json file to my_credential.json and Move the downloaded json file to folder keys.
4. Run commands:
   """
  terraform init
  terraform plan
  terraform apply
"""
6. Mage:
  > docker compose up
6. Go to http://localhost:6789/
7. Run pipeline: airbnb_to_gcs to deploy the pipeline.
8. BigQuery:
  - Run query in airbnb_tokyo.sql.
9. DBT:
  1. Set up a DBT project.
  2. Add this github repo for version control.
  3. Connect to Bigquery using my_credential.json.
  4. Run build.
  5. Set up the job in a production environment.
  6. Job will be triggered on every  Monday. 

10. Go to BigQuery and table fact_airbnb_tokyo should exist in BigQuery Dataset.
11. Select the table and select Explore in Looker to develop the dashboard.



If the dashboard is not available, please refer to folder ./dashboard for the image and exported pdf files of dashbaord developed.
