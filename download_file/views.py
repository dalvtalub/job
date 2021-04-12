from django.http import HttpResponse
from django.shortcuts import render


def download_file(request):
    return render(request, 'download_file.html')
