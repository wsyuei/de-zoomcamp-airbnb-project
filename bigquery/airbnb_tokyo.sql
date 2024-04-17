CREATE OR REPLACE EXTERNAL TABLE `example-de-zoomcamp.example_de_zoomcamp_dataset.airbnb_tokyo`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://example_de_zoomcamp_bucket/airbnb_data/review_date=*.parquet']
);