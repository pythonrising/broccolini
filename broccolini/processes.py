"""ProcessOperation functions.

Process operations functions such as psutil.  Will likely rename later.
"""
import logging
import psutil
from typing import List, Tuple

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class ProcessOperations:
    """Process such as psutil."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    # def view_running_processes(**kwargs: str) -> List[Tuple[str, int]]:
    def view_running_processes() -> List[Tuple[str, int]]:
        """View Running Processes.
        input: input_data
        input_type: str
        output: list_of_files
        output_type: List[Tuple]
        """
        list_of_processes: List[Tuple[str, int]] = []
        for proc in psutil.process_iter():
            try:
                process_name: str = proc.name()
                process_id: int = proc.pid
                list_of_processes.append((process_name, process_id))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as _error:
                raise ValueError("Missing environment variables") from _error
        return list_of_processes
