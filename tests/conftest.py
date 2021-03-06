#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide non secret data here for all tests.

Give data in various forms to the test functions.
"""
import random
import time

import pytest
import shortuuid

from faker import Faker


@pytest.fixture(scope="session")
def return_random_uuid():
    """Provide random values."""
    return f"conftest_{shortuuid.uuid()}"


@pytest.fixture(scope="session")
def return_data_dict():
    """Provide dictionary values to functions."""
    input_dict = dict(
        github_token="GITHUB_TOKEN_FROM_CONFTEST",
        vault_url="VAULT_URL_FROM_CONFTEST",
        secret_path="python_rising/dev/path1conftest",
        secret=dict(secret_test_key="secret_value_from_conftest"),
        twilio_auth_token="python_rising/dev/twilio_data/TWILIO_AUTH_TOKEN",
        twilio_account_sid="python_rising/dev/twilio_data/TWILIO_ACCOUNT_SID",
        twilio_notify_number="python_rising/dev/twilio_data/TWILIO_NOTIFICATION_NUMBER",
        twilio_phone_number="python_rising/dev/twilio_data/TWILIO_PHONE_NUMBER",
        written_directories=["dir_test1", "dir_test2", "dir_test3"],
        valid_json_file_name="json_file_from_conftest.json",
        faker_files=r"./tests/fake_data_from_conftest/training",
        output_file_name=r"./tests/__output_files/output_json_files.json",
        input_directory_path=r"",
        api_url=r"python_rising/dev/python_rising/dev/api_data/API_URL",
        api_key=r"python_rising/dev/python_rising/dev/api_data/API_KEY",
        # fix duplicate above
        todoist_secret_path="python_rising/dev/todoist_data/TODOIST_API_TOKEN",
    )
    return input_dict


@pytest.fixture(scope="session")
def presentation_settings():
    """Provide values for presentation functions."""
    input_dict = dict(
        input_template_name="new_python_script.jinja2",
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=False,
        autoescape_formats=["html", "xml"],
        template_dict_values=dict(
            long_description="long_description_from_conftest", title="title"
        ),
    )
    return input_dict


@pytest.fixture(scope="session")
def return_database_settings():
    """Provide values for Fauna.

    Note Fauna uses admin keys and server keys.  Server mapped to databases.
    """
    input_dict = dict(
        fauna_secret_path_admin="python_rising/dev/faunadb/admin/api_token",
        fauna_test_data=r"string formatted test data from conftest",
        fauna_path_srv="python_rising/dev/faunadb/pythonrising_dev/server/api_token",
        fauna_db_name="pythonrising_dev",
        fauna_collection_name="collection_name_used_for_delete_test",
        fauna_index_name="index_name_used_for_delete_test",
        fauna_index_name_all="all_Items",
        fauna_test_bad_database=r"bad_database",
        fauna_document_data={"data": {"name": "tdata", "CtestDkey": ["air", "fire"]}},
        fauna_extended_term="fire",
        fauna_new_collection_name="Conftest_db_items",
        fauna_new_index_name="items_search_by_name",
        fauna_new_search_term="Name_conftest_101",
        fauna_reference_id="101",
        fauna_id_101_extra="Description conftest 101.",
        fauna_input_template_name="fauna_bulk_upload_preparation.jinja2",
        fauna_input_data_csv="__input_files/fauna_input_data.csv",
        fauna_output_file="__output_files/fauna_template_output.txt",
        fauna_training_path="python_rising/dev/faunadb/training_db/server/api_token",
    )
    return input_dict


@pytest.fixture(scope="session")
def mock_settings():
    """Provide values for mocks."""

    input_dict = dict(
        bad_mock_input_value="BAD MOCK VALUES FROM CONFTEST",
        bad_mock_output_value="BAD MOCK VALUES FROM CONFTEST",
        mock_input_value="mock_input_from_conftest",
        mock_output_value="mock_input_from_conftest",
    )
    return input_dict


@pytest.fixture(scope="session")
def return_json_settings():
    """Provide values for json functions."""

    input_dict = dict(
        json_output_file_name="./__output_files/result_sample.json",
        json_dict_test={
            "Title": {"DataType": "String", "StringValue": "The Whistler"},
            "Author": {"DataType": "String", "StringValue": "John Grisham"},
            "WeeksOn": {"DataType": "Number", "StringValue": "6"},
        },
        json_list_test=[
            {
                "api_version": "v1alpha1",
                "directorate_name": "directname",
                "project_name": "PROJNAMEHERE",
                "target_revision": "main",
            },
            {
                "file1_name": "file_to_be_copied_created_by_conftest.txt",
                "file2_name": "file2_to_be_copied_created_by_conftest.txt",
            },
            {
                "api_version": "v1alpha2",
                "directorate_name": "adsfdssd2",
                "project_name": "PROJNAMEHERE2",
                "target_revision": "targetrev",
            },
        ],
    )
    return input_dict


@pytest.fixture(scope="session")
def return_aws_settings():
    """Provide values for AWS."""
    # faker = Faker("en_US")
    # short_uuid_conftest = shortuuid.ShortUUID(alphabet="01345678")
    # aws_s3_bucket_name = short_uuid_conftest.uuid()
    # aws_s3_bucket_name = f's3Bucket{faker.name()}'
    # aws_s3_bucket_name = f's3-bucket{faker.name()}'
    # {faker.random_lowercase_letter()}-{faker.random_int()}
    # aws_s3_bucket_name = f's3-{faker.random_lowercase_letter()}{faker.random_int()}'
    aws_s3_bucket_name = f"s3-conftest-{time.time_ns()}"
    aws_s3_bad_bucket_name = "badbucketname_with_underscorecharacter"

    input_dict = dict(
        aws_s3_key_id_path="python_rising/dev/aws_data/AWS_ACCESS_KEY_ID",
        aws_s3_secret_key_path="python_rising/dev/aws_data/AWS_SECRET_ACCESS_KEY",
        aws_s3_bucket_name=aws_s3_bucket_name,
        aws_s3_bad_bucket_name=aws_s3_bad_bucket_name,
        aws_default_region="us-east-1",
        aws_sqs_key_id_path="python_rising/dev/aws_data/sqs/AWS_ACCESS_KEY_ID",
        aws_sqs_secret_key_path="python_rising/dev/aws_data/sqs/AWS_SECRET_ACCESS_KEY",
        sqs_queue_url=(
            "https://sqs.us-east-1.amazonaws.com/568639476002/directories_to_process"
        ),
        sqs_message_attributes={
            "Title": {"DataType": "String", "StringValue": "The Whistler"},
            "Author": {"DataType": "String", "StringValue": "John Grisham"},
            "WeeksOn": {"DataType": "Number", "StringValue": "6"},
        },
        sqs_message_body=("Information about bestseller for week of 12/11/2016."),
        aws_iam_key_id_path="python_rising/dev/aws_data/iam/AWS_ACCESS_KEY_ID",
        aws_iam_secret_key_path="python_rising/dev/aws_data/iam/AWS_SECRET_ACCESS_KEY",
        aws_iam_user=f"user-conftest-{time.time_ns()}",
        aws_iam_group="s3_users",
        aws_iam_group_arn="arn:aws:iam::568639476002:group/s3_users",
    )
    return input_dict


@pytest.fixture
def return_a_list():
    """Function returns list values."""
    input_list = [
        {
            "api_version": "v1alpha1",
            "directorate_name": "directname",
            "project_name": "PROJNAMEHERE",
            "target_revision": "main",
        },
        {
            "file1_name": "file_to_be_copied_created_by_conftest.txt",
            "file2_name": "file2_to_be_copied_created_by_conftest.txt",
        },
        {
            "api_version": "v1alpha2",
            "directorate_name": "adsfdssd2",
            "project_name": "PROJNAMEHERE2",
            "target_revision": "targetrev",
        },
    ]
    return input_list


@pytest.fixture
def create_generic_json_test_file(tmpdir_factory):
    """create a generic test directory."""
    folder_name = "generic_test_directory_json"
    file_name = "generic_file_name_json.json"
    a_dir = tmpdir_factory.mktemp(folder_name)
    a_file = a_dir.join(file_name)
    return a_file


@pytest.fixture
def create_dir_to_simulate_json_bulk_load_orig(tmpdir_factory):
    """Create a directory with json files in it."""
    json_string = """
        {
        "website": "website_from_conftest",
        "topic": "json and python",
        "year": 2019,
        "list": [10, 20, 30]
    }
    """
    folder_name = "folder_with_sample_json"
    file_name = "json_vault_test_data.json"
    a_dir = tmpdir_factory.mktemp(folder_name)
    a_file = a_dir.join(file_name)

    with open(a_file, "w") as file_p:
        file_p.write(json_string)
    return a_file


@pytest.fixture(scope="session")
def create_list_of_filenames_and_directories(tmpdir_factory):
    """Create a list of directories and files from various choices."""
    base_file_name = "test_dir_created/training/"
    # base_file_name = "training/"
    test_dir_name = tmpdir_factory.mktemp("test_dir_created")
    # test_dir_name = tmpdir_factory.mktemp(base_file_name)
    # test_dir_name = tmpdir_factory.mktemp()
    # print(f"testdirname {test_dir_name}")
    faker = Faker("en_US")
    # base_file_name = "training/"
    folder_list = ["python", "javascript", "network", "ml_ai"]
    sub_directory_name_list = ["subdir_1", "subdir_2", "subdir_3"]
    folder_type = random.choice(folder_list)
    full_path = (
        base_file_name
        + folder_type
        + "/"
        + faker.file_name(extension="txt", category="office")
    )
    file_path_and_name_list = []
    for _ in range(5):
        folder_type = random.choice(folder_list)
        subdirectory = random.choice(sub_directory_name_list)
        full_path = (
            base_file_name
            + folder_type
            + "/"
            + faker.file_name(extension="txt", category="office")
        )
        full_path_subdir = (
            base_file_name
            + folder_type
            + "/"
            + subdirectory
            + "/"
            + faker.file_name(extension="txt", category="office")
        )
        file_path_and_name_list.append(full_path)
        file_path_and_name_list.append(full_path_subdir)
    # list_of_directories = []
    full_path_including_file = []
    for each in file_path_and_name_list:
        directory_and_path = str(test_dir_name) + "/" + each
        full_path_including_file.append(directory_and_path)
    return full_path_including_file, test_dir_name
