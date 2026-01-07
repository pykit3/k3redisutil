# k3redisutil

[![Action-CI](https://github.com/pykit3/k3redisutil/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3redisutil/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3redisutil/badge/?version=stable)](https://k3redisutil.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3redisutil)](https://pypi.org/project/k3redisutil)

Redis utilities for easier client management and proxy support.

k3redisutil is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3redisutil
```

## Quick Start

```python
import k3redisutil

# Get a process-wise singleton redis client
client = k3redisutil.get_client(6379)
client.set('foo', 'bar')

# Using redis as a duplex cross-process channel
c = k3redisutil.RedisChannel(6379, '/foo', 'client')
s = k3redisutil.RedisChannel(6379, '/foo', 'server')

c.send_msg('hello from client')
print(s.recv_msg())  # 'hello from client'

# Using redis proxy client
cli = k3redisutil.RedisProxyClient([('127.0.0.1', 2222)])
cli.set('key', 'value', expire=1000)  # with TTL in msec
print(cli.get('key'))
```

## API Reference

::: k3redisutil

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
