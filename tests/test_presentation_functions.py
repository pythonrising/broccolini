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
    def test_prepare_template():
        """Get test input, template and output and print.

        Args:
            Get test input, template and output and print. (str):
            get input tempalate output adn prep
        """
        result = PresentationOperations().prepare_template(
            output_file_name="rilaefsdf.txt",
        )
        expected_type = str
        assert isinstance(result, expected_type)
