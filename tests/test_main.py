"""
Test module for main.py.

Contains unit tests for the main module functionality.
"""

import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from main import hello_world


def test_hello_world():
    """Test the hello_world function."""
    result = hello_world()
    assert result == "Hello, World!"


def test_hello_world_type():
    """Test that hello_world returns a string."""
    result = hello_world()
    assert isinstance(result, str)


if __name__ == "__main__":
    pytest.main([__file__])