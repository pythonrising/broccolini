"""PresentationOperation functions.

Presentation operations.
"""
import logging


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class PresentationOperations:
    """Presentation Operation Functions."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    def prepare_template(self, **kwargs: str) -> str:
        """Create template.
        input_Data: json_file build dictionary from file in json format
        input_data: dict - dictionary of values to build template
        input_template_name: str name of the template file
        output_file_name: str - output file name
        """
        output_file_name: str = kwargs["output_file_name"]
        return output_file_name
