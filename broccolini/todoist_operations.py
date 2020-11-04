"""TodoistOperation functions.

Todoist is a todo list application.
"""
import logging

from todoist import TodoistAPI


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TodoIstOperations:
    """T Operation Functions."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    def todoist_get_connection(**kwargs: str) -> str:
        """[summary]

        Returns:
            str: [description]
        """
        todoist_api_token: str = kwargs["todoist_api_token"]
        try:
            api = TodoistAPI(todoist_api_token)
            api.sync()
            return api

        except Exception as _error:  # pragma: no cover
            raise ValueError("Todoist error.") from _error

    def list_all_items(self) -> list[str]:  # pragma: no cover
        """List todoist items."""
        api = self.todoist_get_connection()
        return api.state["items"]
