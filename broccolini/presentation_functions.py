"""PresentationOperation functions.

Presentation operations.
"""
import logging

from pathlib import Path

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
    def prepare_template_with_pathlib(
        **kwargs: str,
    ) -> tuple[bool, str]:
        """Given a path to templates, a file name and a dictionary

        Prepare a final template
        examples input_dictionary: dict[str, object], input_template: str,

        Args: (called from *kwargs)
            input_dictionary (dict[str, object]): [description]
            input_template_file_name (str): template used to build the output
            output_text (str): output text

        Returns:
            tuple[bool, str]: true for success, and the name of the output_file_name

        """
        input_dictionary = kwargs["input_dictionary"]
        input_template_name = kwargs["input_template_name"]
        # file_loader: str = FileSystemLoader(template_folder)
        trim_blocks: str = kwargs["trim_blocks"]
        lstrip_blocks: str = kwargs["lstrip_blocks"]
        keep_trailing_newline: str = kwargs["keep_trailing_newline"]
        autoescape_formats: str = kwargs["autoescape_formats"]

        path_obj = Path(__file__).parent.parent / "templates"  # sample relative path
        env = Environment(
            loader=FileSystemLoader(Path(path_obj)),
            trim_blocks=trim_blocks,
            lstrip_blocks=lstrip_blocks,
            keep_trailing_newline=keep_trailing_newline,
            autoescape=select_autoescape(autoescape_formats),
        )
        template = env.get_template(input_template_name)
        output = template.render(jinja_var=input_dictionary)
        return True, output
