# -*- coding: utf-8 -*-
from subprocess import run
from src.services import restart_service
from src.db import run_query, run_update
from src.templates import db_query


def update_name(name):
    sql = db_query.UPDATE_CONFIG.value
    sql += f"name = '{name}'"
    run_update(sql)
    print(f"Update name with value: {name}")
    

def update_host(host):
    sql = db_query.UPDATE_CONFIG.value
    sql += f"host = '{host}'"
    run_update(sql)
    print(f"Update host with value: {host}")


def update_port(port):
    sql = db_query.UPDATE_CONFIG.value
    sql += f"port = '{port}'"
    run_update(sql)
    print(f"Update port with value: {port}")


def update_type(svr_type):
    sql = db_query.UPDATE_CONFIG.value
    sql += f"type = '{svr_type}'"
    run_update(sql)
    print(f"Update server type: {svr_type}")


def update_description(description):
    sql = db_query.UPDATE_CONFIG.value
    sql += f"des = '{description}'"
    run_update(sql)
    print(f"Update description: {description}")

