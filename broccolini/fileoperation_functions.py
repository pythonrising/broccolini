"""FileOperation functions.

File operations, eg, open close read write.
"""

import logging
from pathlib import Path
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class FileOperationFunctions:
    """File Operation Functions."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    def build_dictionary(**kwargs: Path) -> Dict[str, object]:
        """Builds dictionary of values.

        input: pathlib path object from the file system
        input_type: Path
        output: output_dict
        output_type: dict
        keys in dictionary:
            Current:
            list of files generated by pathlib
            Future:
            sending to database for now
            future can get other data from pathlib information including:
            subjects
            file_size
            modification date - from pathlib
        """
        input_path: Path = kwargs["input_path"]
        output_dict: Dict[str, object] = dict(
            folders_and_files=list(input_path.rglob("*.*")),
        )
        return output_dict

    @staticmethod
    def get_file_information_build(
        **kwargs: str,
    ) -> List[Dict[str, object]]:
        """Build data about file structure.

        input: input_directory
        input_type = input_directory
        output: output_listing
        output_type = List[str]
        """
        input_directory: str = kwargs["input_directory"]
        path = Path(input_directory)
        folder_list: List[Path] = []
        for each in path.iterdir():
            folder_list.append(each)

        output_listing: List[Dict[str, object]] = []
        for each in folder_list:
            write_to_json: Dict[str, object] = FileOperationFunctions.build_dictionary(input_path=each)
            output_listing.append(write_to_json)
        return output_listing

    # def filter_file_information(
    #     **kwargs: str,
    # ) -> Dict[str,str]:
    #     """Filter data from pathlib import.

    #     input: list of files
    #     input_type = List['windows-path-object', str]
    #     output: output_listing various functions in dictionary
    #     output_type = Dict[str]
    #     """
    #     input_directory: str = kwargs["input_list"]
    #     logging.debug(input_directory)

    #     return_dict = dict(
    #         input_directory=input_directory,
    #         original_full_path="original_full_path_here",
    #         subject="subject_name_from_file_name",
    #     )
    #     return return_dict

    # @staticmethod
    # def build_dictionary(**kwargs: Path) -> Dict[str, object]:
    #     """Builds dictionary of values.

    #     input: pathlib path object from the file system
    #     input_type: Path
    #     output: output_dict
    #     output_type: dict
    #     keys in dictionary:
    #         Current:
    #         list of files generated by pathlib
    #         Future:
    #         sending to database for now
    #         future can get other data from pathlib information including:
    #         subjects
    #         file_size
    #         modification date - from pathlib
    #     """
    #     input_path: Path = kwargs["input_path"]
    #     output_dict: Dict[str, object] = dict(
    #         folders_and_files=list(input_path.rglob("*.*")),
    #     )
    #     return output_dict

    @staticmethod
    def filter_file_data(**kwargs: str) -> Dict[str, object]:
        """Filter data."""
        input_path: str = kwargs["input_path"]
        output_dict = dict(
            input_path=input_path,
            # original_full_path="original_full_path_here",
            subject="subject_name_from_file_name",
        )
        return output_dict
