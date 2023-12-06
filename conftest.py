import pytest
import yaml
import requests

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def log_in():
    result = requests.post(url=data["url"], data={"username": data["login"], "password": data["pass"]})
    token = (result.json()["token"])
    return token


@pytest.fixture()
def add_new_post():
    res = requests.post(url=data["url_post"], headers={"X-Auth-Token": data["token"]},
                        data={"username": data["login"], "password": data["pass"], 'title': data["title"], 'description': data["descr"], 'content': data["cont"]})
    return res.json()["description"]


@pytest.fixture()
def text1():
    return data["title"]


@pytest.fixture()
def text2():
    return data["descr"]
