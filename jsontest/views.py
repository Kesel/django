import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from jsontest.models import Way
from django.core.serializers.json import json, DjangoJSONEncoder


def home(request):
    if request.method == 'POST':
        # POST goes here . is_ajax is must to capture ajax requests. Beginners pit.
        if request.is_ajax():
            email = request.POST.get('email')
            password = request.POST.get('password')
            data = {"email": email, "password": password}
            return JsonResponse(data)
    # Get goes here
    return render(request, 'base_json.html')


@csrf_exempt
def pedometer(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        way = Way.objects.get(id=1)
        way.duration = body['duration']
        way.steps = body['steps']
        way.save()
        nowdatetime = {"result": "ok"}
        return JsonResponse(nowdatetime)
