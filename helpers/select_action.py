from helpers.constants import *


def select_action(user_input):
    answer = ""
    if user_input == "1" or user_input == "sl":
        answer = GET_ALL_SCOPES
    elif user_input == "2" or user_input == "pl":
        answer = GET_ALL_PAGES
    elif user_input == "3" or user_input == "ct":
        answer = COUNT_RECORDS
    elif user_input == "4" or user_input == "rl":
        answer = SHOW_ALL_RECORDS
    elif user_input == "5" or user_input == "ctr":
        answer = CHECK_TEST_RECORD
    elif user_input == "6" or user_input == "cnv":
        answer = CONVERT_SCOPES
    elif user_input == "help":
        answer = HELP
    elif user_input == "0" or user_input == "exit" or user_input == "q":
        answer = EXIT
    return answer

