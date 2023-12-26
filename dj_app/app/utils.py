from django.core.serializers.json import DjangoJSONEncoder
from bson.objectid import ObjectId


class MongoObjectIdJSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)
