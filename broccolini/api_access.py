"""API Access functions.

API Access functions.
"""
import logging

# from typing import List, Tuple, Dict

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class ApiAccess:
    """Process such as psutil."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    # def view_running_processes(**kwargs: str) -> List[Tuple[str, int]]:
    def connect_to_api() -> str:
        """View Running Processes.
        input: input_data
        input_type: str
        output: list_of_files
        output_type: List[Tuple]
        """
        return "greg"
        # input_data: str = kwargs["input_data"]
        # return input_data

    @staticmethod
    def connect_to_api_updated() -> str:
        """View Running Processes."""
        return "greg"
        # input_data: str = kwargs["input_data"]
        # return input_data
