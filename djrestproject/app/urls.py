from django.urls import path,include
from . import views


urlpatterns = [
    path('userlist/',views.UserList),
    path('userlist/<int:id>',views.UserDetail),
]