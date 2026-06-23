from django.shortcuts import render
from django.core.paginator import Paginator

def inicio(request):
    # Criamos o contexto com a lista de produtos aqui também!
    contexto = {
        'lista_produtos': [
            {
                'nome': 'Colar Quartzo Rosa', 
                'preco': 20.00, 
                'img': 'produtos_diversos/produto-1.png', 
                'disponivel': True
            },
            {
                'nome': 'Chaveiro Chapéu do Luffy', 
                'preco': 25.00, 
                'img': 'produtos_diversos/produto-2.png', 
                'disponivel': True
            },
            {
                'nome': 'Amigurumi Polvo', 
                'preco': 10.00, 
                'img': 'produtos_diversos/produto-3.png', 
                'disponivel': True
            },
        ]
    }
    # Agora passamos o contexto para o inicio.html
    return render(request, 'minearts_app/inicio.html', contexto)

def sobre(request):
    # View simples que renderiza a página Sobre
    return render(request, 'minearts_app/sobre.html')

def produtos(request):
    # 1. Captura o que o usuário clicou (se não clicar em nada, o padrão é 'Todos' e 'recentes')
    categoria_selecionada = request.GET.get('categoria', 'Todos')
    ordem_selecionada = request.GET.get('ordem', 'recentes')

    # 2. Nossa base de dados com as categorias e datas adicionadas
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

    # 3. Lógica do FILTRO
    if categoria_selecionada == 'Todos':
        produtos_filtrados = todos_produtos.copy()
    else:
        produtos_filtrados = [p for p in todos_produtos if categoria_selecionada in p['categorias']]

    # 4. Lógica da ORDENAÇÃO
    if ordem_selecionada == 'menor-preco':
        produtos_filtrados.sort(key=lambda x: x['preco'])
    elif ordem_selecionada == 'maior-preco':
        produtos_filtrados.sort(key=lambda x: x['preco'], reverse=True)
    else:
        # Por padrão (recentes), ordena pela data do mais novo para o mais antigo
        produtos_filtrados.sort(key=lambda x: x['data'], reverse=True)

    # 5. Lógica da PAGINAÇÃO
    paginator = Paginator(produtos_filtrados, 6) 
    
    # Pega o número da página na URL (ex: ?page=2)
    numero_pagina = request.GET.get('page')
    
    # Gera o objeto da página atual com os 6 produtinhos
    page_obj = paginator.get_page(numero_pagina)

    # 6. Envia os dados para o HTML
    contexto = {
        'nome_categoria': categoria_selecionada,
        'page_obj': page_obj,
        'categoria_atual': categoria_selecionada,
        'ordem_atual': ordem_selecionada,
    }
    return render(request, 'minearts_app/produtos.html', contexto)

def carrinho(request):
    return render(request, 'minearts_app/carrinho.html')

def cadastro(request):
    return render(request, 'minearts_app/cadastro.html')

def login(request):
    return render(request, 'minearts_app/login.html')