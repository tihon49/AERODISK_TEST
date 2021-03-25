from django.urls import path
from .views import login_view, registration_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
]
