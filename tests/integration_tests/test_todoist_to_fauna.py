#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integration test: take todoist data and put into fauna

input: todoist data
processing: generate data into a dictionary
put this data into fauna with a timestamp
"""

import datetime
import logging

import pytest

# from broccolini.authentication_functions import VaultFunctions
from broccolini.database_operations import DataBaseOperations
from broccolini.todoist_operations import TodoIstOperations


FAUNA_SECRET_PATH = "python_rising/dev/todoist_data/TODOIST_API_TOKEN"
SECRET_PATH = "python_rising/dev/todoist_data/TODOIST_API_TOKEN"
FAUNA_DATABASE_NAME = "todoist_archives"
TODAYS_DATE = (datetime.date(2019, 10, 20)).strftime("%Y%m%d")
FAUNA_COLLECTION_NAME = "todoist_data_nov_2020"

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestIntegrationTodoistFauna:
    """Test the integration from files to fauna database."""

    # @classmethod
    # def get_test_values(cls, secret_path):
    #     """Build values needed for the test."""
    #     try:
    #         todoist_secret_key = VaultFunctions().query_vault_data(
    #             vault_url="VAULT_URL",
    #             vault_token="VAULT_TOKEN",
    #             secret_path=secret_path,
    #         )

    #         return todoist_secret_key["data"]["data"]["_key"]
    #     except KeyError as _error:  # pragma: no cover
    #         raise ValueError("Missing environment variables") from _error

    @staticmethod
    @pytest.mark.skip(reason="integration testing")
    def test_integration_todoist_to_fauna(return_database_settings):
        """Test the integration from todoist to fauna."""

        todoist_api_token = TestIntegrationTodoistFauna.get_test_values(
            SECRET_PATH,
        )
        todoist_items = TodoIstOperations().list_items(
            todoist_api_token=todoist_api_token,
        )
        list_of_items = []
        # print(TODAYS_DATE)
        for each in todoist_items:
            list_of_items.append(len(each["content"]))
        records_to_add = {"data": {TODAYS_DATE: list_of_items}}

        fauna_api_token = TestIntegrationTodoistFauna.get_test_values(
            return_database_settings["fauna_path_srv"],
        )
        # print(len(fauna_api_token))
        DataBaseOperations(client_token=fauna_api_token).fauna_create_document(
            fauna_collection_name=FAUNA_COLLECTION_NAME,
            fauna_document_data=records_to_add,
        )
        # print(result_of_db_add)
