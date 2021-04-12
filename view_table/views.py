from django.shortcuts import render


def view_table(request):
    return render(request, 'view_table.html')
