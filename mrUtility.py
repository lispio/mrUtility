#!/opt/lispio/mrUtility/mrUtility_venv/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse
import textwrap

from src.services import *
from src.db import create_db, applay_migration, run_query
from src.display import display_service, display_config
from src.configSvr import update_name, update_host, update_port, update_type, update_description
from src.mock import mock


def parse_args():
    """parse command line arguments"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            "mrUtility config setup mr project"
        ),
        epilog=textwrap.dedent(
            "Application examples:\n'mrUtility.py "
        ),
    )

    parser.add_argument("-services_status", action="store_true", help="display services status")

    subparsers = parser.add_subparsers(dest="subcommand")

    db = subparsers.add_parser("db", help="data base management")
    db.add_argument('-cdb', type=str, help="Create empty data base")
    db.add_argument('-am', type=str,  help="run migration from path")
    db.add_argument('-db', type=str,  help="db name")
    
    services = subparsers.add_parser("services", help="services management")
    services.add_argument(
        "-status", action="store_true", help="display services status"
    )
    services.add_argument("-start", action="store_true", help="start all services")
    services.add_argument("-stop", action="store_true", help="stop all services")
    services.add_argument("-restart", action="store_true", help="restart all services")

    mock = subparsers.add_parser("mock", help="mock data")
    mock.add_argument("-uc", type=str, help="user count ")
    mock.add_argument("-rc", type=str, help="recipes count ")

    return parser.parse_args()


def main():
    a = parse_args()

    if a.services_status:
        display_service()
    
    if a.subcommand == "db":
        if a.cdb:
            print(f"Create DB  with name {a.cdb}")
            create_db(a.cdb)

        if a.am and a.db:
            print(f"aplay migration to data base {a.db}  from path {a.am} ")
            applay_migration(a.am, a.db)

    if a.subcommand == "services":
        if a.status:
            display_service()

        if a.start:
            services_start()

        if a.stop:
            services_stop()

        if a.restart:
            services_restart()

    if a.subcommand == 'config':
        if a.view:
            display_config() 
            
        if a.name:
            update_name(a.name)
        if a.host:
            update_host(a.host)
        if a.port:
            update_port(a.port)
        if a.type:
            update_type(a.type)
        if a.des:
            update_description(a.des)

    if a.subcommand == 'mock':
        m = mock()
        if a.uc:
            print("mock users ")
            m.mock_users(a.uc)
            print("done")

        if a.rc:
            print("mock recipes ")
            m.mock_recipes(a.rc)
            print("done")
            

if __name__ == "__main__":
    sys.exit(main())
