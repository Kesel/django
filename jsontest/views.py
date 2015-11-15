import datetime

from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from jsontest.models import Way, DailySteps
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
        # mydict = {'date': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%LZ')}
        mydict = {'steps': 1, 'duration': 1}
        nowdatetime = json.dumps(mydict)
        return JsonResponse(mydict)


def timenow(request):
    mydict = {'date': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}
    return JsonResponse(mydict)


@csrf_exempt
def daily_steps(request):
    if request.method == 'GET':
        dailysteps = DailySteps.objects.all()
        data = []
        for day in dailysteps:
            data.append({'day': day.day, 'steps': day.steps})
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        daysteps = DailySteps(day=body['day'], steps=body['steps'])
        daysteps.save()
        return JsonResponse({'result': 'ok'})


@csrf_exempt
def day_steps(request, day_id):
    if request.method == 'GET':
        daysteps = DailySteps.objects.get(day=day_id)
        return JsonResponse({'day': daysteps.day, 'steps': daysteps.steps})
    elif request.method == 'PUT':
        daysteps = DailySteps.objects.get(day=day_id)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        daysteps.steps = body['steps']
        daysteps.save()
        return JsonResponse({'result': 'ok'})
    elif request.method == 'DELETE':
        daysteps = DailySteps.objects.get(day=day_id)
        daysteps.delete()
        return JsonResponse({'result': 'ok'})
