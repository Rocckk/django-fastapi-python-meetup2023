from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi import Depends
from utils import query_parameters
from typing import Annotated
from models import LossItemModel
# from threading import current_thread
# from time import time


app = FastAPI()
mg_client = MongoClient(
    'mongodb+srv://igorrrockit:l1ZNpEnUtZzHaYuR@cluster0.g81yooe.mongodb.net/?retryWrites=true&w=majority'
)
mydb = mg_client["my_db"]
my_col = mydb["rus_losses"]


@app.get("/losses")
async def get_losses(query_parameters: Annotated[dict, Depends(query_parameters)]):
    # thread = current_thread()
    # print(thread.native_id, time(), 'aaaaa')
    filters = {k: {"$gt": v} for k, v in query_parameters.items() if v}
    if not filters:
        result = my_col.find(limit=500)
    else:
        result = my_col.find(filters)
    return jsonable_encoder([i for i in result], custom_encoder={ObjectId: lambda x: str(x)})


@app.post("/losses")
async def insert_loss_item(items: LossItemModel | list[LossItemModel]):
    if isinstance(items, list):
        my_col.insert_many([item.model_dump() for item in items])
    elif isinstance(items, LossItemModel):
        my_col.insert_one(items.model_dump(by_alias=True))
    else:
        return Response(status_code=400)
