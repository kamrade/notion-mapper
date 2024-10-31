from helpers.get_scopes import get_scopes
from helpers.get_pages import get_pages
from helpers.write_to_file import write_to_file
from helpers.constants import *
from helpers.select_action import select_action
from colorama import init as colorama_init, Fore
from scope_commands.test_record_manipulation import test_record_manipulation
from scope_commands.convert_scopes import convert_scopes
from scope_commands.scopes_calculation import scopes_calculation
colorama_init()


def my_scope():
    all_pages = get_pages()
    counter = len(all_pages)
    scopes = get_scopes()
    answer = ""

    while answer != EXIT:
        user_input = input(Fore.GREEN + "Enter command: " + Fore.WHITE)
        answer = select_action(user_input)

        if answer == GET_ALL_SCOPES:
            write_to_file("output/all_scopes.json", scopes)

        elif answer == GET_ALL_PAGES:
            write_to_file("output/all_pages.json", all_pages)

        elif answer == COUNT_RECORDS:
            print(f"🧮 Total pages: {counter}")

        elif answer == CONVERT_SCOPES:
            convert_scopes()

        elif answer == CHECK_TEST_RECORD:
            test_record_manipulation(scopes)

        elif answer == SHOW_ALL_RECORDS:
            scopes_calculation(all_pages, scopes)

        elif answer == HELP:
            print(f"Possible commands: ")

        elif answer == EXIT:
            print("🤟 Exit program")
            answer = EXIT

        else:
            print(f"Operational error. Try again")


