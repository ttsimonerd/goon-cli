import sys
import argparse
from asyncio import sleep

from .app import run_app, update, run_mobile
from .app import clear, type_out
from .config import load_config, save_config, reset_config, DEFAULT_CONFIG


def main():
    # -----------------------------
    # Args
    # -----------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", default="run")
    parser.add_argument("key", nargs="?")
    parser.add_argument("value", nargs="?")
    args = parser.parse_args()

    # -----------------------------
    # Config command
    # -----------------------------
    if args.command == "config":
        handle_config(args)
        return

    # -----------------------------
    # Update command
    # -----------------------------
    if args.command == "update":
        update()
        return

    # -----------------------------
    # Mobile command
    # -----------------------------
    if args.command == "mobile":
        cfg = load_config()
        speed = cfg["speed"]
        run_mobile(speed)
        return

    # -----------------------------
    # Run App
    # -----------------------------
    cfg = load_config()
    speed = cfg["speed"]
    mobile = cfg["mobile_version"]

    try:
        if mobile:
            run_mobile(speed)
        else:
            run_app(speed)
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        sleep(1)
        type_out("Exiting..........")
        clear()


def handle_config(args):
    cfg = load_config()

    if args.key is None:
        print("Current configuration:")
        for k, v in cfg.items():
            print(f"  {k}: {v}")

        print("\nAvailable commands:")
        print("  goon config get <key>")
        print("  goon config set <key> <value>")
        print("  goon config reset")
        return

    # Reset config
    if args.key == "reset":
        reset_config()
        print("Configuration reset to defaults.")
        return

    # Validate key
    if args.key not in DEFAULT_CONFIG:
        print(f"Unknown config key: {args.key}")
        return

    # Get value
    if args.value is None:
        print(cfg[args.key])
        return

    # Set value
    cfg[args.key] = parse_value(args.value)
    save_config(cfg)
    print(f"Set {args.key} = {cfg[args.key]}")


def parse_value(v):
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    try:
        return int(v)
    except:
        try:
            return float(v)
        except:
            return v
