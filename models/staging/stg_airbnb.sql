{{
    config(
        materialized='view'
    )
}}


select
    -- identifiers
    cast(id as numeric) as id,
    cast(host_id as numeric) as host_id,
    
    -- timestamps
    cast(last_review as date) as review_date,
    
    -- host and property info
    name,
    --host_name,
    neighbourhood,
    room_type,
    cast(latitude as numeric) as latitude,
    cast(longitude as numeric) as longitude,
    cast(price as numeric) as price,

    -- other info
    cast(minimum_nights as numeric) as minimum_nights,
    cast(number_of_reviews as numeric) as number_of_reviews,
    cast(reviews_per_month as numeric) as reviews_per_month,
    cast(calculated_host_listings_count as numeric) as calculated_host_listings_count,
    cast(availability_365 as numeric) as availability_365,
    cast(number_of_reviews_ltm as numeric) as number_of_reviews_ltm,
    license
from {{ source('staging', 'airbnb_tokyo') }}


-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}



{% endif %}
