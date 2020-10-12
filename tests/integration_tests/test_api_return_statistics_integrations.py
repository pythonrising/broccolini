#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing integration of api access."""

import logging
import pytest

from broccolini.api_access import ApiAccess

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestIntegrationFileToFauna:
    """Testing integration of api access."""

    @staticmethod
    @pytest.mark.skip(reason="needs mocking for cicd")
    def test_return_statistics_from_api(test_get_api_settings):
        """Test we can get statistics via the api.

        The test url is not reachable from github. Use mock.
        the key in method has to match the assert called with value given
        """
        result = ApiAccess().return_statistics_from_api(
            api_url=test_get_api_settings["api_url"],
            api_key=test_get_api_settings["api_key"],
        )
        expected_type = dict
        result_json = result.json()
        expected = 1000
        assert result_json["results"]["shares_good"] >= expected
        assert isinstance(result_json, expected_type)
