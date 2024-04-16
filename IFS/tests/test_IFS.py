"""
Unit and regression test for the IFS package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import IFS


def test_IFS_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "IFS" in sys.modules
