# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

from abc import ABC, abstractmethod


class NlpPlatform(ABC):

    @abstractmethod
    def post(self, session, payload):
        pass
