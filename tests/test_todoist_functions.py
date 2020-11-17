#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Presentation functions.

Starting with jinja templates.
"""

import logging

import pytest

from todoist import TodoistAPI

from broccolini.common import get_authentication_values
from broccolini.todoist_operations import TodoIstOperations


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestTodoIstOperations:
    """Test Todoist Functions."""

    @staticmethod
    @pytest.mark.dependency(name="test_login_to_todoist")
    def test_todoist_get_connection(return_data_dict):
        """Connect to todoist test."""
        todoist_api_token = get_authentication_values(
            secret_path=return_data_dict["todoist_secret_path"]
        )

        result = TodoIstOperations().todoist_get_connection(
            todoist_api_token=todoist_api_token,
        )
        expected_type = TodoistAPI
        assert isinstance(result, expected_type)

    @staticmethod
    def test_todoist_list_items(return_data_dict):
        """Test todoist list tasks."""
        todoist_api_token = get_authentication_values(
            secret_path=return_data_dict["todoist_secret_path"]
        )
        result = TodoIstOperations().list_items(
            todoist_api_token=todoist_api_token,
        )
        expected_type = list
        assert isinstance(result, expected_type)

    @staticmethod
    def test_todoist_list_projects(return_data_dict):
        """Test todoist list projects."""
        todoist_api_token = get_authentication_values(
            secret_path=return_data_dict["todoist_secret_path"]
        )
        result = TodoIstOperations().list_projects(
            todoist_api_token=todoist_api_token,
        )
        expected_type = list
        assert isinstance(result, expected_type)

    @staticmethod
    def test_filter_items(return_data_dict):
        """Test todoist filter items."""
        todoist_api_token = get_authentication_values(
            secret_path=return_data_dict["todoist_secret_path"]
        )

        result = TodoIstOperations().filter_items(
            todoist_api_token=todoist_api_token,
        )
        expected_type = list
        assert isinstance(result, expected_type)
