from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('logout/', views.User_logout, name='logout')
]