import requests
from helpers.headers import headers, DATABASE_ID, NOTION_URL
from yaspin import yaspin


def get_single_page(page_id: str):
    url = f"{NOTION_URL}pages/{page_id}"
    with yaspin(text="Loading data", color="green") as spinner:
        try:
            response = requests.get(url, headers=headers)
        except requests.exceptions.RequestException as e:
            spinner.fail(f"🔴 Request {url} error")
            raise SystemExit(e)
        else:
            spinner.ok(f"✅ Request {url} success")
            data = response.json()
            return data

