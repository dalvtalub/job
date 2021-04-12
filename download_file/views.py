from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
#
#
# @login_required
def download_file(request):
    return render(request, 'download_file.html')
