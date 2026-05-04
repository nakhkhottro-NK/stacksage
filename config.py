
config.py — StackSage Configuration
Reads from environment variables when deployed live.
"""
import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
GITHUB_TOKEN      = os.environ.get("GITHUB_TOKEN", "")
DATABASE_PATH     = "stacksage.db"
MAX_REPOS         = 12
DEBUG_MODE        = os.environ.get("DEBUG", "false").lower() == "true"
