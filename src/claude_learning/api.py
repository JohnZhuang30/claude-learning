"""
Claude Learning API module.
This module demonstrates basic API structure with logging.
"""

import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def hello_claude():
    """Return a greeting."""
    logger.info("hello_claude called")
    return "Hello, Claude!"

if __name__ == "__main__":
    print(hello_claude())