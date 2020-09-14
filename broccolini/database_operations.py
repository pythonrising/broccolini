"""DataBaseOperation functions.

DataBase operations.
"""
import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class DataBaseOperationFunctions:
    """DataBase Operation Functions."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    def fauna_first(**kwargs: str) -> str:
        """Get Fauna Connection.

        input: vault credentials from environment variables
        input_type: str
        output: fauna database connection
        output_type: fauna client
        """
        fauna_secret_path = kwargs["fauna_secret_path"]
        return fauna_secret_path
