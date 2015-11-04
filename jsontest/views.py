from django.shortcuts import render
from django.http import JsonResponse
from jsontest.models import Way


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


def pedometer(request):
    if request.method == 'POST':
        way = Way.objects.get(id=1)
        way.duration = request.POST.get('duration')
        way.steps = request.POST.get('steps')
        way.save()
