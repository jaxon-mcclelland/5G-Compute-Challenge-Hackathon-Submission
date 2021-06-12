from django.shortcuts import render, HttpResponse, redirect
from django.http import request, JsonResponse
from .models import iotDevice
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

@csrf_exempt
def index(request):
    if request.method == 'POST':
        deviceHostname = request.POST.get("deviceHostname", str)
        deviceHumidity = request.POST.get("humidity", float)
        devicePressure = request.POST.get("pressure", float)
        deviceTemperature = request.POST.get("temperature", float)
        deviceMagX = request.POST.get("magx", float)
        deviceMagY = request.POST.get("magy", float)
        deviceMagZ = request.POST.get("magz", float)

        iotDevice.objects.create(
            deviceHostname = deviceHostname,
            deviceHumidity = deviceHumidity,
            devicePressure = devicePressure,
            deviceTemperature = deviceTemperature,
            deviceMagX = deviceMagX,
            deviceMagY = deviceMagY,
            deviceMagZ = deviceMagZ,
        )
        test = iotDevice.objects.all()
        return HttpResponse(test)
    else:
        test = iotDevice.objects.all()
        return HttpResponse(test)
    
def csrf(request):
    return JsonResponse({'csrfmiddlewaretoken': get_token(request)})