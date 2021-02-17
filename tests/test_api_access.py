#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing API access functions.

Testing API access functions.
"""

import logging

from unittest import TestCase, mock

from broccolini.api_access import ApiAccess


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestWorkerModule(TestCase):
    """Mock API functions."""

    @staticmethod
    def test_return_statistics_from_api():  # pragma: no cover
        """Patch example for use in other mocking tests."""
        with mock.patch(
            # from broccolini.api_access import ApiAccess
            "broccolini.api_access.ApiAccess.return_statistics_from_api"
        ) as mock_helper:
            mock_helper.return_value.broccolini.api_access.return_statistics_from_api.return_value = (
                "testing"
            )
            ApiAccess.return_statistics_from_api()
            # ApiAccess.return_statistics_from_api("input_dictionary=input_dict")
            mock_helper.assert_called_once()
            # mock_helper.assert_called_once_with("input_dictionary=input_dict")
            # return_statistics_from_api


# class TestApiAccess:
#     """Test API Access functions."""

#     @staticmethod
#     @pytest.fixture
#     @pytest.mark.dependency(name="test_get_api_settings")
#     def test_get_api_settings(return_data_dict):  # pragma: no cover
#         """Test connect to api.

#         input from conftest with secret path
#         input_type: str
#         input_url: string
#         input_type: str
#         side_effect: call_to_external_api
#         output: my_dict
#         output_type: Dict[str, str]
#         """
#         api_url = get_authentication_values(return_data_dict["api_url"])
#         api_key = get_authentication_values(return_data_dict["api_key"])

#         return dict(api_url=api_url, api_key=api_key)

# def test_return_statistics_from_api(return_data_dict):  # pragma: no cover
#     """Test connect to api."""
#     result = ApiAccess().return_statistics_from_api()
#     result = ApiAccess()
#     print(result)


#     @staticmethod
#     def test_return_statistics_from_api_mock(_mocked_api_access):  # pragma: no cover
#         Test we can get statistics via the api.

#         The test url is not reachable from github. Use mock.
#         the key in method has to match the assert called with value given
#         """
#         result = ApiAccess().return_statistics_from_api()
#         expected = True
#         expected_type = bool
#         assert isinstance(result, expected_type)
#         assert expected == result


# @pytest.fixture
# def _mocked_api_access(mocker):  # pragma: no cover
#     """Use for mocking variables."""
#     mock_api_access = mocker.patch.object(
#         ApiAccess, "return_statistics_from_api", autospec=True
#     )
#     mock_api_access.return_value = True
#     return mock_api_access
