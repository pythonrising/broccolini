#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing common functions.

Testing common access functions.
"""


import logging

from broccolini.common import get_authentication_values


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


def test_get_authentication_values(return_data_dict):
    """Get authentication values."""

    result = get_authentication_values(
        secret_path=return_data_dict["twilio_notify_number"],
    )
    expected = "5716859313"
    expected_type = str
    assert isinstance(result, expected_type)
    assert expected == result
