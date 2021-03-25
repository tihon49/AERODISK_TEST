from django.contrib import admin
from django.urls import path

from main_app.views import BaseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='base'),
]
