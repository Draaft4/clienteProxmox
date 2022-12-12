from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse

class Visualizacion():

    @csrf_exempt
    @api_view(['GET','POST'])
    def index(request):
        return render(request,"components.html")
