import socket
from dataclasses import dataclass
from typing import List

from illumio.util import JsonObject, ModifiableObject


@dataclass
class BaseService(JsonObject):
    port: int = None
    proto: int = None

    def __post_init__(self):
        if type(self.proto) is str:
            self.proto = socket.getprotobyname(self.proto)
        super().__post_init__()


@dataclass
class ServicePort(BaseService):
    to_port: int = None
    icmp_type: int = None
    icmp_code: int = None
    service_name: str = None
    process_name: str = None
    windows_service_name: str = None
    user_name: str = None


@dataclass
class ServiceAddress(BaseService):
    ip: str = None
    fqdn: str = None
    description: str = None


@dataclass
class Service(ModifiableObject):
    service_ports: List[ServicePort] = None
