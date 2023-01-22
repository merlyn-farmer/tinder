import time
import json
import requests
import itertools
import random
from selenium import webdriver
import pyautogui as pg
from selenium.webdriver.common.by import By


def get_session():
    with open("sessions", "r") as f:
        list_sessions = f.readlines()
        session = list_sessions[0].strip()

    with open("sessions", "w") as f:
        new_list = list_sessions[1:]
        content = "".join(new_list)
        f.write(content)

        return session

def get_session_name():
    with open("session_names", "r", encoding="utf-8") as f:
        session_names = f.readlines()
        session_name = session_names[0].strip()

    with open("session_names", "w", encoding="utf-8") as f:
        new_list = session_names[1:]
        content = "".join(new_list)
        f.write(content)

        return session_name


def create_driver(session):
        mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId=' + session
        resp = requests.get(mla_url)
        json = resp.json()
        print(json)
        driver = webdriver.Remote(command_executor=json['value'])
        return driver


def get_longitude():
    with open("geo/longitudes", "r") as f:
        longitudes = f.readlines()
        longitude = longitudes[0].strip()

    with open("geo/longitudes", "w") as f:
        new_list = longitudes[1:]
        content = "".join(new_list)
        f.write(content)

        return longitude

def get_latitude():
    with open("geo/latitudes", "r") as f:
        latitudes = f.readlines()
        latitude = latitudes[0].strip()

    with open("geo/latitudes", "w") as f:
        new_list = latitudes[1:]
        content = "".join(new_list)
        f.write(content)

        return latitude


def get_name():
    with open("names", "r") as f:
        list_names = f.readlines()
        name = list_names[0].strip()

    with open("names", "w") as f:
        new_list = list_names[1:]
        content = "".join(new_list)
        f.write(content)

        return name


def get_website():
    with open("websites", "r") as f:
        website = f.readline()
        websites = website[0].strip()

        return website

def get_group():
    with open("group", "r") as f:
        group = f.readline()
        groups = group[0].strip()

        return group

def update_profile_proxy(profile_id, proxy_type, proxy_host, proxy_port, proxy_username, proxy_password):
    url = 'http://localhost:35000/api/v2/profile/' + profile_id
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "network": {
            "proxy": {
                "type": proxy_type,
                "host": proxy_host,
                "port": proxy_port,
                "username": proxy_username,
                "password": proxy_password,
            }
        }
    }
    r = requests.post(url, json.dumps(data), headers=header)
    print(r.status_code)


def update_profile_group(profile_id, group_id):
    url = 'http://localhost:35000/api/v2/profile/' + profile_id
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "group": group_id,
}
    r = requests.post(url, json.dumps(data), headers=header)
    print(r.status_code)

def update_profile_geo(profile_id, latitude, longitude):
    url = 'http://localhost:35000/api/v2/profile/' + profile_id
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "mediaDevices": {
            "mode": "REAL"
        },
        "geolocation": {
            "mode": "PROMPT",
            "fillBasedOnExternalIp": False,
            "lat": latitude,
            "lng": longitude,
            "accuracy": "100"
        }
    }
    r = requests.post(url, json.dumps(data), headers=header)
    print(r.status_code)

def create_profile(session_name, website, group):
    x = {
        "name": f"{session_name}",
        "browser": "mimic",
        "os": "win",
        "enableLock": True,
        "startUrl": f"{website}",
        "group": f"{group}"


    }
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    url = "http://localhost:35000/api/v2/profile"
    req = requests.post(url, data=json.dumps(x), headers=header)

    return json.loads(req.content).get("uuid")

def get_proxy_password():
    with open("proxy/password", "r") as f:
        proxy_passwords = f.readlines()
        proxy_password = proxy_passwords[0].strip()

        return proxy_password


def get_proxy_port():
    with open("proxy/port", "r") as f:
        proxy_ports = f.readlines()
        proxy_port = proxy_ports[0].strip()

    with open("proxy/port", "w") as f:
        new_list = proxy_ports[1:]
        content = "".join(new_list)
        f.write(content)

        return proxy_port


def get_proxy_username():
    with open("proxy/username", "r") as f:
        proxy_usernames = f.readlines()
        proxy_username = proxy_usernames[0].strip()

        return proxy_username

def get_proxy_host():
    with open("proxy/host", "r") as f:
        proxy_hosts = f.readlines()
        proxy_host = proxy_hosts[0].strip()

        return proxy_host





