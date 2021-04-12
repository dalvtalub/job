from django.urls import path, include
from .views import view_table

urlpatterns = [
    path('', view_table),
    path('download_file', include('download_file.urls')),
]