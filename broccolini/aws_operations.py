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

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""
        # self.client_token = client_token

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    def aws_get_connection(**kwargs: str) -> dict[str, str]:
        """Get AWS Connection.

        Provide credentials and settings to other methods.
        Arguments:
        aws_access_key_id: str AWS creds key id
        aws_secret_key: str AWS cred secret key
        aws_default_region: str AWS region

        Returns:
        output: dict[str, str] Dictionary of login values
        """
        aws_access_key_id: str = kwargs["aws_access_key_id"]
        aws_secret_access_key: str = kwargs["aws_secret_access_key"]
        aws_default_region: str = kwargs["aws_default_region"]

        return dict(
            AWS_ACCESS_KEY_ID=aws_access_key_id,
            AWS_SECRET_ACCESS_KEY=aws_secret_access_key,
            AWS_DEFAULT_REGION=aws_default_region,
            # aws_region="us-east-1",
        )
