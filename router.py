# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

from flask import Flask, request, make_response, jsonify

from bot_client_factory import BotClientFactory
from npl_platform_factory import NlpPlatformFactory
from utils.request_parser import parse_messenger_request, parse_backend_request

app = Flask(__name__)
logger = app.logger


@app.route('/messenger', methods=['POST'])
def messenger():
    req = request.get_json(silent=True, force=True)
    session, payload = parse_messenger_request(req)
    logger.debug(f'Request: {payload}')

    nlp = NlpPlatformFactory.get()
    res = nlp.post(session, payload)

    logger.debug(f'Response: {res}')
    return make_response(jsonify(res))


@app.route('/backend', methods=['POST'])
def backend():
    req = request.get_json(silent=True, force=True)
    session, payload = parse_backend_request(req)
    logger.debug(f'Request: {payload}')

    nlp = NlpPlatformFactory.get()
    res = nlp.post(session, payload)

    client = BotClientFactory.get()
    res = client.post(req, res)

    logger.debug(f'Response: {res}')
    return make_response(jsonify(res))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6677)
