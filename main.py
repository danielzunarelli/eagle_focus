from start_menu import start_menu
from focus_menu import focus_menu

print("\nWelcome to the Eagle Focus App\n")
option = int(input(""
"   1: Start\n"
"   2: Focus Settings\n"
"   9: Exit\n"
"   \nSelect one option:"))

if option == 1:
    start_menu() 
if option == 2: 
    focus_menu()