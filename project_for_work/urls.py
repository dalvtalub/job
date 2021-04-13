from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('view_table.urls')),
    path('api/', include('authentication.urls', namespace='authentication')),
]
