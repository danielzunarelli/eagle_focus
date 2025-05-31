focus_name = []

def focus_menu():
    print("\nFocus Menu\n")
    option_focus = int(input(""
"   1: Register a new Focus\n"
"   2: List Focus\n"
"   3: Delete Focus\n"
"   4: Back to Menu\n"
"   9: Exit\n"
"   \nSelect one option: "
    ))

# Option 1 ##
    if option_focus == 1:
        name_focus = input("Name of Focus: ")
        focus_name.append(name_focus)
        print("\nFocus Saved Successfully!")
        return focus_menu()

# Option 2 ##
    if option_focus == 2:
        view_focus = input(" of Focus: ")
        focus_name.append(name_focus)
        print("\nFocus Saved Successfully!")
    return focus_menu()
