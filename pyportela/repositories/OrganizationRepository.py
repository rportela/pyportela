from pyportela.models.Organization import Organization
from pyportela.services.SupabaseClient import SupabaseClient


class OrganizationRepository:

    supabase: SupabaseClient

    def __init__(self) -> None:
        self.supabase = SupabaseClient.get_instance()

    def get_organization(self, organization_id: str) -> Organization | None:
        doc = (
            self.supabase.table("data_organization")
            .select("*")
            .eq("id", organization_id)
            .single()
            .execute()
        )
        print(doc)
        return Organization(**doc) if doc else None
