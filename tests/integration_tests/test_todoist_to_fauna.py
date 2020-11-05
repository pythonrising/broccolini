#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integration test: take todoist data and put into fauna

input: todoist data
processing: generate data into a dictionary
put this data into fauna with a timestamp
"""

import logging

from broccolini.authentication_functions import VaultFunctions
from broccolini.todoist_operations import TodoIstOperations


SECRET_PATH = "python_rising/dev/todoist_data/TODOIST_API_TOKEN"

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestIntegrationTodoistFauna:
    """Test the integration from files to fauna database."""

    @classmethod
    def get_test_values(cls, secret_path):
        """Build values needed for the test."""
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
    def test_integration_todoist_to_fauna():
        """XXXa."""
        todoist_api_token = TestIntegrationTodoistFauna.get_test_values(
            SECRET_PATH,
        )
        result = TodoIstOperations().list_projects(
            todoist_api_token=todoist_api_token,
        )
        print(result)

        expected_type = list
        assert isinstance(result, expected_type)

        # DataBaseOperations(client_token=client_token).fauna_create_document(
        #         fauna_collection_name=FAUNA_COLLECTION_NAME,
        #         fauna_document_data=records_to_add,
        #     )


# class TestIntegrationTodoistToFauna:
#     """Test the integration from files to fauna database."""

#     @classmethod
#     def get_test_values(cls, secret_path):
#         """Build values needed for the test."""
#         try:
#             fauna_secret_key = VaultFunctions().query_vault_data(
#                 vault_url="VAULT_URL",
#                 vault_token="VAULT_TOKEN",
#                 secret_path=secret_path,
#             )
#             return fauna_secret_key["data"]["data"]["_key"]
#         except KeyError as _error:  # pragma: no cover

#             raise ValueError("Missing environment variables") from _error

#     def test_integration_todoist_data_to_fauna():
#         """Create document from data created in other function."""
#         # client_token = TestIntegrationTodoistToFauna.get_test_values(
#         #     secret_path=SECRET_PATH,
#         #     )
#         try:
#             client_token = TestIntegrationTodoistToFauna.get_test_values(
#             secret_path=SECRET_PATH,
#             )
#             print(len(client_token))

#         except Exception as _error:  # pragma: no cover
#             print(f'error is {_error}')

# # def test_integration_sample_training_data_to_fauna(
# #         return_database_settings, test_get_files_from_folder
# #     ):
# #         """Create document using data created in other function."""
# #         client_token = TestIntegrationFileToFauna.get_test_values(
# #             return_database_settings["fauna_path_srv"],
# #         )

#         # client_token = TestIntegrationTodoistToFauna.get_test_values(
#         #     secret_path=SECRET_PATH,
#         # )
#         # print(len(client_token))
#         # TodoIstOperations(client_token=client_token).list_projects()

# # FAUNA_DATABASE_NAME = 'todoist_archives'

# # def vault_login(secret_path):
# #     """login to vault

# #     Args:
# #         secret_path ([str]): path in vault

# #     Raises:
# #         ValueError: error if vault issue

# #     Returns:
# #         vault_path: path to use from vault
# #         result = VaultFunctions.get_vault_credentials(
# #             vault_url="VAULT_URL", vault_token="VAULT_TOKEN"
# #         )
# #     """
# #     try:
# #         secret_key = VaultFunctions().query_vault_data(
# #             vault_url="VAULT_URL",
# #             vault_token="VAULT_TOKEN",
# #             secret_path=secret_path,
# #         )
# #         return secret_key["data"]["data"]["_key"]
# #     except KeyError as _error:  # pragma: no cover
# #         raise ValueError("Missing environment variables") from _error

# # # @pytest.mark.skip(reason="integration testing")
# # def test_integrations_get_todoist_projects():
# #     """Test login to fauna.

# #     input: fauna projects
# #     input: secret_path
# #     input: fauna database name to use
# #     side_effect: fauna db write
# #     output: list of data updated -or- bool
# #     input: vault credentials
# #     input_type: str
# #     output_type: FaunaClient
# #     output example: <faunadb.client.FaunaClient object at 0x000002439xxxxx>
# #     """

# #     try:
# #         todoist_api_token = vault_login(
# #             secret_path=SECRET_PATH,
# #         )

# #         todoist_project_data = TodoIstOperations().list_projects(
# #             todoist_api_token=todoist_api_token,
# #         )
# #         return todoist_project_data

# #     except Exception as _error:  # pragma: no cover
# #         raise ValueError("Todoist error.") from _error


# #     # next take project data and add date and timestamp
# #     # using new python date timestamp functionailty
# #     # keep in mind javascript / fauna limitations
