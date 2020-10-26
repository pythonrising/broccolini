#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing AWS operations functions.

Testing common AWS operations. Initially using SQS and S3.
"""

import logging

import pytest

from broccolini.authentication_functions import VaultFunctions
from broccolini.aws_operations import AWSOperations


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
        aws_region
        """
        aws_access_key_id = TestAWSOperations.get_test_values(
            return_aws_settings["aws_access_key_id_path"]
        )
        aws_secret_access_key = TestAWSOperations.get_test_values(
            return_aws_settings["aws_secret_access_key_path"]
        )

        result = AWSOperations(client_token=aws_access_key_id).aws_get_connection()
        result2 = AWSOperations(client_token=aws_secret_access_key).aws_get_connection()
        print(type(result))
        print(type(result2))

    # @staticmethod
    # @pytest.mark.dependency(depends=["test_login_to_aws"])
    # def test_create_bucket(return_aws_settings):  # pragma: no cover
    #     """Test create aws S3 bucket.

    #     what creds are needed to create the s3 bucket
    #     need region from conftest
    #     """

    #     result = AWSOperations(client_token=aws_secret_access_key).create_bucket(
    #         aws_region=return_aws_settings['aws_region'],
    #         creds1='creds1',
    #         creds2='creds2',
    #     )

    #     expected = True
    #     expected_type = bool
    #     assert isinstance(result, expected_type)
    #     assert expected == result

    # expected = "valuefromfunction"
    # expected_type = str
    # assert expected == result
    # assert isinstance(result, expected_type)
