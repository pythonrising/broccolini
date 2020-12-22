"""AWSOperation functions.

AWS operations.
"""
import logging

from os import environ
from typing import Dict
from typing import List

import boto3

from botocore.exceptions import ClientError


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
    def aws_get_connection(**kwargs: str) -> Dict[str, str]:
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
            s3_resource.Bucket(aws_s3_bucket_name).delete()
            return True

        except Exception as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error

    def aws_list_s3_buckets(self, **kwargs: str) -> List[str]:
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
            list_of_buckets: List[object] = s3_client.list_buckets()
            return list_of_buckets

        except (ClientError) as _error:  # pragma: no cover
            raise ValueError("AWS error.") from _error

    def aws_sqs_send_message(self, **kwargs: str) -> bool:
        """Send sqs message.

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

    # def aws_iam_delete_user(self, **kwargs: str) -> bool:
    #     """IAM delete user."""
    #     aws_client = self.aws_get_connection(
    #         aws_access_key_id=kwargs["aws_access_key_id"],
    #         aws_secret_access_key=kwargs["aws_secret_access_key"],
    #         aws_default_region=kwargs["aws_default_region"],
    #     )
    #     _aws_access_key_id: str = aws_client["AWS_ACCESS_KEY_ID"]
    #     _aws_secret_access_key: str = aws_client["AWS_SECRET_ACCESS_KEY"]
    #     _aws_default_region: str = aws_client["AWS_DEFAULT_REGION"]
    #     try:
    #         if _aws_access_key_id not in environ:
    #             environ["AWS_ACCESS_KEY_ID"] = _aws_access_key_id

    #         if _aws_secret_access_key not in environ:
    #             environ["AWS_SECRET_ACCESS_KEY"] = _aws_secret_access_key

    #         if _aws_default_region not in environ:
    #             environ["AWS_DEFAULT_REGION"] = _aws_default_region

    #         # user_name: str = kwargs["user_name"]
    #         # group_name: str = kwargs["group_name"]

    #         iam_resource = boto3.resource(
    #             "iam",
    #             aws_access_key_id=_aws_access_key_id,
    #             aws_secret_access_key=_aws_secret_access_key,
    #             region_name=_aws_default_region,
    #         )

    #         # KEY = 'LastUsedDate'
    #         client = boto3.client("iam")
    #         all_users = iam_resource.users.all()
    #         print(type(all_users))
    #         # for user in iam_resource.users.all():
    #         #     meta_data = client.list_access_keys(UserName=user.user_name)
    #         #     if meta_data["AccessKeyMetadata"]:
    #         #         all_users.append(user)

    #         print(all_users)

    #     except Exception as _error:  # pragma: no cover
    #         raise ValueError("AWS error.") from _error
