import inquirer
from helpers.update_page import update_page


def test_record_manipulation(scopes):
    test_page_id = "0dadb176496c4d1fa2a3df21c85adca3"
    scope_list = list(map(lambda scope_list_item: {
        "id": scope_list_item["id"],
        "title": scope_list_item["properties"]["Name"]["title"][0]["plain_text"]
    }, scopes))
    scope_names_list = list(map(lambda scope_list_item: scope_list_item["title"], scope_list))

    selected_my_scope_title = inquirer.list_input("Select the My Scope", choices=scope_names_list)
    selected_my_scope_id = ""
    for scope_item in scope_list:
        if scope_item["title"] == selected_my_scope_title:
            selected_my_scope_id = scope_item["id"]
            break

    update_page(test_page_id, {
        "My scope": {
            "relation": [
                {
                    "id": selected_my_scope_id
                }
            ]
        }
    })

