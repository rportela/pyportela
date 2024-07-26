from pyportela.models.Organization import Organization
from pyportela.services.SupabaseClient import SupabaseClient


class OrganizationService:

    supaClient: SupabaseClient

    def __init__(self) -> None:
        self.supaClient = SupabaseClient.get_instance()

    def register(self, org: Organization, overwrite: bool = False):
        pass
