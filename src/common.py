# -*- coding: utf-8 -*-
import json
import os


def read_config_file(path):
    f = open(path, )
    data = json.load(f)
    print(f"data {data}")
    f.close()
    return data
