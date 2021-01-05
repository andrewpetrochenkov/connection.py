__all__ = ['check']


import requests

TIMEOUT = 5
URL = 'http://www.google.com/'


def check(timeout=None, url=None):
    """return True if connection is ok, else False"""
    if not timeout:
        timeout = TIMEOUT
    if not url:
        url = URL
    try:
        requests.get(url=URL, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
    except requests.exceptions.ReadTimeout:
        False
    return False
