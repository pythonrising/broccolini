"""DataBaseOperation functions.

DataBase operations.
"""
import logging

# from typing import Any

from faunadb import query as q
from faunadb.client import FaunaClient

from faunadb.errors import BadRequest

# from faunadb.objects import Ref

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class DataBaseOperations:
    """DataBase Operation Functions.

    Authentication and secrets from Hashicorp Vault.
    input: client_token - from vault data
    input_type: str
    """

    def __init__(self, client_token: str) -> None:
        """Init class - vars are called in the function as needed."""
        self.client_token = client_token

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    def fauna_get_connection(self) -> FaunaClient:
        """Get Fauna Connection.

        input: client_token from class
        input_type: str
        output: fauna database connection
        output_type: FaunaClient
        """
        try:
            client = FaunaClient(secret=self.client_token)
            return client
        except Exception as _errorinfo:  # pragma: no cover
            raise ValueError("error connecting") from _errorinfo

    def fauna_create_collection(self, **kwargs: str) -> bool:
        """Create collection."""
        client = self.fauna_get_connection()
        fauna_collection_name: str = kwargs["fauna_collection_name"]
        try:
            client.query(q.create_collection({"name": fauna_collection_name}))
            return True
        except (Exception) as _error:  # pragma: no cover
            print(_error)
            raise ValueError("Fauna error.") from _error

    def fauna_create_index(self, **kwargs: str) -> bool:
        """Create index."""
        client = self.fauna_get_connection()
        fauna_collection_name: str = kwargs["fauna_collection_name"]
        fauna_index_name: str = kwargs["fauna_index_name"]
        try:
            client.query(
                q.create_index(
                    {
                        "name": fauna_index_name,
                        "source": q.collection(fauna_collection_name),
                        "values": [{"field": ["data", "name"]}],
                    }
                )
            )
            return True
        except (BadRequest, Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

    def fauna_query_index(self, **kwargs: str) -> bool:
        """query index."""
        client = self.fauna_get_connection()
        # _fauna_collection_name: str = kwargs["fauna_collection_name"]
        fauna_index_name: str = kwargs["fauna_index_name"]
        try:
            client.query(q.get(q.index(fauna_index_name)))
            return True
        except (Exception) as _error:  # pragma: no cover
            print(_error)
            raise ValueError("Fauna error.") from _error

    @staticmethod
    def fauna_create_document():
        """Add document."""
        return True

    @staticmethod
    def fauna_paginate_database():
        """Fauna paginate database."""
        return True

    @staticmethod
    def fauna_read_database():
        """Read from fauna database."""
        return True

    @staticmethod
    def fauna_delete_document() -> bool:
        """Delete document."""
        return True

    def fauna_delete_index(self, **kwargs: str) -> bool:
        """Delete index."""
        client = self.fauna_get_connection()
        _fauna_collection_name: str = kwargs["fauna_collection_name"]
        fauna_index_name: str = kwargs["fauna_index_name"]
        try:
            client.query(
                q.delete(q.index(
                    fauna_index_name
                    )
                )
            )
            return True
        except (Exception) as _error:  # pragma: no cover
            print(_error)
            raise ValueError("Fauna error.") from _error

    def fauna_query_collection(self, **kwargs) -> bool:
        """Query collection."""
        client = self.fauna_get_connection()
        fauna_collection_name: str = kwargs["fauna_collection_name"]
        try:
            client.query(q.get(q.collection(fauna_collection_name)))
            return True
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

    def fauna_delete_collection(self, **kwargs) -> bool:
        """Delete collection."""
        client = self.fauna_get_connection()
        fauna_collection_name: str = kwargs["fauna_collection_name"]
        try:
            client.query(q.delete(q.collection(fauna_collection_name)))
            return True
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error
