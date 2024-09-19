from . import views
from django.urls import path


# namespace
app_name = 'enquetes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('<int:pergunta_id>/', views.DetalhesView.as_view(), name='detalhes'),

    path('<int:pergunta_id>/resultado/', views.ResultadoView.as_view(), name='resultado'),

]


