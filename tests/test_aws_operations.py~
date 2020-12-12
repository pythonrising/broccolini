#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing AWS operations functions.

Testing common AWS operations. Initially using SQS and S3.
"""

import logging

import pytest

from broccolini.aws_operations import AWSOperations
from broccolini.common import get_authentication_values


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

    @staticmethod
    @pytest.mark.dependency(name="test_login_to_aws")
    def test_aws_get_connection(return_aws_settings):  # pragma: no cover
        """Test login to aws.

        input: str TBD
        output: str TBD
        aws_secret_access_key_path
        aws_region: str TBD
        """
        aws_access_key_id = get_authentication_values(
            secret_path=return_aws_settings["aws_s3_key_id_path"]
        )
        aws_secret_access_key = get_authentication_values(
            secret_path=return_aws_settings["aws_s3_secret_key_path"]
        )

        aws_default_region = return_aws_settings["aws_default_region"]

        result = AWSOperations().aws_get_connection(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_default_region=aws_default_region,
        )

        expected = return_aws_settings["aws_default_region"]
        expected_type = dict
        assert expected == result["AWS_DEFAULT_REGION"]
        assert isinstance(result, expected_type)

    @staticmethod
    # @pytest.mark.dependency(depends=["test_login_to_aws"])
    def test_aws_iam_functions(return_aws_settings):  # pragma: no cover
        """Test IAM settings."""
        aws_access_key_id = get_authentication_values(
            secret_path=return_aws_settings["aws_iam_key_id_path"]
        )
        aws_secret_access_key = get_authentication_values(
            secret_path=return_aws_settings["aws_iam_secret_key_path"]
        )
        aws_default_region = return_aws_settings["aws_default_region"]

        user_name = return_aws_settings["aws_iam_user"]
        group_name = return_aws_settings["aws_iam_group"]

        result_create_user = AWSOperations().aws_iam_create_user(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_default_region=aws_default_region,
            user_name=user_name,
        )
        expected_type_create_user = bool
        assert isinstance(result_create_user, expected_type_create_user)

        result_add_user_to_group = AWSOperations().aws_iam_add_user_to_group(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_default_region=aws_default_region,
            user_name=user_name,
            group_name=group_name,
        )
        expected_type_add_user_to_group = bool
        assert isinstance(result_add_user_to_group, expected_type_add_user_to_group)

    @staticmethod
    def test_aws_iam_list_users(return_aws_settings):  # pragma: no cover
        """[summary]

        Args:
            return_aws_settings ([type]): [description]
        """

        aws_access_key_id = get_authentication_values(
            secret_path=return_aws_settings["aws_iam_key_id_path"]
        )
        aws_secret_access_key = get_authentication_values(
            secret_path=return_aws_settings["aws_iam_secret_key_path"]
        )
        aws_default_region = return_aws_settings["aws_default_region"]

        user_name = return_aws_settings["aws_iam_user"]

        result_list_users = AWSOperations().aws_iam_list_users(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_default_region=aws_default_region,
            user_name=user_name,
        )

        assert result_list_users
