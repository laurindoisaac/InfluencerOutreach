# test_influenceroutreach.py
"""
Tests for InfluencerOutreach module.
"""

import unittest
from influenceroutreach import InfluencerOutreach

class TestInfluencerOutreach(unittest.TestCase):
    """Test cases for InfluencerOutreach class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfluencerOutreach()
        self.assertIsInstance(instance, InfluencerOutreach)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfluencerOutreach()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
