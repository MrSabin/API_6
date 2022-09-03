import requests
from environs import Env
from pathlib import Path
from download import download_comics, get_total_images
import random
import os


def get_upload_url(token, group_id):
    method = "photos.getWallUploadServer"
    api_version = "5.131"
    payload = {"group_id": group_id, "access_token": token, "v": api_version}
    url = f"https://api.vk.com/method/{method}"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()["response"].get("upload_url")


def send_to_server(upload_url, filename):
    path = Path.cwd() / filename 
    with open(path, "rb") as file:
        files = {"photo": file}
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
    vk_api_answer = response.json()
    vk_server = vk_api_answer["server"]
    vk_photo = vk_api_answer["photo"]
    vk_hash = vk_api_answer["hash"]
    return vk_server, vk_photo, vk_hash


def save_in_album(token, group_id, server, photo, hash):
    method = "photos.saveWallPhoto"
    api_version = "5.131"
    payload = {
        "access_token": token,
        "group_id": group_id,
        "server": server,
        "photo": photo,
        "hash": hash,
        "v": api_version,
    }
    url = f"https://api.vk.com/method/{method}"
    response = requests.post(url, params=payload)
    response.raise_for_status()
    vk_api_answer = response.json()
    image_id = vk_api_answer["response"][0]["id"]
    image_owner_id = vk_api_answer["response"][0]["owner_id"]
    return image_id, image_owner_id


def post_on_wall(token, owner_id, image_id, image_owner_id, message):
    method = "wall.post"
    api_version = "5.131"
    url = f"https://api.vk.com/method/{method}"
    attachments = f"photo{image_owner_id}_{image_id}"
    payload = {
        "access_token": token,
        "owner_id": f"-{owner_id}",
        "from_group": 1,
        "attachments": attachments,
        "message": message,
        "v": api_version,
    }
    response = requests.post(url, params=payload)
    response.raise_for_status()


def main():
    env = Env()
    env.read_env()
    group_id = env.str("VK_GROUP_ID")
    vk_access_token = env.str("VK_ACCESS_TOKEN")
    total_images = get_total_images()
    comics_number = random.randint(1, total_images)
    filename, author_comment = download_comics(comics_number)
    upload_url = get_upload_url(vk_access_token, group_id)
    vk_server, vk_photo, vk_hash = send_to_server(upload_url, filename)
    image_id, image_owner_id = save_in_album(
        vk_access_token, group_id, vk_server, vk_photo, vk_hash
    )
    try:
        post_on_wall(vk_access_token, group_id, image_id, image_owner_id, author_comment)
    finally:
        os.remove(filename)


if __name__ == "__main__":
    main()
