import sys
from .app import run_app, update

def main():

    if len(sys.argv) > 1:
        if sys.argv[1] == "update":
            update()
            return
    run_app()
