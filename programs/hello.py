def my_hello(name):
    print(f"Yo {name}")


def my_goodbye(name: str, formal: bool):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")