#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:40:57 2023

@author: khusboopatel
"""

import requests
import unittest
from unittest.mock import patch, MagicMock
from GithubAPI import gitHubFunction

class TestGitHubFunction(unittest.TestCase):

    # Test that an empty or None input returns an error message
    def test_empty_input(self):
        result = gitHubFunction("")
        self.assertEqual(result, "You must provide a username")

        result = gitHubFunction([])
        self.assertEqual(result, "You must provide a username")

    # Test that a non-string input returns an error message
    def test_invalid_input(self):
        result = gitHubFunction(123)
        self.assertEqual(result, "The input username is not valid")

        result = gitHubFunction({"username": "test"})
        self.assertEqual(result, "The input username is not valid")

    # Test that an account with no repositories returns an error message
    @patch('requests.get')
    def test_no_repositories(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        result = gitHubFunction("testuser")
        self.assertEqual(result, "This account does not have any repositories")

    # Test that the function returns the expected result for a valid input
    @patch('requests.get')
    def test_valid_input(self, mock_get):
        mock_response1 = MagicMock()
        mock_response1.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get.side_effect = [mock_response1, mock_response1]

        mock_response2 = MagicMock()
        mock_response2.json.return_value = [{"sha": "abc123"}, {"sha": "def456"}]
        mock_get.return_value = mock_response2

        result = gitHubFunction("testuser")
        expected_result = "Repo:repo1 Number of commits: 2\nRepo:repo2 Number of commits: 2\n"
        self.assertEqual(result, expected_result)

    # Test that the function returns an error message when the API rate limit is exceeded
    @patch('os.system')
    @patch('requests.get')
    def test_api_rate_limit(self, mock_get, mock_os):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
        mock_get.return_value = mock_response

        mock_os.return_value = ""

        result = gitHubFunction("testuser")
        self.assertTrue("YOU HAVE EXCEEDED YOUR API RATE LIMIT" in result)

