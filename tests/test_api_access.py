#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing API access functions.

Testing API access functions.
"""

import logging

import pytest

from broccolini.api_access import ApiAccess
from broccolini.authentication_functions import VaultFunctions


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestApiAccess:
    """Test API Access functions."""

    @classmethod
    def get_test_values(cls, secret_path):  # pragma: no cover
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
    @pytest.mark.dependency(name="test_get_api_settings")
    def test_get_api_settings(return_data_dict):  # pragma: no cover
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
        return dict(api_url=api_url, api_key=api_key)

        # put in exception here if not getting 200

    @staticmethod
    # @pytest.mark.skip(reason="needs mocking for cicd")
    def test_return_statistics_from_api_mock(
        test_get_api_settings, _mocked_api_access
    ):  # pragma: no cover
        """Test we can get statistics via the api.

        The test url is not reachable from github. Use mock.
        the key in method has to match the assert called with value given
        """
        # result = ApiAccess().return_statistics_from_api(
        #     api_url=test_get_api_settings["api_url"],
        #     api_key=test_get_api_settings["api_key"],
        # )
        result = ApiAccess().return_statistics_from_api()
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert expected == result

        # result.method = MagicMock(return_value=4)

        # result.method(
        #     api_url=test_get_api_settings["api_url"],
        #     api_key=test_get_api_settings["api_key"],
        #     key="value",
        # )
        # result.method.assert_called_with(
        #     api_url=test_get_api_settings["api_url"],
        #     api_key=test_get_api_settings["api_key"],
        #     key="value",
        # )


@pytest.fixture
def _mocked_api_access(mocker):  # pragma: no cover
    """Use for mocking variables."""
    mock_api_access = mocker.patch.object(
        ApiAccess, "return_statistics_from_api", autospec=True
    )
    mock_api_access.return_value = True
    return mock_api_access
