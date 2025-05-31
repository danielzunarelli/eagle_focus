import time
import itertools
import sys
import threading

spinner_running = True
spinner_paused = False

def spinner():
    spinner_cycle = itertools.cycle(['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏'])
    while spinner_running:
        sys.stdout.write("\033[s")              # Salva posição do cursor
        sys.stdout.write("\033[1A\r")           # Sobe 1 linha e vai pro início
        if not spinner_paused:
            sys.stdout.write(f"Focus is running {next(spinner_cycle)}   \n")
        else:
            sys.stdout.write("Focus is paused           \n")
        sys.stdout.write("\033[u")              # Restaura posição do cursor
        sys.stdout.flush()
        time.sleep(0.1)

def start_focus_timer(focus_name):
    global spinner_running, spinner_paused
    print(f"\nStarting focus session: {focus_name}")
    print("-" * 22)
    print("Focus Timer Menu")
    print("   1: Pause")
    print("   2: Resume")
    print("   3: Stop\n")

    start_time = time.time()
    paused_time = 0
    is_paused = False
    last_pause = None

    spinner_running = True
    spinner_paused = False
    spinner_thread = threading.Thread(target=spinner, daemon=True)
    spinner_thread.start()

    while True:
        option = input("Select an option: ")

        if option == "1" and not is_paused:
            is_paused = True
            spinner_paused = True
            last_pause = time.time()
            print("Paused.")

        elif option == "2" and is_paused:
            is_paused = False
            spinner_paused = False
            paused_duration = time.time() - last_pause
            paused_time += paused_duration
            print("Resumed.")

        elif option == "3":
            spinner_running = False
            spinner_thread.join()
            if is_paused:
                end_time = last_pause
            else:
                end_time = time.time()
            total_focus_time = end_time - start_time - paused_time
            print(f"\nFocus '{focus_name}' ended. Total time: {int(total_focus_time)} seconds.")
            break

        else:
            print("Invalid option.")