# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

import logging
from flask import Flask, request, make_response, jsonify

from bot_clients.base import BotClientType
from bot_clients.bot_client_factory import BotClientFactory
from language_processors.language_processor_factory import LanguageProcessorFactory
from utils.request_parser import (
    parse_backend_request,
)

app = Flask(__name__)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
logger = app.logger


@app.route('/', methods=['GET'])
def welcome():
    return make_response(jsonify('Hello world!'))


@app.route('/messenger', methods=['GET'])
def verify():
    challenge = request.args.get('hub.challenge')
    return make_response(challenge)


@app.route('/messenger', methods=['POST'])
def messenger():
    req = request.get_json(silent=True, force=True)
    logger.debug(f'Request: {req}')

    with BotClientFactory.get(BotClientType.MESSENGER) as bot_client:
        session, text = bot_client.parse(req)

        with LanguageProcessorFactory.get() as nlp:
            replies = nlp.post(session, text)
            logger.debug(f'Replies: {session}:{replies}')

        bot_client.post(session, replies)

    return make_response()


@app.route('/backend', methods=['POST'])
def backend():
    req = request.get_json(silent=True, force=True)
    logger.info(f'Request: {req}')

    session, event, parameters = parse_backend_request(req)

    with LanguageProcessorFactory.get() as nlp:
        replies = nlp.post(session, (event, parameters))

    with BotClientFactory.get(BotClientType.MESSENGER) as bot_client:
        logger.debug(f'Replies: {session}:{replies}')
        bot_client.post(session, replies)

    return make_response()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6677)
