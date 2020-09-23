"""FileOperation functions.

File operations, eg, open close read write.
"""

import logging
import re
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

    # def is_this_valid_subject(self) -> bool:
    #     """Filter data.
    #     do 1 or 2 tests
    #     is the text followed by training/*
    #     does the training meet one of these group
    #     """
    #     input_subject_name = self.possible_subject_name
    #     valid_subjects = ['python', 'javascript', 'ml', 'ai', 'network', 'general']

    @staticmethod
    def filter_subject_from_list(**kwargs: str) -> List[Dict[str, object]]:
        """When given list of parents in pathlib format - search for the line we need

        Given list like this:
        WindowsPath('C:/Users/bachs1x/AppData/Local/Temp/pytest-of-bachs1x/pytest-690/test_dir_created0/
        test_dir_created/training/network/subdir_3'),
        get the text following training/
        input: list_of_pathlib_files
        input_type = List[Pathlib]
        Note - return on first match is good because the list refers to the same path
        """
        pattern = str = kwargs["pattern"]
        input_list: List[Path] = kwargs["input_list"]
        for each in input_list:
            # print(f"line from list is {each}")
            # print(f"pattern is {pattern}")
            pattern = re.compile(pattern)
            match = re.match(pattern, each)
            if (match := re.match(pattern, each)) is not None:
                # print(f"entire string:{match[0]}:")
                # print(f"just the first matched group:{match[1]}:")
                return match[1]
            else:
                return f"no match on {each}"
        # return pattern, input_list

    @staticmethod
    def filter_file_data(**kwargs: str) -> List[Dict[str, object]]:
        """Filter data.

        input: dictionary_of_paths_in_pathlib_format
        input_type = input_directory
        output: output_dictionary
        output_type = List[Dict[str, str]]
        # to get the subject
        # do a quick regex to find the parent after the text created/training/TEXTHEREISWHATWEWANT
        # -bachs1x/pytest-669/test_dir_created0/test_dir_created/training/javascript/subdir_3/seek.txt')
        x = "Success!" if (y == 2) else "Failed!"
        x = "valid" if in list else failed  or do a dictionary lookup of the valid subjects
        """
        input_path: Dict[List[str]] = kwargs["input_path"]
        # subject = 'unknown_subject'
        records_to_add = []
        for each in input_path["folders_and_files"]:
            records_to_add.append(
                dict(
                    file_name=each.name,
                    file_suffix=each.suffix,
                    parent_dir=each.parent,
                    creation_time=each.stat().st_ctime,
                    mod_time=each.stat().st_mtime,
                    size=each.stat().st_size,
                    # size=each.each.stat().st_size,
                    parent_dir_up_2=each.parent.parent,
                    parent_dir_up_3=each.parent.parent.parent,
                    parent_list=list(each.parents),
                )
            )
        return records_to_add
