from db import insert_focus, get_all_focus, delete_focus_by_id

def focus_menu():
    print("\nFocus Menu\n")
    option_focus = int(input(
        "   1: Register a new Focus\n"
        "   2: List Focus\n"
        "   3: Delete Focus\n"
        "   4: Back to Menu\n"
        "   9: Exit\n"
        "\nSelect one option: "
    ))

    if option_focus == 1:
        name_focus = input("Name of Focus: ")
        insert_focus(name_focus)
        print("\nFocus Saved Successfully!")
        return focus_menu()

    elif option_focus == 2:
        focus_list = get_all_focus()
        if focus_list:
            print("\nRegistered Focuses:")
            for f in focus_list:
                print(f"{f[0]}. {f[1]}")
        else:
            print("No focus registered yet.")
        return focus_menu()

    elif option_focus == 3:
        focus_list = get_all_focus()
        if focus_list:
            print("\nRegistered Focuses:")
            for f in focus_list:
                print(f"{f[0]}. {f[1]}")
            try:
                focus_id = int(input("\nEnter the number of the Focus to delete: "))
                delete_focus_by_id(focus_id)
                print("Focus deleted successfully.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No focus registered yet.")
        return focus_menu()

    elif option_focus == 4:
        from menu import option_menu 
        return option_menu()

    elif option_focus == 9:
        print("Goodbye!")