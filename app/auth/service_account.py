from google.cloud import bigquery
from google.oauth2 import service_account


key_path = "app/auth/apigee-dev-442506-f4287a3a7731.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# Alternatively, use service_account.Credentials.from_service_account_info()
# to set credentials directly via a json object rather than set a filepath
#credentials = service_account.Credentials.from_service_account_info(key_json)



def get_bigquery_client():
    client = bigquery.Client(
        credentials=credentials,
        project=credentials.project_id,
    )
    return client