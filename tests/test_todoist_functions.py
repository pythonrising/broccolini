#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Presentation functions.

Starting with jinja templates.
"""

import logging

import pytest

from todoist import TodoistAPI

from broccolini.authentication_functions import VaultFunctions
from broccolini.todoist_operations import TodoIstOperations


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestTodoIstOperations:
    """Test Todoist Functions."""

    @classmethod
    def get_test_values(cls, secret_path):
        """Build values for the test."""
        try:
            todoist_secret_key = VaultFunctions().query_vault_data(
                vault_url="VAULT_URL",
                vault_token="VAULT_TOKEN",
                secret_path=secret_path,
            )
            return todoist_secret_key["data"]["data"]["_key"]
        except KeyError as _error:  # pragma: no cover
            raise ValueError("Missing environment variables") from _error

    @staticmethod
    @pytest.mark.dependency(name="test_login_to_todoist")
    def test_todoist_get_connection(return_data_dict):
        """Connect to todoist test."""
        todoist_api_token = TestTodoIstOperations.get_test_values(
            secret_path=return_data_dict["todoist_secret_path"]
        )

        result = TodoIstOperations().todoist_get_connection(
            todoist_api_token=todoist_api_token,
        )
        # print(result)
        expected_type = TodoistAPI
        assert isinstance(result, expected_type)

    @staticmethod
    def test_todoist_list_items(return_data_dict):
        """Test todoist list tasks."""
        todoist_api_token = TestTodoIstOperations.get_test_values(
            secret_path=return_data_dict["todoist_secret_path"]
        )

        result = TodoIstOperations().list_all_items(
            todoist_api_token=todoist_api_token,
        )
        expected_type = list
        assert isinstance(result, expected_type)


# @staticmethod
#     @pytest.mark.dependency(depends=["test_login_to_todoist"])
#     def test_todoist_list_tasks():  # pragma: no cover
#
