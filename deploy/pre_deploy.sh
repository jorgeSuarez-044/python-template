#!/bin/bash

echo GCP_ENV=$GCP_ENV >> .env
echo TEST=$TEST >> .env
echo GA_TRACKING_ID=$GA_TRACKING_ID >> .env
echo PROJECT_ID="${GCP_ENV}_project_id"
echo BIG_QUERY_KEY=$BIG_QUERY_KEY >> .env

echo -e "\nenv_variables:" >> app.yaml
while IFS= read -r line
do echo -e "  $line" | sed 's/=/: /g' >> app.yaml
done < .env
