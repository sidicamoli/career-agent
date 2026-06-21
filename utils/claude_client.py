"""
This is the ONLY file in the whole project that talks to the Claude API.

Every feature (skill suggestions, cover letters, mock interview questions)
will call the ask_claude() function below instead of writing its own API
code. That way, if the API ever changes, we fix it in one place.
"""

from anthropic import Anthropic
from config import ANTHROPIC_API_KEY, CLAUDE_MODEL

# Create one client and reuse it for every request, rather than
# creating a brand new connection every time we want to ask something.
client = Anthropic(api_key=ANTHROPIC_API_KEY)


def ask_claude(prompt: str, system: str = "", max_tokens: int = 1024) -> str:
    """
    Send a prompt to Claude and return its reply as plain text.

    Args:
        prompt: The actual question or instruction (e.g. "Write a cover letter for...").
        system: Optional instructions describing HOW Claude should behave
                (e.g. "You are a career coach who writes concise, honest feedback.").
        max_tokens: The maximum length of Claude's reply. 1024 is plenty for
                    a paragraph or two; raise it for longer documents like
                    full cover letters.

    Returns:
        Claude's reply as a plain Python string.
    """
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    # message.content is a list of content blocks; for plain text replies,
    # the text we want is always in the first block.
    return message.content[0].text