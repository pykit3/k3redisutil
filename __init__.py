"""
For using redis more easily.
"""

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


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3redisutil")
