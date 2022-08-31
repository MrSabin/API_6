import requests
from environs import Env
from pathlib import Path


def get_groups_info(token):
    method = "groups.get"
    api_version = "5.131"
    payload = {
            "access_token": token,
            "v": api_version
            }
    url = f"https://api.vk.com/method/{method}"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.json())


def get_upload_url(token, group_id):
    method = "photos.getWallUploadServer"
    api_version = "5.131"
    payload = {
            "group_id": group_id,
            "access_token": token,
            "v": api_version
            }
    url = f"https://api.vk.com/method/{method}"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()['response'].get('upload_url')


def send_image(upload_url):
    path = Path.cwd() / 'images' / 'comix.png'
    with open(path, 'rb') as file:
        files = {"photo": file}
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
    server = response.json()['server']
    photo = response.json()['photo']
    hash = response.json()['hash']
    return server, photo, hash


def save_image(token, group_id, server, photo, hash):
    method = "photos.saveWallPhoto"
    api_version = "5.131"
    payload = {
            "access_token": token,
            "group_id": group_id,
            "server": server,
            "photo": photo,
            "hash": hash,
            "v": api_version
            }
    url = f"https://api.vk.com/method/{method}" 
    response = requests.post(url, params=payload)
    response.raise_for_status()
    image_id = response.json()['response'][0]['id']
    image_owner_id = response.json()['response'][0]['owner_id']
    return image_id, image_owner_id


def post_image():
    method = "wall_post"
    url = f"https://api.vk.com/method/{method}" 


def main():
    env = Env()
    env.read_env()

    group_id = "215609822"
    vk_access_token = env.str("VK_ACCESS_TOKEN")

    upload_url = get_upload_url(vk_access_token, group_id)
    server, photo, hash = send_image(upload_url)
    save_image(vk_access_token, group_id, server, photo, hash)

if __name__ == "__main__":
    main()

