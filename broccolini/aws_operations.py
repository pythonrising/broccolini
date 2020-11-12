"""AWSOperation functions.

AWS operations.
"""
import logging

from dataclasses import dataclass
from os import environ

import boto3

from botocore.exceptions import ClientError


# from botocore.exceptions import ParamValidationError


@dataclass
class AWSUser:
    """Data class for holding variables."""

    username: str
    secret_access_key: str
    access_key_id: str


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
        )

    def aws_delete_s3_bucket(self, **kwargs: str) -> bool:
        """Delete S3 bucket.

        Args:
            bucket_name (str): bucket name to delete

        Raises:
            ValueError: AWS error.

        Returns:
            bool: True if successfully deleted bucket.
        """
        aws_client = self.aws_get_connection(
            aws_access_key_id=kwargs["aws_access_key_id"],
            aws_secret_access_key=kwargs["aws_secret_access_key"],
            aws_default_region=kwargs["aws_default_region"],
        )
        _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
        _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
        _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]

        if _aws_access_key_id not in environ:
            environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

        if _aws_secret_access_key not in environ:
            environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

        if _aws_default_region not in environ:
            environ["AWS_DEFAULT_REGION"] = _aws_default_region

        aws_s3_bucket_name = kwargs["aws_s3_bucket_name"]

        s3_resource = boto3.resource(
            "s3",
            aws_access_key_id=_aws_access_key_id,
            aws_secret_access_key=_aws_secret_access_key,
            region_name=_aws_default_region,
        )
        try:
            return s3_resource.Bucket(aws_s3_bucket_name).delete()

        except Exception as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error

    def aws_list_s3_buckets(self, **kwargs: str) -> list[str]:
        """List S3 buckets.

        Args:
            bucket_name (str): bucket name

        Raises:
            ValueError: AWS error.

        Returns:
            list[str]: List of buckets
        """
        aws_client = self.aws_get_connection(
            aws_access_key_id=kwargs["aws_access_key_id"],
            aws_secret_access_key=kwargs["aws_secret_access_key"],
            aws_default_region=kwargs["aws_default_region"],
        )
        _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
        _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
        _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]

        try:
            if _aws_access_key_id not in environ:
                environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

            if _aws_secret_access_key not in environ:
                environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

            if _aws_default_region not in environ:
                environ["AWS_DEFAULT_REGION"] = _aws_default_region

            s3_client = boto3.client(
                "s3",
                aws_access_key_id=_aws_access_key_id,
                aws_secret_access_key=_aws_secret_access_key,
                region_name=_aws_default_region,
                # region_name='missing',
            )
            return s3_client.list_buckets()
        except (ClientError) as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error

    def aws_sqs_send_message(self, **kwargs: str) -> bool:
        """Send sqs message

        Returns:
            bool: Success of send message.
        """
        aws_client = self.aws_get_connection(
            aws_access_key_id=kwargs["aws_access_key_id"],
            aws_secret_access_key=kwargs["aws_secret_access_key"],
            aws_default_region=kwargs["aws_default_region"],
        )
        _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
        _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
        _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]
        try:
            if _aws_access_key_id not in environ:
                environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

            if _aws_secret_access_key not in environ:
                environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

            if _aws_default_region not in environ:
                environ["AWS_DEFAULT_REGION"] = _aws_default_region

            sqs_client = boto3.client(
                "sqs",
                aws_access_key_id=_aws_access_key_id,
                aws_secret_access_key=_aws_secret_access_key,
                region_name=_aws_default_region,
            )

            sqs_client.send_message(
                QueueUrl=kwargs["sqs_queue_url"],
                DelaySeconds=10,
                MessageAttributes=kwargs["sqs_message_attributes"],
                MessageBody=kwargs["sqs_message_body"],
            )
        except (ClientError) as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error
        return True

    def aws_sqs_list_messages(self, **kwargs: str) -> list[str]:
        """SQS list messages.

        Returns:
            list[str]: list of messages
        """
        aws_client = self.aws_get_connection(
            aws_access_key_id=kwargs["aws_access_key_id"],
            aws_secret_access_key=kwargs["aws_secret_access_key"],
            aws_default_region=kwargs["aws_default_region"],
        )
        _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
        _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
        _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]
        try:
            if _aws_access_key_id not in environ:
                environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

            if _aws_secret_access_key not in environ:
                environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

            if _aws_default_region not in environ:
                environ["AWS_DEFAULT_REGION"] = _aws_default_region

            sqs_client = boto3.client(
                "sqs",
                aws_access_key_id=_aws_access_key_id,
                aws_secret_access_key=_aws_secret_access_key,
                region_name=_aws_default_region,
            )
            sqs_client.receive_message(
                QueueUrl=kwargs["sqs_queue_url"],
                MaxNumberOfMessages=10,
                WaitTimeSeconds=1,
            )

        except (ClientError) as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error
        return True

    def aws_sqs_read_and_delete_messages(self, **kwargs: str) -> bool:
        """Read messages and delete them.

        Returns:
            bool: Is delete successful.
        """
        aws_client = self.aws_get_connection(
            aws_access_key_id=kwargs["aws_access_key_id"],
            aws_secret_access_key=kwargs["aws_secret_access_key"],
            aws_default_region=kwargs["aws_default_region"],
        )
        _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
        _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
        _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]
        try:
            if _aws_access_key_id not in environ:
                environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

            if _aws_secret_access_key not in environ:
                environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

            if _aws_default_region not in environ:
                environ["AWS_DEFAULT_REGION"] = _aws_default_region

            sqs_client = boto3.client(
                "sqs",
                aws_access_key_id=_aws_access_key_id,
                aws_secret_access_key=_aws_secret_access_key,
                region_name=_aws_default_region,
            )
            sqs_queue_url = kwargs["sqs_queue_url"]

            response = sqs_client.receive_message(
                QueueUrl=sqs_queue_url,
                AttributeNames=["SentTimestamp"],
                MaxNumberOfMessages=1,
                WaitTimeSeconds=1,
                MessageAttributeNames=["All"],
                VisibilityTimeout=0,
            )
            message = response["Messages"][0]
            receipt_handle = message["ReceiptHandle"]
            body_of_message_1 = message["Body"]

            sqs_client.delete_message(
                QueueUrl=sqs_queue_url, ReceiptHandle=receipt_handle
            )
            return (
                f"received and deleted message {message} with body:{body_of_message_1}"
            )
        except (ClientError, KeyError) as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error

    def aws_iam_list_users(self, **kwargs: str) -> bool:
        """IAM list users."""
        aws_client = self.aws_get_connection(
            aws_access_key_id=kwargs["aws_access_key_id"],
            aws_secret_access_key=kwargs["aws_secret_access_key"],
            aws_default_region=kwargs["aws_default_region"],
        )
        _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
        _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
        _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]

        if _aws_access_key_id not in environ:
            environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

        if _aws_secret_access_key not in environ:
            environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

        if _aws_default_region not in environ:
            environ["AWS_DEFAULT_REGION"] = _aws_default_region

        try:
            boto3.resource(
                "iam",
                aws_access_key_id=_aws_access_key_id,
                aws_secret_access_key=_aws_secret_access_key,
                region_name=_aws_default_region,
            )
            client = boto3.client("iam")
            # print(client.list_users()["Users"][0]['UserName'])
            # print(f'users {client.list_users()}')
            return client.list_users()["Users"]

        except Exception as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error

    def aws_iam_create_user(self, **kwargs: str) -> bool:
        """IAM create user.

        Returns:
            success[bool]: success of creation
        """
        aws_client = self.aws_get_connection(
            aws_access_key_id=kwargs["aws_access_key_id"],
            aws_secret_access_key=kwargs["aws_secret_access_key"],
            aws_default_region=kwargs["aws_default_region"],
        )
        _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
        _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
        _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]

        if _aws_access_key_id not in environ:
            environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

        if _aws_secret_access_key not in environ:
            environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

        if _aws_default_region not in environ:
            environ["AWS_DEFAULT_REGION"] = _aws_default_region

        user_name: str = kwargs["user_name"]

        iam_resource = boto3.resource(
            "iam",
            aws_access_key_id=_aws_access_key_id,
            aws_secret_access_key=_aws_secret_access_key,
            region_name=_aws_default_region,
        )

        try:
            iam_resource.create_user(UserName=user_name)
            client = boto3.client("iam")
            client.create_access_key(UserName=user_name)
            return True

        except Exception as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error

    def aws_iam_add_user_to_group(self, **kwargs: str) -> bool:
        """IAM add user to group."""
        aws_client = self.aws_get_connection(
            aws_access_key_id=kwargs["aws_access_key_id"],
            aws_secret_access_key=kwargs["aws_secret_access_key"],
            aws_default_region=kwargs["aws_default_region"],
            user_name=kwargs["user_name"],
            group_name=kwargs["group_name"],
        )

        _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
        _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
        _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]
        try:
            if _aws_access_key_id not in environ:
                environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

            if _aws_secret_access_key not in environ:
                environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

            if _aws_default_region not in environ:
                environ["AWS_DEFAULT_REGION"] = _aws_default_region

            iam_resource = boto3.resource(
                "iam",
                aws_access_key_id=_aws_access_key_id,
                aws_secret_access_key=_aws_secret_access_key,
                region_name=_aws_default_region,
            )
            user_name: str = kwargs["user_name"]
            group_name: str = kwargs["group_name"]

            try:
                group = iam_resource.Group(group_name)
                group.add_user(UserName=user_name)

            except Exception as _error:  # pragma: no cover
                raise ValueError("AWS error add user to group.") from _error

        except Exception as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error
        return True

    def aws_iam_delete_user(self, **kwargs: str) -> bool:
        """IAM delete user.

        Returns:
            success[bool]: success of deletion
        """
        aws_client = self.aws_get_connection(
            aws_access_key_id=kwargs["aws_access_key_id"],
            aws_secret_access_key=kwargs["aws_secret_access_key"],
            aws_default_region=kwargs["aws_default_region"],
        )
        _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
        _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
        _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]
        try:
            if _aws_access_key_id not in environ:
                environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

            if _aws_secret_access_key not in environ:
                environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

            if _aws_default_region not in environ:
                environ["AWS_DEFAULT_REGION"] = _aws_default_region

            user_name: str = kwargs["user_name"]
            group_name: str = kwargs["group_name"]
            iam_resource = boto3.resource(
                "iam",
                aws_access_key_id=_aws_access_key_id,
                aws_secret_access_key=_aws_secret_access_key,
                region_name=_aws_default_region,
            )

            try:
                group = iam_resource.Group(group_name)
                group.remove_user(UserName=user_name)
                iam_resource.User(user_name).delete()

            except Exception as _error:  # pragma: no cover
                raise ValueError("AWS error.") from _error

        except Exception as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error
        return True

    # # @staticmethod
    # def aws_create_s3_bucket_refactor(self, **kwargs: str) -> bool:
    #     """Create S3 bucket. Using user created in earlier steps.

    #     Access via dataclass
    #     """

    #     user_name: str = kwargs["user_name"]

    # print(user_name)
    # data = self.aws_iam_create_user(
    #     aws_access_key_id=kwargs["aws_access_key_id"],
    #     aws_secret_access_key=kwargs["aws_secret_access_key"],
    #     aws_default_region=kwargs["aws_default_region"],
    #     user_name=user_name,
    # )
    # return data

    # try:
    #     iam_client = boto3.client("iam")
    #     response_s3_key = iam_client.create_access_key(UserName=user_name)
    #     # print('\n')
    #     # print(response_s3_key)
    #     s3_access_key_new = response_s3_key["AccessKey"]
    #     secret_key_s3_generated = s3_access_key_new["SecretAccessKey"]
    #     access_key_id_s3_generated = s3_access_key_new["AccessKeyId"]
    #     # aws_default_region=kwargs["aws_default_region"],
    #     bucket_name=kwargs["aws_s3_bucket_name"]

    #     # print(secret_key_s3_generated)
    #     session = boto3.Session(
    #         # profile_name='devs3',
    #         aws_access_key_id=secret_key_s3_generated,
    #         aws_secret_access_key=access_key_id_s3_generated,
    #     )
    #     dev_s3_client = session.client('s3')
    #     dev_s3_client.create_bucket(Bucket=bucket_name)

    # {print(len(access_key_id_s3_generated)}\n\n"))
    # print("worked\n\n")

    # session = boto3.Session(
    #     aws_secret_access_key=secret_key_s3_generated,
    #     aws_access_key_id=access_key_id_s3_generated,
    #     # aws_default_region=aws_default_region,
    # )
    # bucket=kwargs["aws_s3_bucket_name"]
    # s3 = session.resource('s3')
    # s3_client = boto3.client("s3")
    # s3_client.create_bucket(Bucket=kwargs["aws_s3_bucket_name"])

    # s3_client = boto3.client(
    #     "s3",
    #     aws_access_key_id=secret_key_s3_generated,
    #     aws_secret_access_key=_aws_secret_access_key,
    #     region_name=_aws_default_region,
    # )

    # return s3_client.list_buckets()


#     s3_client = boto3.client(
#         "s3",
#         aws_access_key_id=_aws_access_key_id,
#         aws_secret_access_key=_aws_secret_access_key,
#         region_name=_aws_default_region,
#     )
#     s3_client.create_bucket(Bucket=kwargs["aws_s3_bucket_name"])
#     # botocore.exceptions.ParamValidationError: Parameter validation failed:

# except (ClientError, ParamValidationError) as _error:
#     raise ValueError("AWS error.") from _error


# import boto3
# session = boto3.Session(
#     aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
#     aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY,
# )

# Then use that session to get an S3 resource:

# s3 = session.resource('s3')

#  s3_client = boto3.client('s3',
#                       aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
#                       aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY,
#                       region_name=REGION_NAME
#                       )


#         key_id = credentials['accessKeyId']
#     key_secret = credentials['secretAccessKey']
#     session_token = credentials['sessionToken']
#     session = Session(aws_access_key_id=key_id,
#                       aws_secret_access_key=key_secret,
#                       aws_session_token=session_token)
#     s3 = session.client('s3',
#                         config=botocore.client.Config(signature_version='s3v4'))

# session = Session(aws_access_key_id=artifactCredentials['accessKeyId'],
#                   aws_secret_access_key=artifactCredentials['secretAccessKey'],
#                   aws_session_token=artifactCredentials['sessionToken'])


#         environ['API_USER'] = 'username'
#         environ['API_PASSWORD'] = 'secret'

# # Get environment variables
#         # from os import getenv
#         USER = environ.get('API_USER')
#         PASSWORD = environ.get('API_PASSWORD')
#         print(USER)
#         print(PASSWORD)
#         print(environ.get('API_USER'))
#         print(access_key_id_s3_generated)
#         access_key_id_s3_generated = environ["AWS_ACCESS_KEY_ID"]
#         # print(environ.get["AWS_ACCESS_KEY_ID"])


#         # aws_client = self.aws_get_connection(
#     aws_access_key_id=kwargs["aws_access_key_id"],
#     aws_secret_access_key=kwargs["aws_secret_access_key"],
#     aws_default_region=kwargs["aws_default_region"],
# )
# _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
# _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
# _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]


#     if _aws_secret_access_key not in environ:
#         environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

#     if _aws_default_region not in environ:
#         environ["AWS_DEFAULT_REGION"] = _aws_default_region

#     s3_client = boto3.client(
#         "s3",
#         aws_access_key_id=_aws_access_key_id,
#         aws_secret_access_key=_aws_secret_access_key,
#         region_name=_aws_default_region,
#     )
#     s3_client.create_bucket(Bucket=kwargs["aws_s3_bucket_name"])
#     # botocore.exceptions.ParamValidationError: Parameter validation failed:

# except (ClientError, ParamValidationError) as _error:
#     raise ValueError("AWS error.") from _error
#     # return False
# return True
