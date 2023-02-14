import time
import sys

from info import create_profile
from info import update_profile_proxy
from info import get_proxy_port
from info import get_proxy_host
from info import get_proxy_username
from info import get_proxy_password
from info import get_session_name
from info import update_profile_geo
from GUI import Example
from GUI import QApplication
from info import get_website
from GEO import geo_coords

import requests



def get_port(port):

    numb = 8


    for i in range(numb):
        time.sleep(1)
        proxy_type = "HTTP"
        proxy_password = get_proxy_password()
        proxy_host = get_proxy_host()
        proxy_username = get_proxy_username()
        proxy_port = get_proxy_port()
        session_name = get_session_name()

        website = get_website()

        profile_id = create_profile(session_name=session_name, website=website, port=port)
        time.sleep(5)
        update_profile_proxy(profile_id=profile_id, proxy_port=proxy_port, proxy_username=proxy_username, proxy_host=proxy_host,
                             proxy_password=proxy_password, proxy_type=proxy_type, port=port)
        time.sleep(5)
        latitude, longitude = geo_coords()
        update_profile_geo(profile_id=profile_id, latitude=latitude, longitude=longitude, port=port)

get_port(port="34800")

#   Multilogin  34800
#   Indigo      34575

