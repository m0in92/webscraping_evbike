"""
Contains classes and functions for parsing html content
"""

__author__ = "Moin Ahmed"

import json

from request_html import get_html_content, save_html_content, extract_byte_file


def search_for_saved_filename(url: str, info: dict) -> int:
    for i, url_in_info in enumerate(info.keys()):
        if url == url_in_info:
            return i
    return -1


def get_saved_filename_alias() -> dict:
    file_name = 'dict_filenames.json'
    with open(file_name, "r") as json_file:
        info = json.load(json_file)
    return info


def dump_saved_filenames_alias(new_dict: dict) -> None:
    file_name = 'dict_filenames.pkl'
    with open(file_name, "w") as pickle_file:
        json.dump(dict, pickle_file, indent=4,
                        separators=(',',': '))


def create_name_for_filename(string: str):
    return "".join(char for char in string.split('/')[-1] if char.isalnum())


def extract_parsed_html_content(url: str):
    info = get_saved_filename_alias()
    print(info.values())
    if url in info.keys():
        info_index = search_for_saved_filename(url=url, info=info)
        file_name = list(info.values())[info_index]
        html_content = extract_byte_file(file_name=file_name)
        print(f'html content was extracted from the saved file named {file_name}')
    else:
        html_content = get_html_content(url=url)
        file_name = create_name_for_filename(string=url)
        save_html_content(content=html_content, file_name=file_name)
        info.update({url: file_name})
        dump_saved_filenames_alias(new_dict=info)
        print(f"Extracted html from a new source. Created a filename: {file_name}")
    return html_content


# print(get_saved_filename_alias())
extract_parsed_html_content(url='https://ebicycle-db.com//brands/aventon?category=electric-bicycle')


