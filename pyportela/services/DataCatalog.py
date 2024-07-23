from pyportela.services.OrganizationService import OrganizationService


class DataCatalog:

    organizations: OrganizationService

    def __init__(self) -> None:
        self.organizations = OrganizationService()
