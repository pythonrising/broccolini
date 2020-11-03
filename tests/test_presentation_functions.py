#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Presentation functions.

Starting with jinja templates.
"""

import logging

from broccolini.presentation_functions import PresentationOperations


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestPresentationOperations:
    """Test Presentation Functions."""

    @staticmethod
    def test_prepare_template(presentation_settings):
        """Get test input, template and output and print.

        Args:
            Get test input, template and output and print. (str):
            get input tempalate output adn prep
        """
        result = PresentationOperations().prepare_template(
            input_data_file=presentation_settings["input_data_file"],
            input_template_name=presentation_settings["input_template_name"],
            output_file_name_jinja2=presentation_settings["output_file_name_jinja2"],
            template_folder=presentation_settings["template_folder"],
            trim_blocks=presentation_settings["trim_blocks"],
            lstrip_blocks=presentation_settings["lstrip_blocks"],
            keep_trailing_newline=presentation_settings["keep_trailing_newline"],
            autoescape_formats=presentation_settings["autoescape_formats"],
        )
        expected_type = tuple
        # print(result)
        assert isinstance(result, expected_type)
