# test_cachelayer.py
"""
Tests for CacheLayer module.
"""

import unittest
from cachelayer import CacheLayer

class TestCacheLayer(unittest.TestCase):
    """Test cases for CacheLayer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CacheLayer()
        self.assertIsInstance(instance, CacheLayer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CacheLayer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
