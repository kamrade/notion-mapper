import requests
from helpers.headers import headers, DATABASE_ID, NOTION_URL


def create_page(data: dict):
    create_url = f"{NOTION_URL}pages"
    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}
    res = requests.post(create_url, headers=headers, json=payload)
    print(res.status_code)
    return res

