from django.contrib import admin
from django.urls import path, include
from fefu_lab import views

handler404 = views.custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fefu_lab.urls')),  # Включаем URLs приложения
]