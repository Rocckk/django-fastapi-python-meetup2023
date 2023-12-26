from django.http import JsonResponse
from pymongo import MongoClient
from .utils import MongoObjectIdJSONEncoder
from django.views.decorators.csrf import csrf_exempt
import json
# from threading import current_thread
# from time import time

mg_client = MongoClient(
    'mongodb+srv://igorrrockit:l1ZNpEnUtZzHaYuR@cluster0.g81yooe.mongodb.net/?retryWrites=true&w=majority'
)
mydb = mg_client["my_db"]
my_col = mydb["rus_losses"]


@csrf_exempt
def get_losses(request):
    # thread = current_thread()
    # print(thread.native_id, time(), 'aaaaa')
    if request.method == 'GET':
        if not request.GET:
            result  = my_col.find(limit=500)
            return JsonResponse(
                [i for i in result],
                safe=False,
                encoder=MongoObjectIdJSONEncoder
            )
        else:
            filters = {k: {"$gt": int(v)} for k, v in request.GET.items()}
            result = my_col.find(filters)
            return JsonResponse(
                [i for i in result],
                safe=False,
                encoder=MongoObjectIdJSONEncoder
            )
    elif request.method == 'POST':
        request_json = json.loads(request.body)
        if isinstance(request_json, list):
            my_col.insert_many(request_json)
        elif isinstance(request_json, dict):
            my_col.insert_one(request_json)
        else:
            return JsonResponse({'error': 'wrong data sent'}, status=400)
        return JsonResponse({}, status=204)
    else:
        return JsonResponse({}, status=405)
