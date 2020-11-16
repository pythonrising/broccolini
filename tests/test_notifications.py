#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing notification files using classes.

Testing notifications including twilio.
"""
import logging

import pytest

from twilio.rest import Client

from broccolini.common import get_authentication_values
from broccolini.notifications import TwilioFunctions


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestTwilioFunctions:
    """Test Twilio Functions."""

    @staticmethod
    @pytest.mark.dependency(name="test_login_to_twilio")
    def test_get_twilio_connection(return_data_dict):
        """Test login to twilio.

        input: auth_token
        input_type: str
        twilio_path_auth_token="greg_production/twilio_data/TWILIO_AUTH_TOKEN",
        output: twilio client
        """
        account_sid = get_authentication_values(
            secret_path=return_data_dict["twilio_account_sid"]
        )
        auth_token = get_authentication_values(return_data_dict["twilio_auth_token"])

        result = TwilioFunctions(account_sid, auth_token).get_twilio_connection()
        expected_type = Client
        assert isinstance(result, expected_type)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_twilio"])
    def test_send_twilio_notification(return_data_dict):
        """Test send twilio notification."""
        account_sid = get_authentication_values(
            secret_path=return_data_dict["twilio_account_sid"]
        )
        auth_token = get_authentication_values(return_data_dict["twilio_auth_token"])

        twilio_phone_number = get_authentication_values(
            return_data_dict["twilio_phone_number"]
        )

        twilio_notify_number = get_authentication_values(
            return_data_dict["twilio_notify_number"]
        )

        this = TwilioFunctions(account_sid, auth_token)
        result = this.send_twilio_notification(
            written_directories=return_data_dict["written_directories"],
            twilio_phone_number=twilio_phone_number,
            twilio_notify_number=twilio_notify_number,
        )
        expected_type = str
        assert isinstance(result, expected_type)
