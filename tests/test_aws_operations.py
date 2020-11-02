#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing AWS operations functions.

Testing common AWS operations. Initially using SQS and S3.
"""

import logging

import pytest

from broccolini.authentication_functions import VaultFunctions
from broccolini.aws_operations import AWSOperations


OTHER_SETTINGS = "other settings"

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestAWSOperations:
    """Test AWS Operation Functions.

    plan
    get a connection using credentials from vault.
    use this connection to login to sqs
    mock this connection
    input: str aws_credentials_from_vault
    output: sqs/s3 client and others
    """

    @classmethod
    def get_test_values(cls, secret_path):
        """Build values for the test."""
        try:
            aws_secret_key = VaultFunctions().query_vault_data(
                vault_url="VAULT_URL",
                vault_token="VAULT_TOKEN",
                secret_path=secret_path,
            )
            return aws_secret_key["data"]["data"]["_key"]
        except KeyError as _error:  # pragma: no cover
            raise ValueError("Missing environment variables") from _error

    @staticmethod
    @pytest.mark.dependency(name="test_login_to_aws")
    def test_aws_get_connection(return_aws_settings):  # pragma: no cover
        """Test login to aws.

        input: str TBD
        output: str TBD
        aws_secret_access_key_path
        aws_region: str TBD
        """
        aws_access_key_id = TestAWSOperations.get_test_values(
            secret_path=return_aws_settings["aws_access_key_id_path"]
        )
        aws_secret_access_key = TestAWSOperations.get_test_values(
            secret_path=return_aws_settings["aws_secret_access_key_path"]
        )
        aws_default_region = return_aws_settings["aws_default_region"]

        result = AWSOperations().aws_get_connection(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_default_region=aws_default_region,
            # other_setings=OTHER_SETTINGS,
        )

        # note returning region to avoid any logging of credentials
        expected = return_aws_settings["aws_default_region"]
        expected_type = dict
        assert expected == result["AWS_DEFAULT_REGION"]
        assert isinstance(result, expected_type)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_aws"])
    def test_aws_create_s3_bucket(return_aws_settings):  # pragma: no cover
        """Test create aws S3 bucket.

        Get data from aws_get_connection
        Put in as environment VARIABLES
        Then run create bucket script
        """
        aws_access_key_id = TestAWSOperations.get_test_values(
            secret_path=return_aws_settings["aws_access_key_id_path"]
        )
        aws_secret_access_key = TestAWSOperations.get_test_values(
            secret_path=return_aws_settings["aws_secret_access_key_path"]
        )
        aws_default_region = return_aws_settings["aws_default_region"]

        # AWSOperations().aws_create_s3_bucket(
        #     aws_access_key_id=aws_access_key_id,
        #     aws_secret_access_key=aws_secret_access_key,
        #     aws_default_region=aws_default_region,
        # )
        result = AWSOperations().aws_create_s3_bucket(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_default_region=aws_default_region,
        )
        expected_type = bool
        assert isinstance(result, expected_type)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_aws"])
    def test_aws_list_s3_buckets(return_aws_settings):  # pragma: no cover
        """Test list AWS S3 buckets."""
        aws_access_key_id = TestAWSOperations.get_test_values(
            secret_path=return_aws_settings["aws_access_key_id_path"]
        )
        aws_secret_access_key = TestAWSOperations.get_test_values(
            secret_path=return_aws_settings["aws_secret_access_key_path"]
        )
        aws_default_region = return_aws_settings["aws_default_region"]

        result = AWSOperations().aws_list_s3_buckets(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_default_region=aws_default_region,
            other_setings=OTHER_SETTINGS,
        )
        expected_type = dict
        assert isinstance(result, expected_type)
        # print(type(result))
        # print(result)
