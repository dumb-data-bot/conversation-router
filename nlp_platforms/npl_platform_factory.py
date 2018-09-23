# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

from dialogflow_client import DialogFlowClient


class NlpPlatformFactory:

    @classmethod
    def get(cls):
        return DialogFlowClient()
