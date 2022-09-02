import os
import urllib.parse

import requests


def get_total_images():
    response = requests.get("https://xkcd.com/info.0.json")
    response.raise_for_status()
    total_images = response.json()['num']
    return total_images


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    xkcd_answer = response.json()
    image_link = xkcd_answer['img']
    author_comment = xkcd_answer['alt']
    parsed_url = urllib.parse.urlsplit(image_link)
    filename = os.path.basename(parsed_url.path)
    response = requests.get(image_link)
    response.raise_for_status()
    with open(filename, "wb") as file:
        file.write(response.content)
    return filename, author_comment
