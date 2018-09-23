# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

from abc import ABC, abstractmethod
from enum import Enum


class BotClientPlatform(Enum):
    MESSENGER = 'messenger'


class BotClient(ABC):

    def __init__(self, platform: BotClientPlatform):
        self.platform = platform

    @abstractmethod
    def post(self, session, payload):
        pass
