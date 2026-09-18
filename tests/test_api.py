"""Tests for the API module."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from claude_learning.api import hello_claude, greet_user


def test_hello_claude():
    """hello_claude should return the standard greeting."""
    assert hello_claude() == "Hello, Claude!"


def test_greet_user_with_name():
    """greet_user should personalize the greeting with a valid name."""
    assert greet_user("Alice") == "Hello, Alice! Welcome to Claude Learning."


def test_greet_user_empty_name():
    """greet_user should fall back to a generic greeting for empty input."""
    assert greet_user("") == "Hello, stranger! Welcome to Claude Learning."


def test_greet_user_whitespace_name():
    """greet_user should treat whitespace-only input as empty."""
    assert greet_user("   ") == "Hello, stranger! Welcome to Claude Learning."