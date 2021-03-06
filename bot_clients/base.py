# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

from abc import ABC, abstractmethod
from contextlib import contextmanager
from enum import Enum


class BotClientType(Enum):
    MESSENGER = 'messenger'


class BotClient(ABC):

    def __init__(self, client_type: BotClientType):
        self.client_type = client_type

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    @abstractmethod
    def post(self, session, payload):
        pass

    @abstractmethod
    def parse(self, req):
        pass
