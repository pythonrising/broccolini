"""TodoistOperation functions.

Todoist is a todo list application.
"""
import logging

from typing import List

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
    def todoist_get_connection(**kwargs: str) -> TodoistAPI:
        # def todoist_get_connection(**kwargs):
        # def todoist_get_connection(**kwargs: str) -> str:
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

    def list_items(self, **kwargs: str) -> TodoistAPI:
        """List todoist items."""
        try:

            todoist_api_token: str = kwargs["todoist_api_token"]
            api: TodoistAPI = self.todoist_get_connection(
                todoist_api_token=todoist_api_token,
            )
            print(type(api))
            return api.state["items"]

        except Exception as _error:  # pragma: no cover
            raise ValueError("Todoist error.") from _error

    def list_projects(self, **kwargs: str) -> TodoistAPI:
        """List todoist items."""
        try:
            todoist_api_token: str = kwargs["todoist_api_token"]
            api: TodoistAPI = self.todoist_get_connection(
                todoist_api_token=todoist_api_token,
            )
            return api.state["projects"]

        except Exception as _error:  # pragma: no cover
            raise ValueError("Todoist error.") from _error

    def filter_items(self, **kwargs: str) -> List[TodoistAPI]:
        """Filter todoist items.

        Returns:
            list[list[str]]: [description]
        """
        try:
            todoist_api_token: str = kwargs["todoist_api_token"]
            data = self.list_items(
                todoist_api_token=todoist_api_token,
            )

            item_list: List[TodoistAPI] = []
            for each in data:
                item_list.append(each["content"])
            return item_list

        except Exception as _error:  # pragma: no cover
            raise ValueError("Todoist error.") from _error
