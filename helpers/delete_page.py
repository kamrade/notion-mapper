import requests
from helpers.headers import headers, NOTION_URL


def delete_page(page_id: str):
    url = f"{NOTION_URL}pages/{page_id}"
    payload = {"archived": True}
    res = requests.patch(url, json=payload, headers=headers)
    print(res.status_code)
    return res

