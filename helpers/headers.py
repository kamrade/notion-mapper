import os
from dotenv import load_dotenv
load_dotenv()


NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["DATABASE_ID"]
SCOPE_DATABASE_ID = os.environ["SCOPE_DATABASE_ID"]
NOTION_URL = "https://api.notion.com/v1/"


headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}