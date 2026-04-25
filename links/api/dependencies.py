from redis.asyncio import Redis

from fastapi import Request

from links.lib import settings
from links.api.errors import TooManyRequestsError


client = Redis.from_url(settings.REDIS_URL)


async def ratelimit(request: Request):
    key = f"rl:{request.client.host}"

    if await client.exists(key):
        raise TooManyRequestsError()

    await client.set(key, "", 1)
