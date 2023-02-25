#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:40:57 2023

@author: khusboopatel
"""

import unittest

from GithubAPI import gitHubFunction

class TestGitHubFunction(unittest.TestCase):
    def testValidUserInput1(self):
        self.assertEqual(gitHubFunction(1), 'The input username is not valid')

    def testValidUserInput2(self):
        self.assertEqual(gitHubFunction(10), 'The input username is not valid')
        self.assertEqual(gitHubFunction(3012), 'The input username is not valid')
        self.assertEqual(gitHubFunction([1,2,3]), 'The input username is not valid')
    
    def testValidUserInput3(self):
        #self.assertEqual(gitHubFunction("asdasdas"), 'This account does not have any repositories')
        self.assertFalse(gitHubFunction("/.123/.123"), 'This account does not have any repositories')

    def testValidUserInput4(self):
        self.assertEqual(gitHubFunction(""), 'You must provide a username')
        self.assertEqual(gitHubFunction([]), 'You must provide a username')

if __name__ == '__main__':
    print('Running Unit Tests')
    unittest.main()
