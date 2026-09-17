"""
Claude Learning API module.
This module demonstrates basic API structure.
"""

import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def hello_claude():
    """Return a greeting."""
    return "Hello, Claude!"

if __name__ == "__main__":
    result = hello_claude()
    if result:
        print(result)