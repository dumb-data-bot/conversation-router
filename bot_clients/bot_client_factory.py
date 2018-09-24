# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

from typing import Dict

from bot_clients.base import BotClient, BotClientType
from bot_clients.messenger_client import MessengerClient


class BotClientFactory:
    clients: Dict[BotClientType, BotClient] = {}

    @classmethod
    def get(
        cls,
        client_type: BotClientType = BotClientType.MESSENGER,
    ) -> BotClient:
        if client_type not in cls.clients:
            if client_type is BotClientType.MESSENGER:
                cls.clients[client_type] = MessengerClient()
            else:
                raise NotImplementedError()
        return cls.clients[client_type]
