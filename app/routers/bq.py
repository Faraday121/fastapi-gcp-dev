from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header
from ..auth.service_account import  get_bigquery_client

router = APIRouter(
    prefix="/bq",
    tags=["bq"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/mock/", tags=["bq"])
async def get_all_user_id():
    client = get_bigquery_client()
    table_id = "apigee-dev-442506.API_data.mock_data01"
    table = client.get_table(table_id)  # Make an API request.

    # View table properties
    print(
        "Got table '{}.{}.{}'.".format(table.project, table.dataset_id, table.table_id)
    )
    print("Table schema: {}".format(table.schema))
    print("Table description: {}".format(table.description))
    print("Table has {} rows".format(table.num_rows))

    query = 'SELECT first_name FROM `apigee-dev-442506.API_data.mock_data01` LIMIT 10'

    query_job = client.query(query)
    first_name_list = []
    for row in query_job:
        first_name_list.append(row["first_name"])

    return first_name_list


