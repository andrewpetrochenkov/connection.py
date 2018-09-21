#!/usr/bin/env python
from public import public
import requests

TIMEOUT = 5
URL = 'http://www.google.com/'

@public
def check(timeout=None):
    if not timeout:
        timeout = TIMEOUT
    try:
        requests.get(URL, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
    return False

