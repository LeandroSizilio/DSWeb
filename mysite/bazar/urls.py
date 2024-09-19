from . import views
from django.urls import path


# namespace
app_name = 'bazar'

urlpatterns = [
    path('', views.BazarIndex.as_view(), name='bazar_index'),

    path('login/', views.LogarView.as_view(), name='login'),

    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),

    path('editar/', views.EditarPerfilView.as_view(), name='editar'),

    path('item-evento/<int:id>/', views.ItensEventoView.as_view(), name='item-evento'),

    path('evento/', views.EventoView.as_view(), name='evento'),

    path('itens/', views.ItensView.as_view(), name='itens'),

    path('reservar/<int:id>/', views.ReservarView.as_view(), name='reservar'),


]



