"""DataBaseOperation functions.

DataBase operations.
"""
import csv
import logging

from typing import Any, Dict, List

import faunadb

from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.errors import BadRequest, NotFound, UnexpectedError
from faunadb.objects import Ref

from broccolini.presentation_functions import PresentationOperations


# from typing import Union


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

    # def fauna_create_collection(self, **kwargs: str) -> bool:
    #     """Create collection."""
    #     client = self.fauna_get_connection()
    #     fauna_collection_name: str = kwargs["fauna_collection_name"]
    #     try:
    #         client.query(q.create_collection({"name": fauna_collection_name}))
    #         return True
    #     except (Exception) as _error:  # pragma: no cover
    #         print(_error)
    #         raise ValueError("Fauna error.") from _error

    # def fauna_create_index(self, **kwargs: str) -> bool:
    #     """Create index."""
    #     client = self.fauna_get_connection()
    #     fauna_collection_name: str = kwargs["fauna_collection_name"]
    #     fauna_index_name: str = kwargs["fauna_index_name"]
    #     try:
    #         client.query(
    #             q.create_index(
    #                 {
    #                     "name": fauna_index_name,
    #                     "source": q.collection(fauna_collection_name),
    #                     "values": [{"field": ["data", "name"]}],
    #                 }
    #             )
    #         )
    #         return True
    #     except (BadRequest, Exception) as _error:  # pragma: no cover
    #         raise ValueError("Fauna error.") from _error

    # def fauna_query_with_ref_id(self, **kwargs: str) -> Dict[Dict[str, str], str]:
    #     """Query fauna when given ref id."""
    #     client = self.fauna_get_connection()
    #     fauna_collection_name: str = kwargs["fauna_collection_name"]
    #     ref_id: str = kwargs["ref_id"]
    #     try:
    #         result = client.query(
    #             q.get(q.ref(q.collection(fauna_collection_name), ref_id))
    #         )
    #         return result
    #     except (Exception) as _error:  # pragma: no cover
    #         raise ValueError("Fauna error.") from _error

    def fauna_query_index(self, **kwargs: str) -> Dict[str, str]:
        """Query index."""
        client = self.fauna_get_connection()
        fauna_index_name: str = kwargs["fauna_index_name"]
        try:
            index_list: Dict[str, str] = client.query(q.get(q.index(fauna_index_name)))
            return index_list
        except (Exception) as _error:  # pragma: no cover
            # print(_error)
            raise ValueError("Fauna error.") from _error

    def fauna_create_document(self, **kwargs: str) -> bool:
        """Add document."""
        client: FaunaClient = self.fauna_get_connection()
        fauna_collection_name: str = kwargs["fauna_collection_name"]
        fauna_document_data: str = kwargs["fauna_document_data"]
        try:
            client.query(
                q.create(q.collection(fauna_collection_name), fauna_document_data)
            )
            #

        except UnexpectedError as _error:  # pragma: no cover
            raise ValueError("Unexpected error with data load.") from _error

        except BadRequest as _error:  # pragma: no cover
            # except (BadRequest, Exception) as _error:  # pragma: no cover
            # for debugging only print statement
            print(f"data load error\n{_error}")
            # raise ValueError("BadRequest.") from _error
        except Exception as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

        return True

    def fauna_paginate_database(self) -> bool:
        """Fauna paginate database.

        Requires admin key to paginate databases instead of just server database.
        """
        client = self.fauna_get_connection()
        try:
            client.query(q.paginate(Ref("databases")))
            return True
        except (BadRequest, Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

    def fauna_read_database(self) -> FaunaClient:
        """Read from fauna database."""
        client = self.fauna_get_connection()
        try:
            return client.query(q.paginate(q.indexes()))
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

    def fauna_delete_document(self, **kwargs: str) -> bool:  # pragma: no cover
        """Delete document.

        fauna_collection_name(str) - collection name created earlier
        fauna_document_ref(str) - reference document id
        Query to get fauna_document_ref
        serverClient.query(q.delete(q.ref(q.collection("posts"), "192903209792045568")))
        output (bool) success if deleted documetn
        """
        client = self.fauna_get_connection()
        fauna_collection_name: str = kwargs["fauna_collection_name"]
        fauna_document_ref: str = kwargs["fauna_document_ref"]
        try:
            client.query(
                q.delete(q.ref(q.collection(fauna_collection_name), fauna_document_ref))
            )
            return True
        except NotFound as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

    def fauna_query_index_with_data(
        self, **kwargs: str
    ) -> Dict[Dict[str, str], str]:  # pragma: no cover
        """Query index when given the index name."""
        client = self.fauna_get_connection()
        fauna_index_name: str = kwargs["fauna_index_name"]
        try:
            reference_id: faunadb = client.query(q.get(q.match(fauna_index_name)))[
                "ref"
            ]
            return reference_id

        except (Exception) as _error:  # pragma: no cover
            print(_error)
            raise ValueError("Fauna error.") from _error

    def fauna_delete_index(self, **kwargs: str) -> bool:  # pragma: no cover
        """Delete index."""
        client = self.fauna_get_connection()
        fauna_index_name: str = kwargs["fauna_index_name"]
        try:
            client.query(q.delete(q.index(fauna_index_name)))
            return True
        except (Exception) as _error:  # pragma: no cover
            print(_error)
            raise ValueError("Fauna error.") from _error

    def fauna_query_collection(self, **kwargs: str) -> bool:  # pragma: no cover
        """Query collection."""
        client: FaunaClient = self.fauna_get_connection()
        fauna_collection_name: str = kwargs["fauna_collection_name"]
        try:
            client.query(q.get(q.collection(fauna_collection_name)))
            return True
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error. - fauna_query_collection") from _error

    def fauna_delete_collection(self, **kwargs: str) -> bool:  # pragma: no cover
        """Delete collection."""
        client = self.fauna_get_connection()
        fauna_collection_name: str = kwargs["fauna_collection_name"]
        try:
            client.query(q.delete(q.collection(fauna_collection_name)))
            return True
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

    def fauna_query(self, **kwargs: str) -> Any:
        """Query data updated."""
        client = self.fauna_get_connection()
        fauna_index_name: str = kwargs["fauna_index_name"]
        fauna_search_term: str = kwargs["fauna_search_term"]
        try:
            result = client.query(
                q.paginate(q.match(q.index(fauna_index_name), fauna_search_term))
            )
            # print(type(result["data"]))
            # print(result)
            return result
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

    # def fauna_query_by_reference_id(self, **kwargs: str) -> Dict[Dict[str, str], str]:
    #     """Query data using reference id ."""
    #     client = self.fauna_get_connection()
    #     fauna_collection_name: str = kwargs["fauna_collection_name"]
    #     fauna_reference_id: str = kwargs["fauna_reference_id"]
    #     try:
    #         result = client.query(
    #             q.get(q.ref(q.collection(fauna_collection_name), fauna_reference_id))
    #         )
    #         return result
    #     except BadRequest as _error:  # pragma: no cover
    #         raise ValueError("Fauna error.") from _error

    # def fauna_query_with_name(self, **kwargs: str) -> Dict[Dict[str, str], Any]:
    #     """Query fauna when given name."""
    #     client = self.fauna_get_connection()
    #     fauna_index_name: str = kwargs["fauna_index_name"]
    #     name: str = kwargs["name"]
    #     try:
    #         result = client.query(q.get(q.match(q.index(fauna_index_name), name)))
    #         return result
    #     except (Exception) as _error:  # pragma: no cover
    #         raise ValueError("Fauna error.") from _error

    @staticmethod
    def fauna_create_data_using_jinja(**kwargs: str) -> Any:
        """Create a bulk upload file using a jinja template.

        input: records_to_create: Dict[str, str]
        side_effect: jinja_template file type: io
        returns: success: bool
        """
        success = False
        fauna_collection_name: str = kwargs["fauna_collection_name"]
        fauna_input_data_csv: str = kwargs["fauna_input_data_csv"]
        output_file: str = kwargs["output_file"]
        input_template_name: str = kwargs["input_template_name"]
        input_list: List[Dict[str, str]] = []

        with open(fauna_input_data_csv, "rt") as file_handle:
            reader = csv.DictReader(file_handle)
            for row in reader:
                input_list.append(row)

        input_dict = dict(
            input_list=input_list,
            fauna_collection_name=fauna_collection_name,
        )

        result = PresentationOperations().prepare_template_with_pathlib(
            input_dictionary=input_dict,
            input_template_name=input_template_name,
            autoescape_formats=["html", "xml"],
        )

        with open(output_file, "w") as file_handle:
            file_handle.write(result)
            success = True

        return success

    def fauna_list_all_using_lambda(self, **kwargs: str) -> Any:
        """Follow example from serverless to list using lambda(javascript)

        __credits__ = https://github.com/serverless/examples/blob/master/
        aws-python-rest-api-with-faunadb/todos/list.py
        """
        fauna_index_name: str = kwargs["fauna_index_name"]
        # fauna_index_name: str = "all_Items"
        client = self.fauna_get_connection()
        # all_todos = q.index("all_Items")
        results = client.query(
            q.map_expr(lambda ref: q.get(ref), q.paginate(q.match(fauna_index_name)))
        )

        return results
