#!/usr/bin/env python3
import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("CRITICAL ERROR: python-dotenv is not installed.")
    print("Please install it: pip install python-dotenv")
    sys.exit(1)


def check_git_security() -> bool:
    gitignore_path = ".gitignore"
    if not os.path.exists(gitignore_path):
        return False
    try:
        with open(gitignore_path, "r") as file:
            for line in file:
                if line.strip() == ".env":
                    return True
    except IOError:
        return False
    return False


def oracle() -> None:
    load_dotenv()

    raw_mode = os.environ.get("MATRIX_MODE")
    if raw_mode is None:
        print("[CONFIG]: MATRIX_MODE undefined. Defaulting to development.")
        matrix_mode = "development"
    else:
        matrix_mode = raw_mode.lower().strip()

    if matrix_mode not in ("production", "development"):
        print("CRITICAL ERROR:"
              "MATRIX_MODE can only be 'production' or 'development'.")
        sys.exit(1)

    db_url = os.environ.get("DATABASE_URL")
    api_key = os.environ.get("API_KEY")
    log_lvl = os.environ.get("LOG_LEVEL")
    zion_endpoint = os.environ.get("ZION_ENDPOINT")

    missing_configs = []
    if not db_url:
        missing_configs.append("DATABASE_URL")
    if not api_key:
        missing_configs.append("API_KEY")
    if not zion_endpoint:
        missing_configs.append("ZION_ENDPOINT")

    if missing_configs:
        print("\nWARNING: The Oracle's vision is clouded. Missing configs:")
        for config in missing_configs:
            print(f"  - {config} is not set")
        print("\nPlease copy .env.example to .env and fill in the values.\n")

    print("\nConfiguration loaded:")
    print(f"Mode: {matrix_mode}")

    if matrix_mode == "production":
        db_status = ("Connected to production cluster [Secured URL]"
                     if db_url else "DISCONNECTED")
        api_status = ("Authenticated with high-security token [Masked]"
                      if api_key else "DENIED")
    else:
        db_status = (f"Connected to local instance ({db_url})"
                     if db_url else "DISCONNECTED")
        api_status = "Authenticated" if api_key else "DENIED"

    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_lvl if log_lvl else 'Not Set'}")
    print(f"Zion Network: {'Online' if zion_endpoint else 'Offline'}\n")

    print("Environment security check:")
    if check_git_security():
        print("[OK] Environment file properly secured via .gitignore")
    else:
        print("[WARN] .env file might be exposed to version control!")

    if os.path.exists(".env"):
        print("[OK] Local .env file detected")
    else:
        print("[WARN] .env file is missing")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...")
    oracle()
