from helpers.get_scopes import get_scopes
import json


scopes = get_scopes()
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


user_input = input('Enter an action code: ')

# get all scopes
if user_input == "6":
    scopes = get_scopes()
    with open("output/all_scopes.json", "w", encoding="utf-8") as f:
        try:
            json.dump(scopes, f, ensure_ascii=False, indent=4)
        except TypeError:
            print("Error writing file.")
