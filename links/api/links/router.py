from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse

from links.db import Link
from links.api.errors import NotFoundError
from links.api.schemas import Hex
from links.api.dependencies import ratelimit
from links.api.links.schemas import LinkCreateSchema, LinkReadSchema


router = APIRouter(tags=["Links"], dependencies=[Depends(ratelimit)])


@router.post("/links")
async def create_link(request: Request, payload: LinkCreateSchema) -> LinkReadSchema:
    link = await Link.create(location=str(payload.location), ip=request.client.host)

    return LinkReadSchema.from_orm(link)


@router.get("/{code}")
async def redirect(code: Hex):
    link = await Link.get_or_none(id=int(code, 16))

    if link is None:
        raise NotFoundError("link")

    return RedirectResponse(link.location, status_code=308)
