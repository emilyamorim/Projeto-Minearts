from django.urls import path
from . import views

# OBRIGATÓRIO NO ROTEIRO: Define o escopo de rotas do app
app_name = 'minearts_app'

urlpatterns = [
    # Caminho, função da view correspondente, nome da rota
    path('', views.inicio, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('produtos/', views.produtos, name='produtos'),
]