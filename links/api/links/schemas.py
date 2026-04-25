from pydantic import BaseModel, Field, AnyUrl

from links.db import Link
from links.lib import settings


class LinkCreateSchema(BaseModel):
    location: AnyUrl = Field(max_length=256)


class LinkReadSchema(BaseModel):
    shortened: str

    @classmethod
    def from_orm(cls, obj: Link) -> "LinkReadSchema":
        return cls(shortened=f"{settings.BASE_URL}/{obj.id:x}")
