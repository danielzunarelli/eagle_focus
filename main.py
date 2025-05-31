from menu import option_menu
from db import create_tables

if __name__ == "__main__":
    create_tables()
    option_menu()