"""
config.py — StackSage Configuration
Reads from environment variables when deployed live.
"""
import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "sk-ant-api03-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")
GITHUB_TOKEN      = os.environ.get("GITHUB_TOKEN", "")
DATABASE_PATH     = "stacksage.db"
MAX_REPOS         = 12
DEBUG_MODE        = os.environ.get("DEBUG", "false").lower() == "true"
