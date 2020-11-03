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
        result = PresentationOperations().prepare_template_with_pathlib(
            input_dictionary=presentation_settings["template_dict_values"],
            input_template_name=presentation_settings["input_template_name"],
            trim_blocks=presentation_settings["trim_blocks"],
            lstrip_blocks=presentation_settings["lstrip_blocks"],
            keep_trailing_newline=presentation_settings["keep_trailing_newline"],
            autoescape_formats=presentation_settings["autoescape_formats"],
        )
        expected = "long_description_from_conftest"
        expected_type = str
        assert isinstance(result, expected_type)
        assert expected in result
