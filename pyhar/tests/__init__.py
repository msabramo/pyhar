#!/usr/bin/env python
import unittest
import doctest

def all_tests_suite():
    suite = unittest.TestLoader().loadTestsFromNames([
        'pyhar.tests.test_decode',
    ])
    
    return suite

if __name__ == '__main__':
    import os
    import sys
 
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    
    runner = unittest.TextTestRunner()
    suite = all_tests_suite()
    runner.run(suite)