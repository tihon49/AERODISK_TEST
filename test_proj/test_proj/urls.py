from django.contrib import admin
from django.urls import path, include

from main_app.views import BaseView, MountView, UnmountView, FormateDiskView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    
    path('', BaseView.as_view(), name='base'),
    path('mount/<str:disk_name>', MountView.as_view(), name='mount'),
    path('unmount/<str:disk_name>', UnmountView.as_view(), name='unmount'),
    path('formate/<str:disk_name>', FormateDiskView.as_view(), name='formate')
]
