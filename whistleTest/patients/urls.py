from django.urls import path
from . import views

app_name = 'patients'
urlpatterns = [
    path('', views.PatientListView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]