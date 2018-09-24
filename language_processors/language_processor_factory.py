# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

from typing import Dict

from language_processors.base import LanguageProcessor, LanguageProcessorType
from language_processors.dialogflow_client import DialogFlowClient


class LanguageProcessorFactory:
    processors: Dict[LanguageProcessorType, LanguageProcessor] = {}

    @classmethod
    def get(
        cls,
        processor_type: LanguageProcessorType = LanguageProcessorType.DIALOGFLOW,
    ) -> LanguageProcessor:
        if processor_type not in cls.processors:
            if processor_type is LanguageProcessorType.DIALOGFLOW:
                cls.processors[processor_type] = DialogFlowClient()
            else:
                raise NotImplementedError()
        return cls.processors[processor_type]
