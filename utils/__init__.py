import random
from os import getcwd

from aiohttp import http

__version__ = "4.1.5"
APP_VERSION = __version__
HOME_DIR = getcwd()
__all__ = [__version__, APP_VERSION]


def generate_random_string():
    length = random.randint(10, 30)
    rand_str = ''
    range_start = 48
    range_end = 122

    for _ in range(length):
        random_integer = random.randint(range_start, range_end)
        # Validate ascii range
        if random_integer <= 57 or random_integer >= 65:
            rand_str += chr(random_integer)

    return rand_str


def block_aiohttp_version():
    # 随机响应头，迷惑网络探测，降低在网络中的存在感
    http.SERVER_SOFTWARE = generate_random_string()


block_aiohttp_version()
