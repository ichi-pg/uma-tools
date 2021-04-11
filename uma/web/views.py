from django.shortcuts import render

# Create your views here.

from api import models

def combinations(req):
    girls = [int(i) for i in req.GET.getlist('girls')]
    size = min(max(int(req.GET.get('size', 4)), 4), 8)
    score = min(max(float(req.GET.get('score', 1)), 0), 1)
    return render(req, 'web/combinations.html', {
        'girls': [
            {'index': k, 'name': v, 'checked': 'checked' if k in girls else '' }
            for k,v in enumerate(models.g_girls)
        ],
        'size': size,
        'score': score,
        'combinations': [
            [{'value': k}]
            + [{'value': models.g_girls[i], 'primary': True if i in girls else False} for i in v]
            + [{'value': float(int(models.avg_score(v)*100)/100)}]
            for k,v in enumerate(models.combinations(girls, size, score))
        ],
    })
