#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Database operations functions.

Testing common Database operations. Starting with www.faunadb.com.
"""

import logging

import pytest

from faunadb.client import FaunaClient
from faunadb.objects import Ref

from broccolini.common import get_authentication_values
from broccolini.database_operations import DataBaseOperations


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestDatabaseOperations:
    """Test Database Operation Functions."""

    @staticmethod
    @pytest.mark.dependency(name="test_login_to_fauna")
    def test_fauna_get_connection(return_database_settings):  # pragma: no cover
        """Test login to fauna.

        input: client_token
        input_type: str
        output_type: FaunaClient
        output example: <faunadb.client.FaunaClient object at 0x000002439xxxxx>
        """

        client_token = get_authentication_values(
            return_database_settings["fauna_path_srv"]
        )

        result = DataBaseOperations(client_token=client_token).fauna_get_connection()
        expected = "faunadb.client.FaunaClient"
        expected_type = FaunaClient
        assert expected in str(result)
        assert isinstance(result, expected_type)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_create_collection(return_database_settings):  # pragma: no cover
        """Test create collection."""
        client_token = get_authentication_values(
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
    def test_fauna_create_index(return_database_settings):  # pragma: no cover
        """Test create index."""
        client_token = get_authentication_values(
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
        expected_type = str
        assert isinstance(result, expected_type)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_create_document(return_database_settings):  # pragma: no cover
        """Test create document."""
        client_token = get_authentication_values(
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
    def test_fauna_paginate_database(return_database_settings):  # pragma: no cover
        """Test Fauna paginate database."""
        client_token = get_authentication_values(
            return_database_settings["fauna_secret_path_admin"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_paginate_database()
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_read_database(return_database_settings):  # pragma: no cover
        """Test Fauna DB read.

        needs admin key since working on all database_operations
        """
        client_token = get_authentication_values(
            return_database_settings["fauna_secret_path_admin"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_read_database()
        expected_type = dict
        assert isinstance(result, expected_type)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_delete_document_mock(
        return_database_settings, _mocked_fauna
    ):  # pragma: no cover
        """Test delete document.

        fauna_document_name
        """
        client_token = get_authentication_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_delete_document(
            fauna_collection_name=return_database_settings["fauna_collection_name"],
        )

        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_delete_collection_mock(
        return_database_settings, _mocked_fauna
    ):  # pragma: no cover
        """Test delete collection using mock."""
        client_token = get_authentication_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_delete_collection(
            mock_fauna_delete_collection=_mocked_fauna["mock_fauna_delete_collection"],
        )
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_query_index_with_data(return_database_settings):  # pragma: no cover
        """Test query index with data from conftest."""
        client_token = get_authentication_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(
            client_token=client_token
        ).fauna_query_index_with_data(
            fauna_index_name=return_database_settings["fauna_index_name"],
        )
        expected = "Ref(id="
        expected_type = Ref
        assert isinstance(result, expected_type)
        assert expected in str(result)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_query(return_database_settings):  # pragma: no cover
        """Test query index with data from conftest.

        Need to manually create the database information for the tests to pass

           Map(
                      [
        [ "101", { name: "Name_conftest_101", extra: "Description conftest 101." } ],
        [ "102", { name: "Name_conftest_102", extra: "Description conftest 102." }],
        [ "103", { name: "Name_conftest_103", extra: "Description conftest 103." } ]
                      ],
                      Lambda(
                        ["id", "data"],
        Create(Ref(Collection("Conftest_db_items"), Var("id")), { data: Var("data") })
                      )
                    )

        """
        client_token = get_authentication_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_query(
            fauna_collection_name=return_database_settings["fauna_new_collection_name"],
            fauna_index_name=return_database_settings["fauna_new_index_name"],
            fauna_search_term=return_database_settings["fauna_new_search_term"],
        )
        expected = return_database_settings["fauna_reference_id"]

        expected_type = dict
        assert expected in str(result)
        assert isinstance(result, expected_type)
        assert result["data"][0].id() == expected

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_query_with_ref_id(return_database_settings):  # pragma: no cover
        """Test updated fauna query method."""
        client_token = get_authentication_values(
            return_database_settings["fauna_path_srv"]
        )
        result = DataBaseOperations(client_token=client_token).fauna_query_with_ref_id(
            fauna_collection_name=return_database_settings["fauna_new_collection_name"],
            ref_id=return_database_settings["fauna_reference_id"],
        )
        expected = return_database_settings["fauna_new_search_term"]
        expected_type = dict
        assert isinstance(result, expected_type)
        assert expected == result["data"]["name"]

    @staticmethod
    def test_fauna_query_with_name(return_database_settings):
        """Test gets id when given name."""
        fauna_db_server_key: str = get_authentication_values(
            secret_path=return_database_settings["fauna_path_srv"],
        )
        result = DataBaseOperations(
            client_token=fauna_db_server_key
        ).fauna_query_with_name(
            fauna_index_name=return_database_settings["fauna_new_index_name"],
            name=return_database_settings["fauna_new_search_term"],
        )
        expected = return_database_settings["fauna_new_search_term"]
        expected_type = dict
        assert isinstance(result, expected_type)
        assert expected in str(result)

    @staticmethod
    def test_fauna_create_data_using_jinja(return_database_settings):
        """Test gets id when given name."""
        fauna_db_server_key: str = get_authentication_values(
            secret_path=return_database_settings["fauna_path_srv"],
        )
        result = DataBaseOperations(
            client_token=fauna_db_server_key
        ).fauna_create_data_using_jinja(
            fauna_collection_name=return_database_settings["fauna_collection_name"],
        )
        expected = return_database_settings["fauna_collection_name"]
        expected_type = str
        assert isinstance(result, expected_type)
        assert expected in str(result)


@pytest.fixture
def _mocked_fauna(mocker):  # pragma: no cover
    """Use for mocking variables."""
    mock_fauna_delete_collection = mocker.patch.object(
        DataBaseOperations, "fauna_delete_collection", autospec=True
    )
    mock_fauna_delete_document = mocker.patch.object(
        DataBaseOperations, "fauna_delete_document", autospec=True
    )
    mock_fauna_delete_collection.return_value = True
    mock_fauna_delete_document.return_value = True

    return dict(
        mock_fauna_delete_collection=mock_fauna_delete_collection,
        mock_fauna_delete_document=mock_fauna_delete_document,
    )
