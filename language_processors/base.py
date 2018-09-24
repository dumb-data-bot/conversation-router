# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

from abc import ABC, abstractmethod
from enum import Enum


class LanguageProcessorType(Enum):
    DIALOGFLOW = 'DialogFlow'


class LanguageProcessor(ABC):

    def __init__(self, processor_type: LanguageProcessorType):
        self.processor_type = processor_type

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    @abstractmethod
    def post(self, session, payload):
        pass
