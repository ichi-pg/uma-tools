from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from . import models

def combinations(req):
    idx = req.GET.getlist('idx')
    idx = [int(i) for i in idx]
    res = models.combinations(idx)
    return HttpResponse(res)
