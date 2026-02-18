from time import sleep
import random
import time
import itertools
import shutil
import os
import sys
import threading

# ------------
# Paths
# ------------
ANIMATIONS_P = "~/local-goon-project/gooncli/anim-list.txt"
VIDS_P = "~/local-goon-project/gooncli/vids-list.txt"
HEN_P = "~/local-goon-project/gooncli/henlist.txt"
NAMES_P = "~/local-goon-project/gooncli/ph-namelist.txt"

# ------------
# Colors
# ------------
HK_GREEN = "\033[92m"
HK_PURPLE = "\033[95m"
HK_LIGHT_PURPLE = "\033[35m"
HK_RED = "\033[91m"
RESET = "\033[0m"
COLORS = [
    "\033[92m",
    "\033[94m",
    "\033[95m",
    "\033[96m"
]
# ------------
# Functions
# ------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def random_line(file):
    return random.choice(open(file).read().splitlines())

def loading(text="Loading", duration=3, speed=0.1):
    spinner = itertools.cycle(["{}".format(HK_GREEN+"|"+RESET), "{}".format(HK_GREEN+"/"+RESET), "{}".format(HK_GREEN+"-"+RESET), "{}".format(HK_GREEN+"\\"+RESET)])
    end_time = time.time() + duration
    while time.time() < end_time:
        frame = next(spinner)
        print(f"\r{HK_GREEN}{text} {frame}", end="", flush=True)
        time.sleep(speed)
        print("\r" + " " * (len(text) + 2) + "\r", end="") # clear line

def choose_goon():
    return "Yes" if random.randint(1, 100) <= 60 else "No"

def choose_list():
    return random.choice([HK_GREEN + "Animations", "Videos", "Hentais/Anime", "Names"])

def section(title):
    type_out("\n" + HK_LIGHT_PURPLE + "=" * 40 + RESET, speed=0.01)
    type_out(HK_LIGHT_PURPLE + title + RESET)
    type_out(HK_LIGHT_PURPLE + "=" * 40 + RESET, speed=0.01)

def type_out(text, speed=0.067):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

def load_logo():
    with open("local-goon-project/gooncli/logo.txt", "r", encoding="utf-8") as f:
        return f.read().splitlines()

def print_centered_logo(path="~/local-goon-project/gooncli/logo.txt"):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    width, _ = shutil.get_terminal_size()

    for line in lines:
        type_out_colored(line.center(width), speed=0.005)

def type_out_colored(text, speed=0.005):
    for char in text:
        if char.strip():
            color = random.choice(COLORS)
            print(color + char + RESET, end="", flush=True)
        else:
            print(char, end="", flush=True)
        time.sleep(speed)
    print()

def print_border():
    width, _ = shutil.get_terminal_size()
    print("+" + "-" * (width - 2) + "+")

def cursor_loop():
    while True:
        print("_", end="", flush=True)
        time.sleep(0.4)
        print("\b \b", end="", flush=True)
        time.sleep(0.4)

def input_with_cursor(prompt=""):
    t = threading.Thread(target=cursor_loop, daemon=True)
    t.start()
    return input(prompt)

# -----------
# Variables
# -----------
goon_today = 0

# ------------
# Main Body
# ------------
def run_app():
    clear()
    sleep(1)
    print_border()
    sleep(1)
    print_centered_logo()
    sleep(1)
    print_border()
    print("\n")
    sleep(1)
    type_out_colored("Hello, welcome to the local goon project!")
    sleep(1)
    type_out("Do you want to take a try? (Yes/No) ")
    yes_no =input("").lower()
    if yes_no == "yes" or yes_no == "y":
        clear()
        sleep(0.5)
        section("First step, incoming")
        sleep(1)
        loading(text="Choosing", duration=2)
        type_out(f"Should you goon today?:")
        sleep(1)
        goon = choose_goon()
        if goon == "Yes":
            goon_today += 1
            type_out(HK_GREEN + goon + RESET)
        else:
            type_out(HK_RED + goon + RESET)
            sleep(1)
            clear()
            type_out(HK_RED + "Ooh! Sorry!" + RESET)
            sleep(1)
            type_out(HK_RED + "Maybe next time?" + RESET)
            sleep(0.5)
            type_out(HK_GREEN + "Exiting............................................" + RESET)
            clear()
    else:
        sleep(1)
        type_out(HK_RED + "Ok" + RESET)
        sleep(1.5)
        type_out(HK_RED + "Goodbah" + RESET)
        sleep(0.5)
        type_out(HK_GREEN + "Exiting............................................" + RESET)
        clear()

    if goon_today == 1:
        sleep(2)
        clear()
        section("Second step, incoming")
        sleep(1)
        loading(text="Choosing available lists", duration=3)
        type_out(HK_RED + "You will goon to something..." + RESET)
        sleep(1)
        goon_from = choose_list()
        type_out(f"From the {HK_GREEN + goon_from + RESET} list!")
        sleep(2)
        clear()
        section("Third and last step, incoming")
        sleep(1)
        loading(text="Chosing from the list", duration=3)
        if goon_from == "Animations":
            type_out(f"From the {HK_GREEN + goon_from + RESET} list you will goon to...")
            sleep(1)
            type_out(random_line(ANIMATIONS_P))
            sleep(0.5)
            type_out(HK_GREEN + "Have fun!" + RESET)
            sleep(2)
        elif goon_from == "Videos":
            type_out(f"From the {HK_GREEN + goon_from + RESET} list you will goon to...")
            sleep(1)
            type_out(random_line(VIDS_P))
            sleep(0.5)
            type_out(HK_GREEN + "Have fun!" + RESET)
            sleep(2)
        elif goon_from == "Hentais/Anime":
            type_out(f"From the {HK_GREEN + goon_from + RESET} list you will goon to...")
            sleep(1)
            type_out(random_line(HEN_P))
            sleep(0.5)
            type_out(HK_GREEN + "Have fun!" + RESET)
            sleep(2)
        elif goon_from == "Names":
            type_out(f"From the {HK_GREEN + goon_from + RESET} list you will goon to...")
            sleep(1)
            type_out(random_line(NAMES_P))
            sleep(0.5)
            type_out(HK_GREEN + "Have fun!" + RESET)
            sleep(2)