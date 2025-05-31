import time

def start_focus_timer(focus_name):
    print(f"\nStarting focus session: {focus_name}")
    start_time = time.time()
    paused_time = 0
    is_paused = False
    last_pause = None

    while True:
        print("\nFocus Timer Menu")
        print("   1: Pause")
        print("   2: Resume")
        print("   3: Stop")
        option = input("Select an option: ")

        if option == "1" and not is_paused:
            is_paused = True
            last_pause = time.time()
            print("Paused.")

        elif option == "2" and is_paused:
            is_paused = False
            paused_duration = time.time() - last_pause
            paused_time += paused_duration
            print("Resumed.")

        elif option == "3":
            if is_paused:
                end_time = last_pause
            else:
                end_time = time.time()
            total_focus_time = end_time - start_time - paused_time
            print(f"\nFocus '{focus_name}' ended. Total time: {int(total_focus_time)} seconds.")
            break

        elif option not in ["1", "2", "3"]:
            print("Invalid option.")