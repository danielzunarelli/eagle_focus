from db import get_all_focus_total_time
from focus_timer import start_focus_timer
import time

def start_menu():
    print("\n===========  START MENU ===========")
    option_start = int(input(
        "   1: Select Focus\n"
        "   2: Back to Menu\n"
        "   9: Exit\n"
        "====================================\n"
        "Select one option: "
    ))

    if option_start == 1:
        focus_list = get_all_focus_total_time()
        if focus_list:
            print("\nList of Focus:")
            for i, (name, duration) in enumerate(focus_list, 1):
                formatted = time.strftime("%H:%M:%S", time.gmtime(duration))
                print(f"{i}. {name} — Total: {formatted}")
            try:
                selected_index = int(input("\nEnter the number of the Focus or press any other number to go back: ")) - 1
                if 0 <= selected_index < len(focus_list):
                    selected_focus = focus_list[selected_index][0]  # nome do focus
                    print(f"\nYou selected: {selected_focus}")
                    start_focus_timer(selected_focus)
                else:
                    print("\nReturning to the menu:")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No focus registered yet.")
        return start_menu()

    elif option_start == 2:
        from menu import option_menu 
        return option_menu()

    elif option_start == 9:
        print("Goodbye! See you soon!")