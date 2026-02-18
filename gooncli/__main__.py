from gooncli.app import clear
from gooncli.app import type_out
from asyncio import sleep
import sys
from .app import run_app, update

def main():

    if len(sys.argv) > 1:
        if sys.argv[1] == "update":
            update()
            return
    try:
        run_app()
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        sleep(1)
        type_out("Exiting..........")
        clear()
