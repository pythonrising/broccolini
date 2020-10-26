"""AWSOperation functions.

AWS operations.
"""
import logging


# from os import environ


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class AWSOperations:
    """AWS Operation Functions.

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

    @staticmethod
    def aws_get_connection() -> str:
        """Get AWS Connection.

        input: str  inputdata
        output: str outputdata
        # get creds from vault
        # set env variable
        # if not import os
        >>> 'HOME' in os.environ  # Check an existing env. variable
        True
        have functions just use env vars
        from os import environ
        'SYSTEMDRIVE' in environ
        AWS_DEFAULT_REGION=us-east-1
        This function uses vault to get the variables and returns to function
        try:
        """
        # return dict(
        #     AWS_ACCESS_KEY_ID='MISSING_ACCESS_KEY_ID',
        #     AWS_SECRET_ACCESS_KEY='MISSING_ACCESS_KEY',
        #     AWS_DEFAULT_REGION='MISSING_REGION',
        # )
        return "valuefromfunction"
