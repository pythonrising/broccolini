#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing API access functions.

Testing API access functions.
"""

import logging
# from typing import Dict
from broccolini.api_access import ApiAccess

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class TestApiAccess:
    """Test API Access functions."""

    @staticmethod
    def test_connect_to_api():
        """Test connect to api.

        input from conftest with secret path
        input_type: str
        input_url: string
        input_type: str
        side_effect: call_to_external_api
        output: my_dict
        output_type: Dict[str, str]
        """
        result = ApiAccess().connect_to_api()
        # expected = "ystem"
        # expected_type = list
        # # assert expected == result[0][0]
        # assert expected in result[0][0]
        # assert isinstance(result, expected_type)
        logging.debug(result)
        # print(result)

    @staticmethod
    def test_view_running_processes2():
        """Test view running processes."""
        result = ApiAccess().connect_to_api_updated()
        logging.debug(result)
        # expected_type = str
        # assert isinstance(result, expected_type)
