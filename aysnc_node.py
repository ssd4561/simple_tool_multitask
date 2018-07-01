import asyncio
from enum import Enum


class node_statue(Enum):
    node_idle=1
    node_error=2
    node_process=3  #use this param for multithreading
    node_stoping=4


class async_node():
    def __init__(self):
        self.status=node_statue.node_idle
