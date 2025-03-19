from django.urls import path
from . import views # . represents current directory

urlpatterns = [
    path('', views.post_list, name = 'post_list')
]
