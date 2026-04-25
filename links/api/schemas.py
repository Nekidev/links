from typing import Annotated

from pydantic import BaseModel, Field


Hex = Annotated[str, Field(max_length=8, pattern=r"^[0-9a-f]+$")]
"""A URL's hex."""


class ErrorSchema(BaseModel):
    """A standard error response schema."""

    title: str
    message: str
