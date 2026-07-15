from django.urls import path
from . import views

# OBRIGATÓRIO NO ROTEIRO: Define o escopo de rotas do app
app_name = 'minearts_app'

urlpatterns = [
    # Caminho, função da view correspondente, nome da rota
    path('', views.inicio, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('produtos/', views.produtos, name='produtos'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    
    # Rotas do Carrinho
    path('adicionar-carrinho/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover-carrinho/<int:produto_id>/', views.remover_carrinho, name='remover_carrinho'),
    path('atualizar-carrinho/<int:produto_id>/', views.atualizar_carrinho, name='atualizar_carrinho'),
    path('aplicar-cupom/', views.aplicar_cupom, name='aplicar_cupom'),
]