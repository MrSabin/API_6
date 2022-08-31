import os
import urllib.parse
from pathlib import Path

import requests

def get_image_link(url):
    response = requests.get(url)
    response.raise_for_status()
    image_link = response.json().get("img")
    author_comment = response.json().get("alt")
    return image_link, author_comment


def download_image(url, path, name, payload=None):
    Path(path).mkdir(parents=True, exist_ok=True)
    extension = extract_extension(url)
    filename = Path(path, f"{name}{extension}")
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(filename, "wb") as file:
        file.write(response.content)


def extract_extension(url):
    parsed = urllib.parse.urlsplit(url)
    unquoted = urllib.parse.unquote(parsed.path)
    return os.path.splitext(unquoted)[-1]

