import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


# result = requests.post(url=data["url"], data={"username": data["login"], "password": data["pass"]})
# token = (result.json()["token"])

def auth_token(token):
    res_get = requests.get(url=data["url_post"], headers={"X-Auth-Token": token}, params=data["owner"])
    title_list = [item["title"] for item in res_get.json()["data"]]
    return title_list


def auth_token2(token):
    res2_get = requests.get(url=data["url_post"], headers={"X-Auth-Token": token}, params=data["owner"])
    des_list = [item["description"] for item in res2_get.json()["data"]]
    return des_list


def test_step1(log_in, add_new_post, text1):
    assert text1 in auth_token(log_in), "not found"


def test_step2(log_in, add_new_post, text2):
    assert text2 in auth_token2(log_in), "not found"
