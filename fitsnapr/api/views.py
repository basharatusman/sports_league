from django.shortcuts import render
from django.http import HttpResponse


def api(request):
    return render(request, 'api/api.html')
