#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing API access functions.

Testing API access functions.
"""

import logging
from unittest.mock import MagicMock
import pytest


# from typing import Dict
from broccolini.api_access import ApiAccess
from broccolini.authentication_functions import VaultFunctions

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class TestApiAccess:
    """Test API Access functions."""

    @classmethod
    def get_test_values(cls, secret_path):
        """[Get values for use in other test functions.]
        Args:
            api_url [str]): [path to grab from vault to return url]
            api_key [str]): [path to grab from vault to return key]


        Returns:
            secret_key ([str]): [returns data from vault]
        """
        try:
            secret_key = VaultFunctions().query_vault_data(
                vault_url="VAULT_URL",
                vault_token="VAULT_TOKEN",
                secret_path=secret_path,
            )
            return secret_key["data"]["data"]["_key"]
        except KeyError as _error:  # pragma: no cover
            raise ValueError("Missing environment variables") from _error

    @staticmethod
    @pytest.fixture
    # @pytest.mark.dependency(name="test_get_api_connection")
    def test_get_api_settings(return_data_dict):
        """Test connect to api.

        input from conftest with secret path
        input_type: str
        input_url: string
        input_type: str
        side_effect: call_to_external_api
        output: my_dict
        output_type: Dict[str, str]
        """
        api_url = TestApiAccess.get_test_values(return_data_dict["api_url"])
        api_key = TestApiAccess.get_test_values(return_data_dict["api_key"])
        return dict(
            api_url=api_url,
            api_key=api_key,
        )

        # put in exception here if not getting 200

    @staticmethod
    def test_return_statistics_from_api(test_get_api_settings):
        """Test we can get statistics via the api.

        The test url is not reachable from github. Use mock.
        the key in method has to match the assert called with value given
        """
        result = ApiAccess().return_statistics_from_api(
            api_url=test_get_api_settings["api_url"],
            api_key=test_get_api_settings["api_key"],
        )
        result.method = MagicMock(return_value=4)
        result.method(api_url=test_get_api_settings["api_url"], api_key=test_get_api_settings["api_key"], key="value")
        result.method.assert_called_with(
            api_url=test_get_api_settings["api_url"], api_key=test_get_api_settings["api_key"], key="value"
        )

    @staticmethod
    def test_return_statistics_from_api_exception(test_get_api_settings):
        """Test we can get statistics via the api exception."""
        # message = "Missing environment variables"
        # with pytest.raises(ValueError, match=message):
        #     VaultFunctions.get_vault_credentials(vault_url="VAULT_URL_BAD", vault_token="VAULT_TOKEN_BAD")
        message = "Issue with url or authentication"
        with pytest.raises(ValueError, match=message):
            # put bad url and or key here
            ApiAccess().return_statistics_from_api(
                api_url=test_get_api_settings["api_url"],
                api_key="BAD_KEY_HERE",
            )


#     from unittest import TestCase
# from mock import patch # for Python >= 3.3 use unittest.mock


# # from main import url_exists


# class FetchTests(TestCase):
#     def test_returns_true_if_url_found(self):
#         with patch('requests.get') as mock_request:
#             url = 'http://google.com'

#             # set a `status_code` attribute on the mock object
#             # with value 200
#             mock_request.return_value.status_code = 200

#             self.assertTrue(url_exists(url))

#     def test_returns_false_if_url_not_found(self):
#         with patch('requests.get') as mock_request:
#                 url = 'http://google.com/nonexistingurl'

#                 # set a `status_code` attribute on the mock object
#                 # with value 404
#                 mock_request.return_value.status_code = 404

#                 self.assertFalse(url_exists(url))
