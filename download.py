import os
import urllib.parse

import requests

def get_image_link(url):
    response = requests.get(url)
    response.raise_for_status()
    image_link = response.json()['img']
    author_comment = response.json()['alt']
    return image_link, author_comment


def get_total_images():
    response = requests.get("https://xkcd.com/info.0.json")
    response.raise_for_status()
    total_images = response.json()['num']
    return total_images


def download_image(url):
    parsed_url = urllib.parse.urlsplit(url)
    filename = os.path.basename(parsed_url.path)
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "wb") as file:
        file.write(response.content)
