from django.urls import path
from .views import home_view, create_schedule_view, open_schedule_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create_schedule/', create_schedule_view, name='create_schedule'),
    path('open_schedule/', open_schedule_view, name='open_schedule'),
]
