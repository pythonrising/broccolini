"""PresentationOperation functions.

Presentation operations.
"""
import logging

from pathlib import Path
from typing import Any

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
    """Presentation Operation Functions.

    add
    trim_blocks
    # lstrip_blocks: bool = kwargs["lstrip_blocks"]
        # keep_trailing_newline: bool = kwargs["keep_trailing_newline"]
        autoescape_formats
    """

    def __init__(
        self,
        trim_blocks: bool = True,
        lstrip_blocks: bool = True,
        keep_trailing_newline: bool = True,
    ) -> None:
        """Init class - vars are called in the function as needed."""
        self.trim_blocks = trim_blocks
        self.lstrip_blocks = lstrip_blocks
        self.keep_trailing_newline = keep_trailing_newline

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    def prepare_template_with_pathlib(self, **kwargs: str) -> Any:  # type: ignore
        """Prepare output using a template and dictionary.

        Take dictionary and a template file.  Combine to create
        template output.

        Returns:
            output_text (str): output text
        """
        # trim_blocks = True
        # lstrip_blocks = True
        # keep_trailing_newline = False
        # autoescape_formats=["html", "xml"],

        input_dictionary: str = kwargs["input_dictionary"]
        input_template_name: str = kwargs["input_template_name"]
        # trim_blocks: bool = kwargs["trim_blocks"]
        # lstrip_blocks: bool = kwargs["lstrip_blocks"]
        # keep_trailing_newline: bool = kwargs["keep_trailing_newline"]
        autoescape_formats: str = kwargs["autoescape_formats"]

        path_obj: Path = Path(__file__).parent.parent / "templates"
        env: Environment = Environment(
            loader=FileSystemLoader(Path(path_obj)),
            trim_blocks=self.trim_blocks,
            lstrip_blocks=self.lstrip_blocks,
            keep_trailing_newline=self.keep_trailing_newline,
            autoescape=select_autoescape(autoescape_formats),
        )
        template: Template = env.get_template(input_template_name)

        return template.render(jinja_var=input_dictionary)
