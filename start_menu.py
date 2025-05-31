from db import get_all_focus
from focus_timer import start_focus_timer
from menu import option_menu

def start_menu():
    option_start = int(input(
        "   1: Select Focus\n"
        "   2: Back to Menu\n"
        "   9: Exit\n"
        "\nSelect one option: "
    ))

    if option_start == 1:
        focus_list = get_all_focus()
        if focus_list:
            print("\nList of Focus:")
            for f in focus_list:
                print(f"{f[0]}. {f[1]}")
            try:
                selected_id = int(input("\nEnter the number of the Focus to start: "))
                selected = next((f[1] for f in focus_list if f[0] == selected_id), None)
                if selected:
                    print(f"\nYou selected: {selected}")
                    start_focus_timer(selected)
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No focus registered yet.")
        return start_menu()

    elif option_start == 2:
        return option_menu()
    
    elif option_start == 9:
        print("Goodbye!")