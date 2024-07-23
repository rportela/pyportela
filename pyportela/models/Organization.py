from typing import Optional
from pydantic import BaseModel
from pyportela.models.OrganizationType import OrganizationType
from pyportela.models.CountryCode import CountryCode


class Organization(BaseModel):
    country: CountryCode
    org_type: OrganizationType
    name: str
    description: Optional[str] = None
    title: Optional[str] = None

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.validate_name(self.name)

    @staticmethod
    def validate_name(org_name: str):
        forbidden_chars = [".", ",", "__", " ", "-"]
        for char in forbidden_chars:
            if char in org_name:
                raise ValueError(f"Organization name cannot contain '{char}'")

    def get_id(self) -> str:
        s = f"{self.country.value}_{self.org_type.value}_{self.name}"
        return s.lower()
