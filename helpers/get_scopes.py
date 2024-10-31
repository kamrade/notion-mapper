from helpers.headers import SCOPE_DATABASE_ID, NOTION_URL
from helpers.get_entity import get_entity


def get_scopes(num_pages=None):
    url = f"{NOTION_URL}databases/{SCOPE_DATABASE_ID}/query"
    return get_entity(url)

