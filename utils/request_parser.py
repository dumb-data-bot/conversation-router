# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0


def parse_backend_request(req):
    session = req['session']
    event = req['event']
    parameters = req['parameters']
    return session, event, parameters
