#!/bin/bash

echo GCP_ENV=$GCP_ENV >> .env
echo TEST=$TEST >> .env
echo GA_TRACKING_ID=$GA_TRACKING_ID >> .env
echo PROJECT_ID=$(project_name="${GCP_ENV}_project_id" && echo "${!project_name}") >> .env

echo -e "\nenv_variables:" >> app.yaml
while IFS= read -r line
do echo -e "  $line" | sed 's/=/: /g' >> app.yaml
done < .env
