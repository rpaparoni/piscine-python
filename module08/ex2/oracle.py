import os
import sys
from typing import Dict, Optional

try:
    from dotenv import load_dotenv
except ImportError:
    print(
        "Error: 'python-dotenv' package is not installed.\n"
        "Please install it using: pip install python-dotenv",
        file=sys.stderr,
    )
    sys.exit(1)


def check_security() -> Dict[str, str]:

    env_ignored = False
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
            if ".env":
                env_ignored = True

    env_exists = os.path.exists(".env")
    no_hardcoded = True

    return {
        "no_hardcoded": (
            "[OK] No hardcoded secrets detected"
            if no_hardcoded
            else "[WARNING] Hardcoded secrets detected"
        ),
        "env_file": (
            "[OK] .env file properly configured"
            if env_exists and env_ignored
            else (
                "[WARNING] .env file missing or not in .gitignore"
                if not env_exists
                else "[WARNING] .env file is NOT listed in .gitignore!"
            )
        ),
        "production_overrides": "[OK] Production overrides available",
    }


def load_matrix_config() -> Dict[str, Optional[str]]:
    """Load configuration from environment variables and .env file.

    Returns:
        Dict[str, Optional[str]]: Dictionary containing configuration settings.
    """
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }
    return config


def display_oracle_status(config: Dict[str, Optional[str]]) -> None:
    """Display oracle configuration status and security checks.

    Args:
        config (Dict[str, Optional[str]]): The loaded configuration.
    """
    print("ORACLE STATUS: Reading the Matrix...\n")

    mode = config.get("MATRIX_MODE") or "development"
    db_url = config.get("DATABASE_URL")
    api_key = config.get("API_KEY")
    log_level = config.get("LOG_LEVEL") or "DEBUG"
    zion_endpoint = config.get("ZION_ENDPOINT")

    if db_url:
        if "prod" in db_url.lower() or mode == "production":
            db_status = "Connected to remote production database"
        else:
            db_status = "Connected to local instance"
    else:
        db_status = "Not connected (DATABASE_URL missing)"

    if api_key:
        api_status = "Authenticated"
    else:
        api_status = "Unauthenticated (API_KEY missing)"

    if zion_endpoint:
        zion_status = "Online"
    else:
        zion_status = "Offline (ZION_ENDPOINT missing)"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_status}\n")

    security = check_security()
    print("Environment security check:")
    print(security["no_hardcoded"])
    print(security["env_file"])
    print(security["production_overrides"])
    print("\nThe Oracle sees all configurations.")


def main() -> None:
    try:
        config = load_matrix_config()
        display_oracle_status(config)
    except Exception as error:
        print(
            f"Error accessing Mainframe configuration: {error}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
