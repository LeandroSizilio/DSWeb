from django.urls import path
from . import views

app_name = "bazar"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bazar/<int:pk>/', views.BazarView.as_view(), name='Bazar'),
]