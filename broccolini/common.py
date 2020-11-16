"""Common functions."""

import logging

from typing import Any

from broccolini.authentication_functions import VaultFunctions


# from typing import Union


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


def get_authentication_values(secret_path: str) -> Any:
    """Authenticate and get authentication data."""
    try:
        secret_key = VaultFunctions().query_vault_data(
            vault_url="VAULT_URL",
            vault_token="VAULT_TOKEN",
            secret_path=secret_path,
        )
        return secret_key["data"]["data"]["_key"]

    except KeyError as _error:  # pragma: no cover
        raise ValueError("Missing environment variables") from _error


FILE_NAME = "__input_files\\emailtestfile.txt"
ASYNC_FILENAME = "async_file1.txt"
LOGOUTPUTFILE = "__output_files\\logging_results.log"
EMAIL_PATTERN = r"[\w\.-]+@[\w\.-]+"

file_handler = logging.FileHandler(LOGOUTPUTFILE)
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
file_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
