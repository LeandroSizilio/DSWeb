from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = "bazar"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]