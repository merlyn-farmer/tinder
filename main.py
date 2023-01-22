import time

from info import create_profile
from info import update_profile_proxy
from info import get_proxy_port
from info import get_proxy_host
from info import get_proxy_username
from info import get_proxy_password
from info import get_session_name
from info import update_profile_geo
from info import get_latitude
from info import get_longitude
from info import get_website
from info import get_group
import requests

for i in range(1):
    time.sleep(1)
    proxy_type = "HTTP"
    proxy_password = get_proxy_password()
    proxy_host = get_proxy_host()
    proxy_username = get_proxy_username()
    proxy_port = get_proxy_port()
    session_name = get_session_name()
    latitude = get_latitude()
    longitude = get_longitude()
    website = get_website()
    group = get_group()

    profile_id = create_profile(session_name=session_name, website=website, group=group)
    time.sleep(5)
    update_profile_proxy(profile_id=profile_id, proxy_port=proxy_port, proxy_username=proxy_username, proxy_host=proxy_host,
                         proxy_password=proxy_password, proxy_type=proxy_type)
    time.sleep(5)
    update_profile_geo(profile_id=profile_id, latitude=latitude, longitude=longitude)
