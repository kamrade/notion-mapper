from helpers.update_page import update_page

def scopes_calculation(all_pages, scopes):
    result = {
        "hs": 0,
        "lancer": 0,
        "showcase": 0,
        "edu": 0,
        "personal": 0,
        "falcon": 0,
        "trading": 0,
        "pet": 0,
        "unl": 0,
        "_empty": 0
    }

    scope_map = {
        "hs": {
            "name": "Haystack",
            "id": "ef8960d161c2421aa3450f6fd8757264"
        },
        "lancer": {
            "name": "Freelance",
            "id": "0381bc0cfa5d4d67a78d91f0c93892dc"
        },
        "showcase": {
            "name": "Showcase",
            "id": "e946742354a248798c5bdabb202b6afb"
        },
        "edu": {
            "name": "Edu",
            "id": "0f35d167c0564ec98a571ad9f5cda552"
        },
        "personal": {
            "name": "Personal",
            "id": "317220c0a4044b498ee836c018a91556"
        },
        "falcon": {
            "name": "Falcon",
            "id": "b16de9db3b784e759836008faa568e0f"
        },
        "trading": {
            "name": "Trading",
            "id": "6553dcb00f714539b6ce97d1bf99cdae"
        },
        "pet": {
            "name": "Pet",
            "id": "c30e7d4d0a3346ff912a73b114e4cb6b"
        },
        "unl": {
            "name": "Unlimint",
            "id": "004f4cdf0c7545bf8c40a8ba124cfe3a"
        },

    }

    # - go through all pages
    # - for each page
    # - - get its Scope

    for page in all_pages:
        # if page["properties"]["My scope"]["relation"]:
        #     for scope in scopes:
        #         if scope["id"] == page["properties"]["My scope"]["relation"][0]["id"]:
        #             if page["properties"]["Scope"]["select"]:
        #                 scope_in = page["properties"]["Scope"]["select"]["name"]
        #                 my_scope_in = scope["properties"]["Name"]["title"][0]["plain_text"]

        if page["properties"]["Scope"]["select"]:
            result[page["properties"]["Scope"]["select"]["name"]] += 1
        else:
            result["_empty"] += 1
    print(result)

    for page in all_pages:
        page_id = page.get("id")
        print("page id: ", page_id)
        if page["properties"]["Scope"]["select"]:
            key = page["properties"]["Scope"]["select"]["name"]
            print(scope_map.get(key).get('name'), " >>> ", scope_map.get(key).get('id'))

            update_page(page_id, {
                "My scope": {
                    "relation": [
                        {
                            "id": scope_map.get(key).get('id')
                        }
                    ]
                }
            })

