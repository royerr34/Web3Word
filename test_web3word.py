# test_web3word.py
"""
Tests for Web3Word module.
"""

import unittest
from web3word import Web3Word

class TestWeb3Word(unittest.TestCase):
    """Test cases for Web3Word class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Word()
        self.assertIsInstance(instance, Web3Word)

    def test_run_method(self):
        """Test the run method."""
        instance = Web3Word()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
