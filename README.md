# Description

Goal of this script to achieve random comix from [xkcd](xkcd.com) and post it to specified VK group.

## Installation

Python should be already installed.

1. Download this repo
2. Run `python pip install -r requirements.txt` to install all dependencies.

## Before run

1. Authorize on [VK](vk.com)
2. Create your group (you can do it [here](https://vk.com/groups?tab=admin&w=groups_create)) or use existing
3. Create your app on [VK Dev](https://vk.com/dev), use `standalone` option
4. Acquire `client_id` of your app by clicking `Edit` in [app page](https://vk.com/apps?act=manage). `client_id` will be in address bar
5. Acquire personal token following [this guide](https://dev.vk.com/api/access-token/implicit-flow-user)
6. Acquire your group_id, [this will help](https://regvk.com/id/)
7. Create .env file in repo directory, and write all gathered info in there, like:

```python
VK_GROUP_ID="your_group_id"
VK_ACCESS_TOKEN="your_token"
```
Example of file you will find in repo, feel free to use it

## Run script

Now you can run script by command:

```python
python main.py
```
## Project goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](dvmn.org)
