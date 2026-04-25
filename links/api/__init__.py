from fastapi import FastAPI
from fastapi.responses import ORJSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from links.lib import settings
from links.api import docs
from links.api.errors import BaseError, NotFoundError
from links.api.lifespan import lifespan
from links.api.links.router import router as links_router


app = FastAPI(
    debug=settings.DEBUG,
    title="Project API",
    description=docs.OPENAPI_DESCRIPTION,
    version="1.0.0",
    docs_url=None,
    redoc_url="/docs",
    lifespan=lifespan,
    openapi_tags=docs.OPENAPI_TAGS,
    default_response_class=ORJSONResponse,
)


@app.get("/")
async def index() -> RedirectResponse:
    return RedirectResponse(settings.SITE_URL)


app.include_router(links_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.BASE_URL,
        settings.SITE_URL,
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_exception_handler(BaseError, BaseError.handler)
app.add_exception_handler(404, NotFoundError.handler)
