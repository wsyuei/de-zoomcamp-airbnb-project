{{
    config(
        materialized='table'
    )
}}

with airbnb_tokyo as (
    select *
    from {{ ref('stg_airbnb') }}
)

select
id,
review_date,
neighbourhood,
room_type,
price,
availability_365
from airbnb_tokyo