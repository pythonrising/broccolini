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
    """Test Presentation Functions.

    plan
    jinja template
    input template
    input data
    output text
    then output pdfs.
    """

    @staticmethod
    def test_prepare_template(return_data_dict):
        """Get test input, template and output and print.

        Args:
            Get test input, template and output and print. (str):
            get input tempalate output adn prep
        """
        result = PresentationOperations().prepare_template(
            input_data_file=return_data_dict["input_data_file"],
            input_template_name=return_data_dict["input_template_name"],
            output_file_name_jinja2=return_data_dict["output_file_name_jinja2"],
        )
        expected_type = dict
        print(result)
        assert isinstance(result, expected_type)
