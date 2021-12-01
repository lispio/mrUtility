# -*- coding: utf-8 -*-
from enum import Enum


class services(Enum):
    PSQL = "postgresql"
    MR = "mr"

    @staticmethod
    def services_list(self):
        return list(map(lambda s: s.value, services))


class StatusCode(Enum):
    ACTIVE = 0
    ERROR = 1
    INACTIVE = 3


class db(Enum):
    DATABASE = "mr"
    USER = 'it'
    HOST = '127.0.0.1'
    PORT = '5432'


class db_query(Enum):
    GET_CONFIG = "SELECT id, name, host, port, status, in_use, type, des FROM config_svr"
    UPDATE_CONFIG = "UPDATE config_svr SET "
