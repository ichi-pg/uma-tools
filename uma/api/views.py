from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from . import models

def combinations(req):
    # TODO 引数
    return HttpResponse(models.combinations())
