from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from view_table.forms import AuthForm


def view_table(request):
    return render(request, 'view_table.html')
