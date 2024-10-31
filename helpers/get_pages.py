from helpers.headers import DATABASE_ID, NOTION_URL
from helpers.get_entity import get_entity


def get_pages(num_pages=None):
    url = f"{NOTION_URL}databases/{DATABASE_ID}/query"
    return get_entity(url, num_pages)

