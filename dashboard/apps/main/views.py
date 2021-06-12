from django.shortcuts import render, HttpResponse, redirect
from django.http import request, JsonResponse
from .models import iotDevice

def index(request):
  devices = iotDevice.objects.all()[:10]
  context = {
	"page": "index",
  "devices": devices,
	}
  return render( request, 'main/index.html', context)

def genData(request):
  return redirect('/')

from json import dumps
from django.http import JsonResponse, HttpResponse
  
def data(request):
  readings = iotDevice.objects.all()[:10]
  print(readings)
  time = []
  for i in readings:
    time.append(i.created_at)
  temperature = []
  for i in readings:
    temperature.append(round(i.deviceTemperature, 5))
  humidity = []
  for i in readings:
    humidity.append(round(i.deviceHumidity, 5))
  pressure = []
  for i in readings:
    pressure.append(round(i.devicePressure, 5))
  magx = []
  magy = []
  magz = []
  for i in readings:
    magx.append(round(i.deviceMagX, 5))
    magy.append(round(i.deviceMagY, 5))
    magz.append(round(i.deviceMagZ, 5))
  # create data dictionary
  dataDictionary = {
    "time": time,
    "temperature": temperature,
    "humidity": humidity,
    "pressure": pressure,
    "magx": magx,
    "magy": magy,
    "magz": magz,
  }
  return JsonResponse(dataDictionary)
