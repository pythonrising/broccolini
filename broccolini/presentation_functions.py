"""PresentationOperation functions.

Presentation operations.
"""
import logging

from pathlib import Path
from typing import List

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template
from jinja2 import select_autoescape


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)

# use as example for how to do variables to template
# from django example
# jinja examples add to jinja templating
# class BasicListView(View):
# def get(self, request, *args, **kwargs):
#     countries = Country.objects.all()
#     context = {"country_list": countries}
#     return render(request, "list.html", context)


class PresentationOperations:
    """Presentation
    Operation Functions."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    def prepare_template_with_pathlib(
        **kwargs,
    ) -> str:
        """Prepare output using a template and dictionary.

        This function takes a dictionary and a template file and produces
        output combining the data and variables.

        Args: (called from *kwargs)
            input_dictionary (dict[str, object]): [description]
            input_template_name (str): template used to build the output
            trim_blocks: bool - jinja 2 options
            lstrip_blocks: bool - jinja 2 options
            keep_trailing_newline: bool - jinja 2 options
            autoescape_formats: list[str] = kwargs["autoescape_formats"]

        Returns:
            output_text (str): output text
        """
        input_dictionary: str = kwargs["input_dictionary"]
        input_template_name: str = kwargs["input_template_name"]
        trim_blocks: bool = kwargs["trim_blocks"]
        lstrip_blocks: bool = kwargs["lstrip_blocks"]
        keep_trailing_newline: bool = kwargs["keep_trailing_newline"]
        autoescape_formats: List[str] = kwargs["autoescape_formats"]

        path_obj: Path = Path(__file__).parent.parent / "templates"
        env: Environment = Environment(
            loader=FileSystemLoader(Path(path_obj)),
            trim_blocks=trim_blocks,
            lstrip_blocks=lstrip_blocks,
            keep_trailing_newline=keep_trailing_newline,
            autoescape=select_autoescape(autoescape_formats),
        )
        template: Template = env.get_template(input_template_name)

        return template.render(jinja_var=input_dictionary)
