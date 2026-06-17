// O Django já renderizou os cards usando {% for %} no produtos.html.
// Este script agora cuida da interatividade e de enviar as requisições de filtro para o Django.

document.addEventListener("DOMContentLoaded", function() {
    
    // === LÓGICA DE INTERATIVIDADE DOS CARDS (Quantidade e Carrinho) ===
    const cards = document.querySelectorAll(".card-produto");

    cards.forEach(card => {
        // Encontra os elementos dentro do card atual
        const btnMenos = card.querySelector(".btn-menos");
        const btnMais = card.querySelector(".btn-mais");
        const spanQtd = card.querySelector(".qtd-numero");
        const btnAdicionar = card.querySelector(".btn-adicionar-grid");
        
        // Pega o nome do produto que o Django colocou no h3 para usar no alerta
        const tituloProdutoElement = card.querySelector(".titulo-produto");
        
        // Segurança extra: só continua se o card tiver um título
        if (!tituloProdutoElement) return; 
        const tituloProduto = tituloProdutoElement.textContent;

        // Se a estrutura de quantidade existir no card, ativa os botões
        if (spanQtd && btnMenos && btnMais) {
            let quantidade = 1;

            btnMais.addEventListener("click", () => {
                quantidade++;
                spanQtd.textContent = quantidade;
            });

            btnMenos.addEventListener("click", () => {
                if (quantidade > 1) {
                    quantidade--;
                    spanQtd.textContent = quantidade;
                }
            });

            // Lógica do botão de adicionar
            if (btnAdicionar) {
                btnAdicionar.addEventListener("click", () => {
                    alert(`Você adicionou ${quantidade}x ${tituloProduto} ao carrinho!`);
                });
            }
        }
    });

    // === LÓGICA DE FILTRO E ORDENAÇÃO COM DJANGO ===

    // 1. Filtro por Categoria
    const botoesFiltro = document.querySelectorAll(".btn-filtro");
    
    botoesFiltro.forEach(botao => {
        botao.addEventListener("click", () => {
            const categoria = botao.textContent.trim();
            // Pega a URL atual para não perder a ordenação que já está aplicada
            const urlParams = new URLSearchParams(window.location.search);
            urlParams.set('categoria', categoria); // Altera a categoria na URL
            
            // Recarrega a página pedindo ao Django os dados novos
            window.location.search = urlParams.toString(); 
        });
    });

    // 2. Ordenação por Select
    const selectOrdenar = document.getElementById("ordenar");
    
    if (selectOrdenar) {
        selectOrdenar.addEventListener("change", (e) => {
            const ordem = e.target.value;
            // Pega a URL atual para não perder o filtro que já está aplicado
            const urlParams = new URLSearchParams(window.location.search);
            urlParams.set('ordem', ordem); // Altera a ordem na URL
            
            // Recarrega a página passando a nova ordem para o Django
            window.location.search = urlParams.toString(); 
        });
    }
});