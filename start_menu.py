from main import option_menu

def start_menu():
    option_start = int(input(
        "   1: Select Focus\n"
        "   2: Back to Menu\n"
        "   9: Exit\n"
        "\nSelect one option: "
    ))

    if option_start == 1:
        print("Select Focus (not implemented yet)")
        return start_menu()
    elif option_start == 2:
        return option_menu()
    elif option_start == 9:
        print("Goodbye!")