# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

from bot_clients.base import BotClient, BotClientPlatform


class MessengerClient(BotClient):

    def __init__(self):
        super().__init__(BotClientPlatform.MESSENGER)

    def post(self, session, payload):
        pass
