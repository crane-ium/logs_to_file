"""
Unit testing
"""

import unittest
from tests import exception_test, logging_test

MODULES = [

]

class TestMain(unittest.TestCase):
    """
    Runs all tests
    """
    for module in MODULES: #Run through each package and create test suites for each package, then run them.
        test_suite = unittest.TestLoader().loadTestsFromModule(module) #The suite is the collection of tested modules
        unittest.TextTestRunner(verbosity=3).run(suite)

