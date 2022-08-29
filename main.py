import requests
from environs import Env


env = Env()
env.read_env()
vk_access_token = env.str("VK_ACCESS_TOKEN")
method = "groups.get"
api_version = "5.131"
payload = {
        "access_token": vk_access_token,
        "v": api_version
        }
url=f"https://api.vk.com/method/{method}"

response = requests.get(url, params=payload)
response.raise_for_status()
print(response.json())
