from datetime import datetime, timezone
from helpers.get_pages import get_pages
from helpers.create_page import create_page
from helpers.update_page import update_page
from helpers.delete_page import delete_page
from helpers.get_single_page import get_single_page

if user_input == "1" or user_input == "2":
    pages = get_pages(save_to_file=(user_input == "2"))

    print("Total pages: ", len(pages))

    for page in pages:
        page_id = page["id"]
        props = page["properties"]
        scope_select = props["Scope"]
        my_scope = props["My scope"]

        if len(my_scope["relation"]) != 0:
            # print("My scope: ", my_scope["relation"][0]["id"])
            for scope in scopes:
                if scope["id"] == my_scope["relation"][0]["id"]:
                    print(scope["properties"]["Name"]["title"][0]["text"]["content"])
                    print(page["properties"]["Task name"]["title"][0]["text"]["content"])

            # Get current page by ID
            # current_page = get_single_page(page_id)
            # print(current_page)

        if scope_select["select"]:
            current_scope = scope_select["select"]["name"]
            result[current_scope] += 1

        else:
            result["_empty"] += 1

    print(result)
        # relation = props["My scope"]
        # url = props["URL"]["title"][0]["text"]["content"]
        # title = props["Title"]["rich_text"][0]["text"]["content"]
        # published = props["Published"]["date"]["start"]
        # published = datetime.fromisoformat(published)

        # if len(relation['relation']) > 0:
            # print(f"Has relation: {url}", relation["relation"][0]["id"])
            # print(f"Has relation: {title} >>>", relation)

        # print(
        #     title, "\n",
        #     page_id, " | ",
        #     scope, " | ",
        #     url, " | ",
        #     published, " | ",
        #     relation
        # )

# create a page
if user_input == "3":
    url = input("Enter url: ")
    title = input("Enter title: ")
    published_date = datetime.now().astimezone(timezone.utc).isoformat()
    data = {
        "URL": {"title": [{"text": {"content": url}}]},
        "Title": {"rich_text": [{"text": {"content": title}}]},
        "Published": {"date": {"start": published_date, "end": None}},
        "My scope": {'id': 'fZrs', 'type': 'relation', 'relation': [{'id': '0f35d167-c056-4ec9-8a57-1ad9f5cda552'}]}
    }
    create_page(data)

# update
if user_input == "4":
    page_id = "40ae1f10-bf58-405c-92f3-836965f2d95b"
    title = "Updated title"
    update_data = {"Title": {"rich_text": [{"text": {"content": title}}]}}
    update_page(page_id, update_data)

# delete
if user_input == "5":
    page_id = "e26f4986-4e42-430f-8b50-43c950de1c21"
    delete_page(page_id)