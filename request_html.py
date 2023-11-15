"""
Contains classes and functions pertaining to the extraction of the html content
"""

__author__ = "Moin Ahmed"


import requests
from bs4 import BeautifulSoup


def get_html_content(url: str) -> bytes:
    headers = {'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'}
    return requests.get(url, headers=headers).content


def save_html_content(content: bytes, file_name: str) -> None:
    with open(file_name, "wb") as binary_file:
        binary_file.write(content)


def extract_byte_file(file_name: str) -> bytes:
    with open(file_name, "rb") as binary_file:
        content = binary_file.read()
    return content





