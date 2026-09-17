"""
Claude Learning API module.
This module demonstrates basic API structure with error handling.
"""

def hello_claude():
    """Return a greeting."""
    try:
        return "Hello, Claude!"
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    result = hello_claude()
    if result:
        print(result)