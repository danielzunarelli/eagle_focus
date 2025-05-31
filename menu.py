# menu.py
from start_menu import start_menu
from focus_menu import focus_menu

def option_menu():
    print("\n######################################")
    print("            EAGLE FOCUS APP         ")
    print("######################################\n")
    option = int(input(
        "   1: Start\n"
        "   2: Focus Settings\n"
        "   9: Exit\n"
        "\nSelect one option: "
    ))

    if option == 1:
        start_menu()
    elif option == 2:
        focus_menu()
    elif option == 9:
        print("Goodbye!")
    else:
        print("Invalid option.")
        option_menu()