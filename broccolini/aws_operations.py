"""AWSOperation functions.

AWS operations.
"""
import logging


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
        """
        return "valuefromfunction"


# """utility functions see shared_utilities/READEM.md
# for information
# """
# import os
# import logging
# import boto3

# logging.basicConfig(
#     level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
# )

# class AwsException(Exception):
#     """Subclass exception for custom exception

#     Example:
#     if not vault_client.is_authenticated():
#         raise AuthException('Failed to aut')
#     """


# class AwsFunctions:
#     """ AWS Functions
#     """

#     def __init__(
#         self,
#         access_key: str = None,
#         secret_access_key: str = None,
#         region: str = None,
#         message_attributes: str = None,
#         message_body: str = None,
#         queue_url: str = None,
#     ) -> None:
#         self.access_key = access_key
#         self.secret_access_key = secret_access_key
#         self.region = region
#         self.message_attributes = message_attributes
#         self.message_body = message_body
#         self.queue_url = queue_url

#     def get_aws_connection(self):
#         """ connect to aws using environment variables
#         start with exporting to environmen vars
#         move to vault - when move to vault get rid of static method and add self
#         """
#         if not self.region:
#             # raise AwsException("missing aws region")
#             raise ValueError("missing aws region")
#         # AwsException("missing aws region")

#         # if not os.getenv("AWS_ACCESS_KEY_ID"):
#         #     raise AwsException("missing aws access key")

#         # if not os.getenv("AWS_SECRET_ACCESS_KEY"):
#         #     raise AwsException("missing aws secret")
#             # raise Exception

#         # aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
#         # aws_access_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
#         # aws_access_key_id = self.access_key
#         # aws_secret_access_key = self.secret_access_key
#         sqs = boto3.client(
#             'sqs',
#             aws_access_key_id=self.access_key,
#             aws_secret_access_key=self.secret_access_key,
#             region_name=self.region
#         )
#         # s3_client = boto3.client('s3',
#         #               aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
#         #               aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY,
#         #               region_name=REGION_NAME
#         #               )
# #         sqs = client = boto3.client(
# #     's3',
# #     aws_access_key_id=ACCESS_KEY,
# #     aws_secret_access_key=SECRET_KEY,
# #     aws_session_token=SESSION_TOKEN,
# # )
# #         sqs = boto3.client(
# #             "sqs",
# #             self.region,
# #             aws_access_key_id=self.access_key,
# #             aws_secret_access_key=self.secret_access_key
# #         )
#         return sqs

#     def send_sqs_message(self):
#         """ send sqs message
#         """
#         sqs = boto3.client(
#             'sqs',
#             aws_access_key_id=self.access_key,
#             aws_secret_access_key=self.secret_access_key,
#             region_name=self.region
#         )
#         # sqs = self.get_aws_connection()
#         response = sqs.send_message(
#             QueueUrl=self.queue_url,
#             DelaySeconds=10,
#             MessageAttributes=self.message_attributes,
#             MessageBody=self.message_body,
#         )
#         return response["MessageId"]

#     def list_sqs_messages(self):
#         """  list sqs messages
#         """
#         sqs = self.get_aws_connection()
#         # return(sqs.get_queue_attributes(QueueUrl=self.queue_url))
#         messages = sqs.receive_message(
#             QueueUrl=self.queue_url, MaxNumberOfMessages=10, WaitTimeSeconds=1
#         )
#         return messages
#         # all_messages = []
#         # request = sqs.get_messages(10)
#         # while len(request) > 0:
#         #     all_messages.extend(request)
#         #     request = sqs.get_messages(10)
#         # logging.debug(request)
#         # return request
#         # response = sqs.send_message(
#         #     QueueUrl=self.queue_url,
#         #     DelaySeconds=10,
#         #     MessageAttributes=self.message_attributes,
#         #     MessageBody=self.message_body,
#         # )
#         # return response["MessageId"]

#         # def other_sqs_methods(self):
#         """Other sqs functions to add and test.
#         WIP
#         # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html
#
#          sqs = boto3.resource('sqs')
#         # Create the queue. This returns an SQS.Queue instance
#         queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})
#         # You can now access identifiers and attributes
#         print(queue.url)
#         print(queue.attributes.get('DelaySeconds'))
#         # Get the service resource
#         sqs = boto3.resource('sqs')
#         # Get the queue. This returns an SQS.Queue instance
#         queue = sqs.get_queue_by_name(QueueName='test')
#         # You can now access identifiers and attributes
#         print(queue.url)
#         print(queue.attributes.get('DelaySeconds'))
#         #Print out each queue name, which is part of its ARN
#         for queue in sqs.queues.all():
#             print(queue.url)
#         """

#     def read_and_delete_sqs_message(self):
#         """ read and delete sqs messages
#         grab message one at a time and delete it
#         need add if not messages exit or put another function to wrap it
#         """
#         sqs = self.get_aws_connection()

#         try:
#             response = sqs.receive_message(
#                 QueueUrl=self.queue_url,
#                 AttributeNames=["SentTimestamp"],
#                 MaxNumberOfMessages=1,
#                 MessageAttributeNames=["All"],
#                 VisibilityTimeout=0,
#                 WaitTimeSeconds=0,
#             )

#             message = response["Messages"][0]
#             receipt_handle = message["ReceiptHandle"]
#             body_of_message_1 = message["Body"]

#             sqs.delete_message(QueueUrl=self.queue_url, ReceiptHandle=receipt_handle)
#             return (
#                 f"received and deleted message {message}
#                 with body:{body_of_message_1}"
#             )

#         except KeyError as error_msg:
#             return f"error_msg is {error_msg}"
#         # except (KeyError, Exception) as error_msg:


# # def main():
# #     """Call other functions from here when called directly.

# #     The above is the current recommended way using pydocstyle.
# #     """

# #     #logging.debug("start of main function")
# #     aws_region = "us-east-1"
# #     sqs_queue_url = (
# #         "https://sqs.us-east-1.amazonaws.com/568639476002/directories_to_process"
# #     )
# #     sqs_message_attributes = {
# #         "JobName": {"DataType": "String", "StringValue": "JOBNAMEHERE"}
# #     }
# #     sqs_message_body = "Information on jobs from git status command."
# #     aws_result = AwsFunctions(
# #         region=aws_region,
# #         queue_url=sqs_queue_url,
# #         message_attributes=sqs_message_attributes,
# #         message_body=sqs_message_body,
# #     )
# #     # readanddelete = aws_result.read_and_delete_sqs_message()
# #     # sendmesage = aws_result.send_sqs_message()
# #     listmessages = aws_result.list_sqs_messages()
# #     print(listmessages)
# #     # logging.debug(readanddelete)
# #     # logging.debug(sendmesage)
# #     # logging.debug(dir(listmessages))
# #     # logging.debug(listmessages)


# # if __name__ == "__main__":
# #     main()
