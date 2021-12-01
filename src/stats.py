# -*- coding: utf-8 -*-

from src.templates import StatusCode, services
from src.services import status_service


def get_service_status():
    service_status = []
    services_list = services.services_list(services)

    for serv in services_list:
        status = status_service(serv)

        if status == StatusCode.ACTIVE.value:
            s = [serv, "active"]
            service_status.append(s)

        elif status == StatusCode.ERROR.value:
            s = [serv, "error"]
            service_status.append(s)

        elif status == StatusCode.INACTIVE.value:
            s = [serv, "inactive (dead)"]
            service_status.append(s)
        else:
            s = [serv, "unknown"]
            service_status.append(s)

    return service_status
