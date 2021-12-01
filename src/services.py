# -*- coding: utf-8 -*-
from subprocess import call, PIPE
from src.templates import services


def status_service(serv):
    service = "systemctl is-active %s" % serv
    status = call(service, shell=True, stdout=PIPE)
    return status


def start_service(serv):
    service = "systemctl start %s" % serv
    call(service, shell=True, stdout=PIPE)


def stop_service(serv):
    service = "systemctl stop %s" % serv
    call(service, shell=True, stdout=PIPE)


def restart_service(serv):
    service = "systemctl restart %s" % serv
    call(service, shell=True, stdout=PIPE)


def services_start():
    services_list = services.services_list(services)
    for s in services_list:
        print("stat service: ", s)
        start_service(s)


def services_stop():
    services_list = services.services_list(services)
    for s in services_list:
        print("stop service: ", s)
        stop_service(s)


def services_restart():
    services_list = services.services_list(services)
    for s in services_list:
        print("restart service: ", s)
        restart_service(s)
