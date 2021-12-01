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
    ADD_USER = "INSERT INTO users (name, password, email) VALUES "
    ADD_RECIPES = "INSERT INTO recipes(name, user_id, recipes_type, is_public) VALUES "
