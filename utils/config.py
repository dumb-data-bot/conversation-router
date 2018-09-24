# !/usr/bin/env python3
# Copyright: Jun Zhang (jzhang@comp.nus.edu.sg)
# Licence: Apache Licence 2.0

import yaml


class Config:
    config = {}

    @classmethod
    def get(cls, key, default=None):
        if not cls.config:
            with open('config.yaml') as file:
                cls.config = yaml.load(file)

        cur = cls.config
        for token in key.split('/'):
            if token not in cur:
                return default
            cur = cur[token]
        return cur
