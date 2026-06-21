"""
Central place for app settings.

Why a separate file? So that if you ever need to change the model name,
or where the API key comes from, you change it in exactly one place
instead of hunting through every file that uses it.
"""

import os
from dotenv import load_dotenv

# load_dotenv() reads the .env file and makes its values available
# through os.getenv(), as if they were normal environment variables.
load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# This is the model string for Claude Sonnet 4.6 as of mid-2026.
# If Anthropic releases a newer model later, this is the only line you'd change.
CLAUDE_MODEL = "claude-sonnet-4-6"

if not ANTHROPIC_API_KEY:
    raise ValueError(
        "ANTHROPIC_API_KEY not found.\n"
        "1. Copy .env.example to a new file named .env\n"
        "2. Paste your API key from https://console.anthropic.com/ into it\n"
    )