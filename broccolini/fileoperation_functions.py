"""FileOperation functions.

File operations, eg, open close read write.
"""
import logging
import re

from pathlib import Path
from typing import Dict
from typing import List


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


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
        input_dict: Path = kwargs["input_dict"]
        output_dict: Dict[str, object] = dict(
            folders_and_files=list(input_dict.rglob("*.*")),
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
            write_to_json: Dict[str, object] = FileOperationFunctions.build_dictionary(
                input_dict=each
            )
            output_listing.append(write_to_json)
        return output_listing

    @staticmethod
    def filter_subject_from_list(**kwargs: str) -> str:
        """When given list of parents in pathlib format - search for the relevant line

        Note - return on first match is good because the list refers to the same path

        input: list_of_pathlib_files
        input_type = List[Path]
        output: match[1]
        output_type: str
        """
        subject = "subject_not_available"
        input_list = kwargs["input_list"]
        pattern = kwargs["pattern"]
        regexp = re.compile(pattern)

        for each in input_list:
            path = Path(each)
            text_path_name = str(path.resolve())
            match = re.match(regexp, text_path_name)
            if (match := re.match(regexp, text_path_name)) is not None:
                subject = match[1]
            else:
                subject = "subject_not_available"
        return subject

    @staticmethod
    def filter_file_data(**kwargs: Dict[str, List[Path]]) -> List[Dict[str, object]]:
        """Filter data.

        input: dictionary_of_paths_in_pathlib_format
        input_type = input_directory

        output: output_dictionary
        output_type = TBD
        # to get the subject
        # regex to find the parent after the text created/training/TEXTHEREISWHATWEWANT
        # -bachs1x/pytest-669/
        # test_dir_created0/test_dir_created/training/javascript/subdir_3/seek.txt')
        x = "Success!" if (y == 2) else "Failed!"
        x = "valid" if in list else failed or dictionary lookup of the valid subject
        """
        # input_path: Dict[List[str], Dict[str, object]] = kwargs["input_path"]
        input_dict = kwargs["input_dict"]
        # print(input_dict)
        # print(type(input_dict))
        records_to_add = []
        for each in input_dict["folders_and_files"]:
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


# def search_for_text(
#     pattern: str, data_to_search: str, file_name: str = None
# ) -> list[str]:
#     """Search for text in files given.

#     Args:
#         pattern (str): pattern to search for
#         data_to_search (str): data we are searching in
#         input_file_name (str): file name being used (Optional)

#     Returns:
#         list[str]: [description]
#     """
#     matched_string = ""
#     matched_line = ""
#     list_of_results = []

#     try:
#         if (search := re.search(pattern, data_to_search)) is not None:
#             matched_string = search[0]
#             matched_line = search[1]
#             list_of_results.append(
#                 dict(
#                     file_name=file_name,
#                     pattern=pattern,
#                     matched_string=matched_string,
#                     matched_line=matched_line,
#                 )
#             )
#     except Exception as _error:
#         logging.debug(_error)

#     # print(len(list_of_results))
#     return list_of_results


# async def read_data_async(file_name: str, output_folder: str = None) -> None:
#     """Read data and process with async."""
#     try:
#         async with aiofiles.open(file_name, encoding="utf-8") as afp:
#             data_ = await afp.read(4096)
#             results = search_for_text(pattern=PATTERN,
# data_to_search=data_, file_name=file_name)
#             if len(results) == 1:
#                 print(results)
#                 return results

#     except Exception as _error:
#         print(f"error is _{_error} for file_name = {file_name}")
#         # with open(output_folder, "a") as file_target:
#         #     file_target.write(f"error is _{_error} for file_name = {file_name}")
