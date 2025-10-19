from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fefu_lab.urls')),  # Включаем URLs приложения
]