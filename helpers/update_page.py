import requests
from helpers.headers import headers, NOTION_URL
from yaspin import yaspin


def update_page(page_id: str, data: dict):

    url = f"{NOTION_URL}pages/{page_id}"
    payload = {"properties": data}

    with yaspin(text="Updating page…", color="green") as spinner:
        try:
            spinner.text = ""
            spinner.ok("Updated")
            res = requests.patch(url, json=payload, headers=headers)
        except requests.exceptions.RequestException as e:
            spinner.fail(f"🔴 Update error")
            raise SystemExit(e)
        else:
            return res

