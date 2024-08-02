from enum import Enum


class OrganizationType(str, Enum):
    COM = "COM"
    ORG = "ORG"
    NET = "NET"
    EDU = "EDU"
    GOV = "GOV"
    MIL = "MIL"
    INT = "INT"
    Other = ""
