from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from . import models
import json

def to_json_res(res):
    res = json.dumps(res, ensure_ascii=False)
    return HttpResponse(res, content_type='application/json; charset=UTF-8')

def combinations(req):
    girls = [int(i) for i in req.GET.getlist('girls')]
    size = int(req.GET.get('size', 4))
    score = float(req.GET.get('score', 1.0))
    com = models.combinations(girls, size, score)
    return to_json_res({
        'combinations':com,
        'count':len(com),
    })

def girls(req):
    return to_json_res({
        'girls':models.g_girls,
        'count':len(models.g_girls),
    })
