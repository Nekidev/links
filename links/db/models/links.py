from tortoise import fields
from tortoise.models import Model


class Link(Model):
    id = fields.BigIntField(primary_key=True)

    location = fields.CharField(max_length=256)

    ip = fields.CharField(max_length=46, db_index=True)
