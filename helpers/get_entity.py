from helpers.headers import headers, SCOPE_DATABASE_ID, NOTION_URL
from helpers.make_request import make_request
from helpers.paginator import paginator


# Only POST method
def get_entity(url, num_pages=None):
    get_all = num_pages is None
    page_size = 100 if get_all else num_pages
    payload = {"page_size": page_size}

    response = make_request("POST", url, headers, payload)

    data = response.json()
    results = data["results"]

    results = paginator(results, data, url, headers, num_pages)
    return results

