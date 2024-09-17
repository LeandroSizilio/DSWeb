from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = "bazar"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('login/', views.LogarView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('evento/<int:id>/', views.ItensEventoView.as_view(), name='evento'),
    path('evento/', views.EventoView.as_view(), name='evento'),
    path('itens/', views.ItensView.as_view(), name='itens'),
    path('reservar/<int:id>/', views.ReservarView.as_view(), name='reservar'),
]