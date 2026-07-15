from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Produto, Categoria

def inicio(request):
    # Pega os 3 produtos mais recentes da categoria Destaques
    lista_produtos = Produto.objects.filter(categorias__nome='Destaques').order_by('-data')[:3]
    
    contexto = {
        'lista_produtos': lista_produtos
    }
    return render(request, 'minearts_app/inicio.html', contexto)

def sobre(request):
    # View simples que renderiza a página Sobre
    return render(request, 'minearts_app/sobre.html')

def produtos(request):
    # 1. Captura o que o usuário clicou (se não clicar em nada, o padrão é 'Todos' e 'recentes')
    categoria_selecionada = request.GET.get('categoria', 'Todos')
    ordem_selecionada = request.GET.get('ordem', 'recentes')
    query_busca = request.GET.get('q', '').strip()

    # 2. Nossa base de dados no SQLite
    if categoria_selecionada == 'Todos':
        produtos_filtrados = Produto.objects.all()
    else:
        produtos_filtrados = Produto.objects.filter(categorias__nome=categoria_selecionada)

    if query_busca:
        produtos_filtrados = produtos_filtrados.filter(nome__icontains=query_busca)

    # 4. Lógica da ORDENAÇÃO
    if ordem_selecionada == 'menor-preco':
        produtos_filtrados = produtos_filtrados.order_by('preco')
    elif ordem_selecionada == 'maior-preco':
        produtos_filtrados = produtos_filtrados.order_by('-preco')
    else:
        # Por padrão (recentes), ordena pela data do mais novo para o mais antigo
        produtos_filtrados = produtos_filtrados.order_by('-data')

    produtos_filtrados = produtos_filtrados.distinct()

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

def adicionar_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    produto_id_str = str(produto_id)
    
    quantidade = request.POST.get('quantidade', 1)
    
    if produto_id_str in carrinho:
        carrinho[produto_id_str] += int(quantidade)
    else:
        carrinho[produto_id_str] = int(quantidade)
        
    request.session['carrinho'] = carrinho
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        from django.http import JsonResponse
        total_itens = sum(carrinho.values())
        return JsonResponse({'total_itens': total_itens})
        
    return redirect('minearts_app:carrinho')

def remover_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    produto_id_str = str(produto_id)
    
    if produto_id_str in carrinho:
        del carrinho[produto_id_str]
        
    request.session['carrinho'] = carrinho
    return redirect('minearts_app:carrinho')

def atualizar_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    produto_id_str = str(produto_id)
    nova_qtd = request.POST.get('quantidade')
    
    if nova_qtd and produto_id_str in carrinho:
        nova_qtd = int(nova_qtd)
        if nova_qtd > 0:
            carrinho[produto_id_str] = nova_qtd
        else:
            del carrinho[produto_id_str]
            
    request.session['carrinho'] = carrinho
    return redirect('minearts_app:carrinho')

def aplicar_cupom(request):
    cupom = request.POST.get('cupom', '').strip().upper()
    
    if cupom == 'PRIMEIRACOMPRA':
        request.session['cupom_desconto'] = 10
        request.session['cupom_nome'] = cupom
    else:
        if 'cupom_desconto' in request.session:
            del request.session['cupom_desconto']
        if 'cupom_nome' in request.session:
            del request.session['cupom_nome']
            
    return redirect('minearts_app:carrinho')

def carrinho(request):
    carrinho_session = request.session.get('carrinho', {})
    itens_carrinho = []
    subtotal = 0
    total_itens = 0
    
    for produto_id_str, quantidade in carrinho_session.items():
        try:
            produto = Produto.objects.get(id=int(produto_id_str))
            total_item = produto.preco * quantidade
            subtotal += total_item
            total_itens += quantidade
            itens_carrinho.append({
                'produto': produto,
                'quantidade': quantidade,
                'total_item': total_item
            })
        except Produto.DoesNotExist:
            continue
            
    # Aplica o cupom de desconto
    percentual_desconto = request.session.get('cupom_desconto', 0)
    desconto_valor = 0
    if percentual_desconto > 0:
        desconto_valor = (subtotal * percentual_desconto) / 100
        
    total = subtotal - desconto_valor
    if total < 0:
        total = 0

    # Mensagem pro WhatsApp
    texto_whats = "Olá! Gostaria de finalizar meu pedido da Minearts:%0A"
    for item in itens_carrinho:
        texto_whats += f"- {item['quantidade']}x {item['produto'].nome} (R$ {item['total_item']:.2f})%0A"
    
    if desconto_valor > 0:
        texto_whats += f"%0ASubtotal: R$ {subtotal:.2f}%0A"
        texto_whats += f"Desconto ({request.session.get('cupom_nome')}): -R$ {desconto_valor:.2f}%0A"
        
    texto_whats += f"%0ATotal: R$ {total:.2f}"
    
    sugestoes = Produto.objects.filter(disponivel=True)[:3]
            
    contexto = {
        'itens_carrinho': itens_carrinho,
        'subtotal': subtotal,
        'desconto_valor': desconto_valor,
        'total': total,
        'total_itens': total_itens,
        'texto_whats': texto_whats,
        'sugestoes': sugestoes
    }
    return render(request, 'minearts_app/carrinho.html', contexto)

def cadastro(request):
    return render(request, 'minearts_app/cadastro.html')

def login(request):
    return render(request, 'minearts_app/login.html')