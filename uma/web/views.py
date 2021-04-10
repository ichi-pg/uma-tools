from django.shortcuts import render

# Create your views here.

from api import models

def index(req):
    return render(req, 'web/index.html', {
        'girls': models.g_girls,
        'combinations': models.to_girl_names(models.combinations(size=4)),
    })
