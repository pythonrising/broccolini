"""API Access functions.

API Access functions.
"""
import logging

import requests
from requests.models import Response

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class ApiAccess:
    """Process such as psutil."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    def return_statistics_from_api(**kwargs: str) -> Response:
        """Get data."""
        api_url: str = kwargs["api_url"]
        api_key: str = kwargs["api_key"]
        headers = {"Authorization": f"Bearer {api_key}"}

        with requests.Session() as session:
            session.headers.update(headers)
            response = session.get(api_url)
            if response.status_code != 200:
                raise ValueError("Issue with url or authentication.")
            return response
