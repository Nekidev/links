import os

from dotenv import load_dotenv


load_dotenv()


DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")


DATABASE = {
    "connections": {"default": os.getenv("LINKS_DATABASE_URL", "sqlite://db.sqlite3")},
    "apps": {
        "models": {
            "models": [
                "links.db.models.links",
                "aerich.models",  # Keep this one for migrations.
            ],
            "default_connection": "default",
        }
    },
    "use_tz": True,
    "timezone": "UTC",
}


BASE_URL = os.environ["LINKS_BASE_URL"]
SITE_URL = os.environ["LINKS_SITE_URL"]

REDIS_URL = os.environ["LINKS_REDIS_URL"]
