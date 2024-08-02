from typing import Optional
from pydantic import BaseModel

from pyportela.models.CountryCode import CountryCode
from pyportela.models.OrganizationType import OrganizationType
from pyportela.utils import validate_name


class Organization(BaseModel):
    country: CountryCode
    org_type: OrganizationType
    name: str
    title: str
    description: Optional[str] = None

    def __init__(
        self,
        country: CountryCode,
        org_type: OrganizationType,
        name: str,
        title: str,
        description: Optional[str] = None,
    ) -> None:
        super().__init__(
            **{
                "country": country,
                "org_type": org_type,
                "name": name,
                "title": title,
                "description": description,
            }
        )
        validate_name(self.name)

    def get_id(self) -> str:
        s = f"{self.country.value}_{self.org_type.value}_{self.name}"
        return s.lower()
