# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Testing integration from files in directory to fauna database.

# Used for tracking duplicate files.
# Also used as a basis for testing file async functionality
# """

# import logging

# from dataclasses import dataclass

# import pytest

# from broccolini.common import get_authentication_values
# from broccolini.database_operations import DataBaseOperations
# from broccolini.fileoperation_functions import FileOperationFunctions


# @dataclass
# class FileAndFolderInformation:
#     """File and folder storage"""

#     file_name: str
#     path: str
#     subject: str = None


# FAUNA_COLLECTION_NAME = "training_collection"


# logging.basicConfig(
#     level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
# )


# class TestIntegrationFileToFauna:
#     """Test the integration from files to fauna database."""

#     @staticmethod
#     @pytest.fixture()
#     def test_get_files_from_folder(return_data_dict):
#         """Get list of files from the directory.

#         input: folder_name
#         output: list_of_files
#         output_type: List[Dict['folders_and_files'][pathlib.WindowsPath]]
#         """
#         result = FileOperationFunctions().get_file_information_build(
#             input_directory=return_data_dict["faker_files"],
#             output_file_name=return_data_dict["output_file_name"],
#         )
#         return result

#     @staticmethod
#     def test_integration_sample_training_data_to_fauna(
#         return_database_settings, test_get_files_from_folder
#     ):
#         """Create document using data created in other function."""
#         client_token = get_authentication_values(
#             return_database_settings["fauna_path_srv"],
#         )

#         list_of_dataclasses = []

#         for each in test_get_files_from_folder:
#             file_name = each["folders_and_files"][0].name
#             path = str(each["folders_and_files"][0].parent)
#             subject = "subject_needed"
#             dataclass_ = FileAndFolderInformation(file_name, path, subject)
#             list_of_dataclasses.append(dataclass_)

#         for each in list_of_dataclasses:
#             records_to_add = {
#                 "data": {
#                     "file_name": each.file_name,
#                     "path": each.path,
#                     "subject": each.subject,
#                 }
#             }
#             DataBaseOperations(client_token=client_token).fauna_create_document(
#                 fauna_collection_name=FAUNA_COLLECTION_NAME,
#                 fauna_document_data=records_to_add,
#             )
