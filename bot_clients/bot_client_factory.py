# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

from bot_clients.base import BotClient
from bot_clients.messenger_client import MessengerClient


class BotClientFactory:

    @classmethod
    def get(cls) -> BotClient:
        return MessengerClient()
