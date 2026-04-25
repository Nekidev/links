from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "link" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "location" VARCHAR(256) NOT NULL,
    "ip" VARCHAR(46) NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_link_ip_fab721" ON "link" ("ip");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJzdlV9v2jAUxb8K4qmTuomGhLC9AdI2po5K3R9NqqrIJCaxcOzUdrZWFd99vk6CkwAZSJ"
    "3W7o2cexzf+4t9eOynPMJUvrkkbN1/13vsM5Ri/aOhn/f6KMusCoJCS2qMtHIspRIoVFpb"
    "ISqxliIsQ0EyRTjTKsspBZGH2khYbKWckbscB4rHWCVY6MLNrZYJi/A9ltVjtg5WBNOo0S"
    "aJYG+jB+ohM9qUxHOm3hsvbLgMQk7zlFl/9qASzrYLCFOgxphhgRSGHZTIYQJosBy0Gqpo"
    "1lqKLmtrIrxCOVW1iY/EEHIGCHU30swYwy6v3zrOcOg7g+Fo7Lm+740HY+01Le2W/E0xsA"
    "VSvMpgmX+YL77CoFx/p+LjgbAxa5BCxSrD2wKmPESm8x3MswSJ/ZDra1qo9YBt1BXYLtaV"
    "YGHbM/ZEtFN0H1DMYpXoR8cbdZD8PrmefZxcn2nXqybPRVlyihqgrZ3V7BSIhftv4Xvqs9"
    "qg5x4Dzz3MzjXo4M6v1rVDCcIShetfSETBToU7/JB3t5Q6aVtBDMUGDUwI/ZcJOMGChMm+"
    "bCwrnemIrOfZ5ON/FI7Oheu74+HI3WbiVumKwj/H3k8s5ImpV1vyUkPPOyr0vI7Q89qhB1"
    "fjBIil/WUCvBgMjgCoXQcBmloToN5R4eIONiF++nK12A+xtqQF8hvTA95EJFTnPUqkun2e"
    "WDsowtTQdCrlHa3DO/s8+dHmOru8mhoKXKpYmLeYF0z/9d/L5jd/IKMe"
)
