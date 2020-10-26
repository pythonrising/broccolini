#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testing integration from files in directory to fauna database.

Used for tracking duplicate files.
Also used as a basis for testing file async functionality
"""

import logging

from dataclasses import dataclass

import pytest

from broccolini.authentication_functions import VaultFunctions
from broccolini.database_operations import DataBaseOperations
from broccolini.fileoperation_functions import FileOperationFunctions


@dataclass
class FileAndFolderInformation:
    """File and folder storage"""

    file_name: str
    path: str
    subject: str = None


FAUNA_COLLECTION_NAME = "training_collection"
FAUNA_DOCUMENT_DATA = {
    "data": {
        "name": "tests\\fake_data_from_conftest\\training\\javascript\\behavior.pdf"
    }
}


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestIntegrationFileToFauna:
    """Test the integration from files to fauna database."""

    @classmethod
    def get_test_values(cls, secret_path):
        """Build values needed for the test."""
        try:
            fauna_secret_key = VaultFunctions().query_vault_data(
                vault_url="VAULT_URL",
                vault_token="VAULT_TOKEN",
                secret_path=secret_path,
            )
            return fauna_secret_key["data"]["data"]["_key"]
        except KeyError as _error:  # pragma: no cover
            raise ValueError("Missing environment variables") from _error

    # @pytest.mark.skip(reason="integration testing")
    @staticmethod
    @pytest.fixture()
    def test_get_files_from_folder(return_data_dict):
        """Get list of files from the directory.

        input: folder_name
        output: list_of_files
        output_type: List[Dict['folders_and_files'][pathlib.WindowsPath]]
        """
        result = FileOperationFunctions().get_file_information_build(
            input_directory=return_data_dict["faker_files"],
            output_file_name=return_data_dict["output_file_name"],
        )
        return result

    @staticmethod
    def test_integration_sample_training_data_to_fauna(
        return_database_settings, test_get_files_from_folder
    ):
        """Create document using data created in other function."""
        client_token = TestIntegrationFileToFauna.get_test_values(
            return_database_settings["fauna_path_srv"],
        )

        # run this if you manually delete the collection
        # DataBaseOperations(client_token=client_token).fauna_create_collection(
        #     fauna_collection_name=FAUNA_COLLECTION_NAME,
        # )
        list_of_dataclasses = []

        for each in test_get_files_from_folder:
            file_name = each["folders_and_files"][0].name
            path = str(each["folders_and_files"][0].parent)
            subject = "subject_needed"
            dataclass_ = FileAndFolderInformation(file_name, path, subject)
            list_of_dataclasses.append(dataclass_)
            # file_data2 = FileAndFolderInformation(file_name, path, subject)

        # print(list_of_dataclasses)
        for each in list_of_dataclasses:
            records_to_add = {
                "data": {
                    "file_name": each.file_name,
                    "path": each.path,
                    "subject": each.subject,
                }
            }
            print(records_to_add)
            DataBaseOperations(client_token=client_token).fauna_create_document(
                fauna_collection_name=FAUNA_COLLECTION_NAME,
                fauna_document_data=records_to_add,
            )

        # records_to_add = {"data": {
        #     "file_name": file_data2.file_name,
        #     "path": file_data2.path,
        #     "subject": file_data2.subject,
        #     }
        # }

        # result = DataBaseOperations(client_token=client_token).fauna_create_document(
        #     fauna_collection_name=FAUNA_COLLECTION_NAME,
        #     fauna_document_data=records_to_add,
        # )
        # return result
