'''
Created on Aug 19, 2018
@author: zhaosong
'''

import unittest

class Test2(unittest.TestCase):
    '''
    This class demo how to setup test case and run test use python unittest module.
    '''

    # This method will be executed only once for this test case class. 
    # It will execute before all test methods. Must decorated with @classmethod.
    @classmethod
    def setUpClass(cls):
        print("setUpClass execute. ")
        
    # Similar with setupClass method, it will be executed after all test method run.    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass execute. ") 
        
    # This method will be executed before each test function.    
    def setUp(self):
        unittest.TestCase.setUp(self)
        print("setUp method execute. ")

    # This method will be executed after each test function.     
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        print("tearDown method execute. ")

    def test_function_one(self):
        print("test_function_one execute. 2")
        self.assertEqual(1, 2, "test_function_one.")
        
    def test_function_two(self):
        print("test_function_two execute. 2")
        self.assertNotEqual(1, 2, "test_function_two.")

    