from db import insert_focus, get_all_focus_total_time, delete_focus_by_name
import time

def focus_menu():
    from menu import option_menu

def focus_menu():
    from menu import option_menu
    print("\n===========  FOCUS MENU ===========")
    option_focus = int(input(
        "   1: Register a new Focus\n"
        "   2: List Focus\n"
        "   3: Delete Focus\n"
        "   4: Back to Menu\n"
        "   9: Exit\n"
        "====================================\n"
        "Select one option: "
    ))

    if option_focus == 1:
        name_focus = input("Name of Focus: ")
        insert_focus(name_focus)
        print("\nFocus Saved Successfully!")
        return focus_menu()

    elif option_focus == 2:
        focus_list = get_all_focus_total_time()
        if focus_list:
            print("\nRegistered Focuses:")
            for name, duration in focus_list:
                formatted = time.strftime("%H:%M:%S", time.gmtime(duration))
                print(f"{name} — Total: {formatted}")
        else:
            print("No focus registered yet.")
        return focus_menu()

    elif option_focus == 3:
        focus_list = get_all_focus_total_time()
        if focus_list:
            print("\nRegistered Focuses:")
            for i, (name, duration) in enumerate(focus_list, 1):
                formatted = time.strftime("%H:%M:%S", time.gmtime(duration))
                print(f"{i}. {name} — Total: {formatted}")
            try:
                index = int(input("\nEnter the number of the Focus to delete: ")) - 1
                if 0 <= index < len(focus_list):
                    delete_focus_by_name(focus_list[index][0])
                    print("Focus deleted successfully.")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No focus registered yet.")
        return focus_menu()

    elif option_focus == 4:
        return option_menu()

    elif option_focus == 9:
        print("Goodbye!")