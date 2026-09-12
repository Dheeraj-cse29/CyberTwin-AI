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

from enum import Enum


class AttackType(str, Enum):
    PORT_SCAN = "PORT_SCAN"
    BRUTE_FORCE = "BRUTE_FORCE"
    DOS = "DOS"
    MALWARE = "MALWARE"
    PHISHING = "PHISHING"


class AttackStatus(str, Enum):
    SIMULATED = "SIMULATED"
    DETECTED = "DETECTED"
    BLOCKED = "BLOCKED"