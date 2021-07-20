__all__ = ['check']


from typing import Union

import requests


def check(url: str = 'https://www.example.com', timeout: Union[int, float] = 5) -> bool:
    """Check for an internet connection. Return True if connection works.
The default URL is https://www.example.com, and the default timeout value is 5."""
    try:
        requests.head(url=URL, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.exceptions.ReadTimeout):
        return False
