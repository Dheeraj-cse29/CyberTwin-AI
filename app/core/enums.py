from enum import Enum


class AssetType(str, Enum):
    SERVER = "Server"
    WORKSTATION = "Workstation"
    ROUTER = "Router"
    SWITCH = "Switch"
    FIREWALL = "Firewall"
    DATABASE = "Database"
    CLOUD = "Cloud"


class AssetStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    MAINTENANCE = "Maintenance"
    COMPROMISED = "Compromised"