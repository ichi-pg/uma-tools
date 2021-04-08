from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from . import models
import json

def to_json_res(res):
    res = json.dumps(res, ensure_ascii=False)
    return HttpResponse(res, content_type='application/json; charset=UTF-8')

def combinations(req):
    idx = req.GET.getlist('idx')
    idx = [int(i) for i in idx]
    res = models.combinations(idx)
    return to_json_res(res)

def girls(req):
    res = models.g_girls
    return to_json_res(res)
