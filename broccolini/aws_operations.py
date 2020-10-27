"""AWSOperation functions.

AWS operations.
"""
import logging
import random

from os import environ

import boto3


# from botocore.exceptions import ClientError


TEMP_BUCKET_NAME = "gdw" + str(random.randint(0, 88888))

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
        Args:
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

    def aws_create_s3_bucket(self, **kwargs: str) -> bool:
        """Create S3 bucket."""
        aws_client = self.aws_get_connection(
            aws_access_key_id=kwargs["aws_access_key_id"],
            aws_secret_access_key=kwargs["aws_secret_access_key"],
            aws_default_region=kwargs["aws_default_region"],
        )
        _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
        _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
        _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]
        # _other_setings: str = kwargs["other_setings"]

        try:
            if _aws_access_key_id not in environ:
                environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

            if _aws_secret_access_key not in environ:
                environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

            if _aws_default_region not in environ:
                environ["AWS_DEFAULT_REGION"] = _aws_default_region

            # session = boto3.Session(
            #     aws_access_key_id=_aws_access_key_id,
            #     aws_secret_access_key=_aws_secret_access_key,
            # )

            s3_client = boto3.client(
                "s3",
                aws_access_key_id=_aws_access_key_id,
                aws_secret_access_key=_aws_secret_access_key,
                region_name=_aws_default_region,
            )

            s3_client.create_bucket(Bucket=TEMP_BUCKET_NAME)

        except (Exception) as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error


# >>> s3_client = boto3.client('s3',
# ...                       aws_access_key_id=AWSID,
# ...                       aws_secret_access_key=AWSKEY,
# ...                       region_name='us-east-1'
# ...                       )

# try:
#     if _aws_default_region is None:
#         s3_client = boto3.client(
#             "s3",
#             aws_access_key_id=_aws_access_key_id,
#             aws_secret_access_key=_aws_secret_access_key,
#         )
#         # print(s3_client)
#         s3_client.create_bucket(Bucket=TEMP_BUCKET_NAME)

#     else:
#         s3_client = boto3.client("s3", region_name=_aws_default_region)
#         location = {"LocationConstraint": _aws_default_region}
#         try:
#             s3_client.create_bucket(
#                 Bucket=TEMP_BUCKET_NAME, CreateBucketConfiguration=location
#             )
#             print("bucket created")
#         except:
#             print("bucket not created")

# except ClientError as _error:
#     logging.error(_error)
#     return False
