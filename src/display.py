# -*- coding: utf-8 -*-

from tabulate import tabulate
from src.stats import get_service_status
from src.db import run_query
from src.templates import db_query


def display_service():
    status = get_service_status()
    print("SERVICE STATUS")
    headers = ["service", "status"]
    print(tabulate(status, headers, tablefmt="fancy_grid"))


def display_config():
    print("SVR CONFIG")
    headers = ["id", "name", "host", "port", "status", "in use",  "type", "des"]
    print(tabulate(run_query(db_query.GET_CONFIG.value), headers, tablefmt="fancy_grid"))

