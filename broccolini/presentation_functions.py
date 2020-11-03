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
    def prepare_template(**kwargs: str) -> str:
        """Create template.
        input_data_file: file to build dictionary from
        input_template_name: str name of the template file
        output_file_name_jinja2: str - output_file_name_jinja2
        """
        input_data_file: str = kwargs["input_data_file"]
        input_template_name: str = kwargs["input_template_name"]
        output_file_name_jinja2: str = kwargs["output_file_name_jinja2"]

        return dict(
            input_template_name=input_template_name,
            input_data_file=input_data_file,
            output_file_name_jinja2=output_file_name_jinja2,
        )
