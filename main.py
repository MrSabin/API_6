import requests
from environs import Env


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


def get_upload_address(token, group_id):
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


def main():
    env = Env()
    env.read_env()
    group_id = "215609822"
    vk_access_token = env.str("VK_ACCESS_TOKEN")
    upload_url = get_upload_address(vk_access_token, group_id)


if __name__ == "__main__":
    main()
