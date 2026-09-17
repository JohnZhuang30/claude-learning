"""
Claude Learning API module.
This module demonstrates basic API structure with logging and error handling.
"""

import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def hello_claude():
    """Return a greeting."""
    try:
        logger.info("hello_claude called")
        return "Hello, Claude!"
    except Exception as e:
        logger.error(f"Error: {e}")
        return None

if __name__ == "__main__":
    result = hello_claude()
    if result:
        print(result)