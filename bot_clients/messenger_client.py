# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

import requests as r

from bot_clients.base import BotClient, BotClientType
from utils.config import Config


class MessengerClient(BotClient):

    def __init__(self):
        super().__init__(BotClientType.MESSENGER)

    def parse(self, req):
        assert req['object'] == 'page'

        session = req['entry'][0]['messaging'][0]['sender']['id']
        text = req['entry'][0]['messaging'][0]['message']['text']
        return session, text

    def post(self, receiver_id, replies):
        qs = 'access_token=' + Config.get('messenger/access_token')

        for reply in replies:
            data = {
                'recipient': {
                    'id': receiver_id,
                },
                'message': reply,
            }
            r.post('https://graph.facebook.com/me/messages?' + qs, json=data)
