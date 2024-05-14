import unittest, math
import numpy as np

from src.interpolation import vandermonde, lagrangian, newton

class InterpolationTest(unittest.TestCase):
    def test_vandermonde(self):
        
