"""
For using redis more easily.
"""

from importlib.metadata import version

__version__ = version("k3redisutil")

from .redis_proxy_cli import (
    KeyNotFoundError,
    RedisProxyClient,
    RedisProxyError,
    SendRequestError,
    ServerResponseError,
)
from .redisutil import (
    RedisChannel,
    get_client,
    normalize_ip_port,
    wait_serve,
)

__all__ = [
    "KeyNotFoundError",
    "RedisChannel",
    "RedisProxyClient",
    "RedisProxyError",
    "SendRequestError",
    "ServerResponseError",
    "get_client",
    "normalize_ip_port",
    "wait_serve",
]
