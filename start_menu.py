from focus_menu import focus_name
from focus_timer import start_focus_timer  # você precisa criar esse arquivo separadamente

def start_menu():
    option_start = int(input(
        "   1: Select Focus\n"
        "   2: Back to Menu\n"
        "   9: Exit\n"
        "\nSelect one option: "
    ))

    if option_start == 1:
        print("\nList of Focus:")
        if focus_name:
            for i, focus in enumerate(focus_name, 1):
                print(f"{i}. {focus}")
            try:
                select_focus = int(input("\nEnter the number of the Focus to start: ")) - 1
                if 0 <= select_focus < len(focus_name):
                    selected = focus_name[select_focus]
                    print(f"\nYou selected: {selected}")
                    start_focus_timer(selected) 
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No focus registered yet.")
        return start_menu()

    elif option_start == 2:
        from menu import option_menu
        return option_menu()

    elif option_start == 9:
        print("Goodbye!")