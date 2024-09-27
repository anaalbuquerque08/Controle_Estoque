from estoque import produtos_iniciais, estoque_inicial
from menu import menu_interativo
 
if __name__ == "__main__":
    produtos = estoque_inicial(produtos_iniciais)
    menu_interativo(produtos)
