"""PresentationOperation functions.

Presentation operations.
"""
import logging

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape


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
    def prepare_template(**kwargs: str) -> tuple[bool, str]:
        """Create template.
        input_data_file: file to build dictionary from
        input_template_name: str name of the template file
        output_file_name_jinja2: str - output_file_name_jinja2
        """
        input_data_file: str = kwargs["input_data_file"]
        input_template_name: str = kwargs["input_template_name"]
        # output_file_name_jinja2: str = kwargs["output_file_name_jinja2"]
        template_folder: str = kwargs["template_folder"]
        file_loader: str = FileSystemLoader(template_folder)
        trim_blocks: str = kwargs["trim_blocks"]
        lstrip_blocks: str = kwargs["lstrip_blocks"]
        keep_trailing_newline: str = kwargs["keep_trailing_newline"]
        autoescape_formats: str = kwargs["autoescape_formats"]

        env = Environment(
            loader=file_loader,
            trim_blocks=trim_blocks,
            lstrip_blocks=lstrip_blocks,
            keep_trailing_newline=keep_trailing_newline,
            autoescape=select_autoescape(autoescape_formats),
        )
        template = env.get_template(input_template_name)
        output = template.render(jinja_var=input_data_file)
        # with open(output_file_name_jinja2, "w") as file_handle:
        #     file_handle.write(output)
        return True, output
