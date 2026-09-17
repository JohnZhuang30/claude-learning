"""
Configuration loader for Claude Learning project.
Loads settings from environment variables and .env files.
"""

import os
from dotenv import load_dotenv

def load_config():
    """Load configuration from environment."""
    load_dotenv()
    return {
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
        "model": os.getenv("CLAUDE_MODEL", "claude-opus"),
        "debug": os.getenv("DEBUG", "false").lower() == "true",
    }

if __name__ == "__main__":
    config = load_config()
    print(f"Config loaded: {config}")