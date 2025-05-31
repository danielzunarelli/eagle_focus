from main import option_menu 

focus_name = []

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
        focus_name.append(name_focus)
        print("\nFocus Saved Successfully!")
        return focus_menu()

    elif option_focus == 2:
        print("\nRegistered Focuses:")
        if focus_name:
            for i, focus in enumerate(focus_name, 1):
                print(f"{i}. {focus}")
        else:
            print("No focus registered yet.")
        return focus_menu()

    elif option_focus == 3:
        print("\nRegistered Focuses:")
        if focus_name:
            for i, focus in enumerate(focus_name, 1):
                print(f"{i}. {focus}")
            try:
                delete_index = int(input("\nEnter the number of the Focus to delete: ")) - 1
                if 0 <= delete_index < len(focus_name):
                    deleted = focus_name.pop(delete_index)
                    print(f"\nFocus '{deleted}' deleted successfully.")
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No focus registered yet.")
        return focus_menu()

    elif option_focus == 4:
        return option_menu()  # agora chama o menu corretamente

    elif option_focus == 9:
        print("Goodbye!")

    else:
        print("Invalid option.")
        return focus_menu()