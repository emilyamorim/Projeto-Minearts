import os
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from minearts_app.models import Categoria, Produto

todos_produtos = [
    {'nome': 'Pulseira de miçangas', 'preco': 5.00, 'img': 'produtos/produto-1.png', 'disponivel': True, 'categorias': ['Pulseiras', 'Destaques'], 'data': '2026-05-24'},
    {'nome': 'Pulseira oceano', 'preco': 8.00, 'img': 'produtos/produto-2.png', 'disponivel': True, 'categorias': ['Pulseiras'], 'data': '2026-05-23'},
    {'nome': 'Colar de resina', 'preco': 20.00, 'img': 'produtos/produto-3.png', 'disponivel': True, 'categorias': ['Colares'], 'data': '2026-05-22'},
    {'nome': 'Colar de Turmalina Negra', 'preco': 25.00, 'img': 'produtos/produto-4.png', 'disponivel': True, 'categorias': ['Colares', 'Minerais'], 'data': '2026-05-21'},
    {'nome': 'Conjunto de pulseiras', 'preco': 25.00, 'img': 'produtos/produto-5.png', 'disponivel': True, 'categorias': ['Pulseiras', 'Destaques'], 'data': '2026-05-20'},
    {'nome': 'Colar em formato de coração em Jasper', 'preco': 12.00, 'img': 'produtos/produto-6.png', 'disponivel': True, 'categorias': ['Pulseiras', 'Minerais'], 'data': '2026-05-19'},
    {'nome': 'Colar em Quartzo Rosa', 'preco': 15.00, 'img': 'produtos/produto-7.png', 'disponivel': True, 'categorias': ['Colares', 'Minerais'], 'data': '2026-05-19'},
    {'nome': 'Chaveiro Chapéu do Luffy', 'preco': 8.00, 'img': 'produtos/produto-8.png', 'disponivel': True, 'categorias': ['Chaveiros'], 'data': '2026-05-19'},
    {'nome': 'Amigurumi Polvo', 'preco': 8.00, 'img': 'produtos/produto-9.png', 'disponivel': True, 'categorias': ['Chaveiros'], 'data': '2026-05-19'},
    {'nome': 'Brincos com pedra da lua e conchas', 'preco': 12.00, 'img': 'produtos/produto-10.png', 'disponivel': True, 'categorias': ['Brincos', 'Minerais'], 'data': '2026-05-19'},
    {'nome': 'Brincos com hamsá e pedra néon', 'preco': 12.00, 'img': 'produtos/produto-11.png', 'disponivel': True, 'categorias': ['Brincos', 'Minerais'], 'data': '2026-05-19'},
    {'nome': 'Colar onda do mar', 'preco': 15.00, 'img': 'produtos/produto-12.png', 'disponivel': True, 'categorias': ['Colares'], 'data': '2026-05-19'},
    {'nome': 'Pulseiras de miçangas', 'preco': 15.00, 'img': 'produtos/produto-13.png', 'disponivel': True, 'categorias': ['Pulseiras', 'Destaques'], 'data': '2026-05-19'},
    {'nome': 'Pulseiras com misangas azuis', 'preco': 15.00, 'img': 'produtos/produto-14.png', 'disponivel': True, 'categorias': ['Pulseiras', 'Destaques'], 'data': '2026-05-19'},
    {'nome': 'Pulseiras com misangas amarelas', 'preco': 15.00, 'img': 'produtos/produto-15.png', 'disponivel': True, 'categorias': ['Pulseiras', 'Destaques'], 'data': '2026-05-19'},
    {'nome': 'Pulseiras diversas', 'preco': 8.00, 'img': 'produtos/produto-16.png', 'disponivel': True, 'categorias': ['Pulseiras', 'Destaques'], 'data': '2026-05-19'},
]

inicio_produtos = [
    {'nome': 'Colar Quartzo Rosa', 'preco': 20.00, 'img': 'produtos_diversos/produto-1.png', 'disponivel': True, 'categorias': ['Destaques'], 'data': '2026-06-01'},
    {'nome': 'Chaveiro Chapéu do Luffy (Grande)', 'preco': 25.00, 'img': 'produtos_diversos/produto-2.png', 'disponivel': True, 'categorias': ['Destaques'], 'data': '2026-06-01'},
    {'nome': 'Amigurumi Polvo (Grande)', 'preco': 10.00, 'img': 'produtos_diversos/produto-3.png', 'disponivel': True, 'categorias': ['Destaques'], 'data': '2026-06-01'},
]

print("Apagando dados antigos...")
Produto.objects.all().delete()
Categoria.objects.all().delete()

print("Criando produtos...")
for p_data in todos_produtos + inicio_produtos:
    p = Produto.objects.create(
        nome=p_data['nome'],
        preco=p_data['preco'],
        img=p_data['img'],
        disponivel=p_data['disponivel'],
        data=datetime.strptime(p_data['data'], "%Y-%m-%d").date()
    )
    for cat_nome in p_data['categorias']:
        cat, created = Categoria.objects.get_or_create(nome=cat_nome)
        p.categorias.add(cat)

print("Dados populados com sucesso!")
