from django.urls import path,include
from . import views
from rest_framework import routers

urlpatterns = [
    path('userlist/',views.UserList),
    path('userlist/<int:id>',views.UserDetail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]