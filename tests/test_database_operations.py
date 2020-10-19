#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Database operations functions.

Testing common Database operations. Starting with www.faunadb.com.
"""

import logging

import pytest

# from faunadb.client import FaunaClient, client
from faunadb.client import FaunaClient

from broccolini.authentication_functions import VaultFunctions
from broccolini.database_operations import DataBaseOperations


# import uuid


# import mock
# from pytest_mock import mocker


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestDatabaseOperations:
    """Test Database Operation Functions."""

    @classmethod
    def get_test_values(cls, secret_path):
        """Build values for the test."""
        try:
            fauna_secret_key = VaultFunctions().query_vault_data(
                vault_url="VAULT_URL",
                vault_token="VAULT_TOKEN",
                secret_path=secret_path,
            )
            return fauna_secret_key["data"]["data"]["_key"]
        except KeyError as _error:  # pragma: no cover
            raise ValueError("Missing environment variables") from _error

    @staticmethod
    @pytest.mark.dependency(name="test_login_to_fauna")
    def test_fauna_get_connection(return_database_settings):
        """Test login to fauna.

        input: client_token
        input_type: str
        output_type: FaunaClient
        output example: <faunadb.client.FaunaClient object at 0x000002439xxxxx>
        """
        client_token = TestDatabaseOperations.get_test_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_get_connection()
        expected = "faunadb.client.FaunaClient"
        expected_type = FaunaClient
        assert expected in str(result)
        assert isinstance(result, expected_type)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_create_collection(return_database_settings):
        """Test create collection."""
        client_token = TestDatabaseOperations.get_test_values(
            return_database_settings["fauna_path_srv"]
        )
        this = DataBaseOperations(client_token=client_token)
        try:
            this.fauna_query_collection(
                fauna_collection_name=return_database_settings["fauna_collection_name"]
            )
            return True
        except ValueError:
            result = this.fauna_create_collection(
                fauna_collection_name=return_database_settings["fauna_collection_name"],
            )
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_create_index(return_database_settings):
        """Test create index."""
        client_token = TestDatabaseOperations.get_test_values(
            return_database_settings["fauna_path_srv"]
        )
        this = DataBaseOperations(client_token=client_token)
        try:
            this.fauna_query_index(
                fauna_collection_name=return_database_settings["fauna_collection_name"],
                fauna_index_name=return_database_settings["fauna_index_name"],
            )
            return True
        except ValueError:
            result = this.fauna_create_index(
                fauna_collection_name=return_database_settings["fauna_collection_name"],
                fauna_index_name=return_database_settings["fauna_index_name"],
            )
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_create_document(return_database_settings):
        """Test create document."""
        client_token = TestDatabaseOperations.get_test_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_create_document(
            fauna_collection_name=return_database_settings["fauna_collection_name"],
            fauna_document_data=return_database_settings["fauna_document_data"],
        )
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_paginate_database(return_database_settings):
        """Test Fauna paginate database."""
        client_token = TestDatabaseOperations.get_test_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_paginate_database()
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_read_database(return_database_settings):
        """Test Fauna DB read."""
        client_token = TestDatabaseOperations.get_test_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_read_database()
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_delete_document(return_database_settings):
        """Test delete document."""
        client_token = TestDatabaseOperations.get_test_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_delete_document()
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_delete_collection_mock(return_database_settings, _mocked_fauna):
        """Test delete collection using mock."""
        client_token = TestDatabaseOperations.get_test_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_delete_collection()
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result


@pytest.fixture
def _mocked_fauna(mocker):
    """Use for mocking variables."""
    mock_fauna = mocker.patch.object(
        DataBaseOperations, "fauna_delete_collection", autospec=True
    )
    mock_fauna.return_value = True
    return mock_fauna
