# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0
import os

from dialogflow_v2 import SessionsClient
from dialogflow_v2.proto.session_pb2 import QueryInput, TextInput, EventInput
from google.protobuf.struct_pb2 import Struct

from language_processors.base import LanguageProcessor, LanguageProcessorType


class DialogFlowClient(LanguageProcessor):

    def __init__(self):
        super().__init__(LanguageProcessorType.DIALOGFLOW)

        if os.path.exists('/Users/jzhang/.ssh/dumb.data.bot.api.json'):
            self.client = SessionsClient.from_service_account_json(
                '/Users/jzhang/.ssh/dumb.data.bot.api.json',
            )
        else:
            self.client = SessionsClient()

    def _gen_replies(self, payload):
        if any(entry.platform == entry.FACEBOOK for entry in payload):
            entries = [entry for entry in payload if entry.platform == entry.FACEBOOK]
        else:
            entries = payload
        replies = []
        for entry in entries:
            if hasattr(entry, 'quick_replies') and entry.quick_replies.quick_replies:
                replies.append({
                    'text': entry.quick_replies.title,
                    'quick_replies': [
                        {
                            'content_type': 'text',
                            'title': quick_reply,
                            'payload': quick_reply,
                        } for quick_reply in entry.quick_replies.quick_replies
                    ],
                })
            elif hasattr(entry, 'text') and entry.text.text:
                replies.append({
                    'text': entry.text.text[0],
                })
            else:
                raise NotImplementedError(entry)
        return replies

    def post(self, session_token, payload):
        session = self.client.session_path('dumbdatabot', session_token)
        if isinstance(payload, str):
            query_input = QueryInput(
                text=TextInput(text=payload, language_code='en_US'),
            )
        else:
            event, parameters = payload
            struct = Struct()
            for key, val in parameters.items():
                struct[key] = val
            query_input = QueryInput(
                event=EventInput(
                    name=event,
                    parameters=struct,
                    language_code='en_US',
                ),
            )
        response = self.client.detect_intent(session, query_input=query_input)
        return self._gen_replies(response.query_result.fulfillment_messages)
