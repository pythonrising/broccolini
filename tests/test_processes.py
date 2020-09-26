#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Database operations functions.

Testing common Database operations. Starting with www.faunadb.com.
"""

import logging
from broccolini.processes import ProcessOperations

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class TestProcessOperations:
    """Test Process OperationsFunctions."""

    @staticmethod
    def test_view_running_processes():
        """Test view running processes."""
        result = ProcessOperations().view_running_processes(
            # input_data='greg',
        )
        expected = "System Idle Process"
        expected_type = list
        assert expected == result[0][0]
        assert isinstance(result, expected_type)
        import pprint as pp
        pp.pprint(result)


        # print(result)
        logging.debug(result)
