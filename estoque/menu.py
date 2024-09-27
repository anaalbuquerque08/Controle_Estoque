from produtos import exibir_produtos, relatorio_geral, adicionar_produto, ordenar_quantidade, procurar_produtos, excluir_produto, listar_produtos_esgotados, listar_produtos_baixo_estoque, modificar_estoque, alterar_preco_venda, calcular_valor_total_estoque, calcular_lucro

def menu_interativo(lista_produtos):
    while True:
        print("\n ☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲  MENU ☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
        print("\nEscolha uma opção:\n")
        print("1 - Listar produtos")
        print("2 - Adicionar novo produto")
        print("3 - Ordenar produtos por quantidade")
        print("4 - Buscar produto")
        print("5 - Remover produto")
        print("6 - Consultar produtos esgotados")
        print("7 - Filtrar produtos com baixa quantidade")
        print("8 - Atualizar estoque")
        print("9 - Atualizar preço")
        print("10 - Calcular valor total do estoque")
        print("11 - Calcular lucro presumido")
        print("12 - Relatório")
        print("13 - Sair")
        
        opcao = input("\n  ✎  Digite a opção desejada: ")

        if opcao == '1':
            print("\n〖 Produtos cadastrados 〗\n")
            exibir_produtos(lista_produtos)
        elif opcao == '2':
            adicionar_produto(lista_produtos)
        elif opcao == '3':
            ordenar_quantidade(lista_produtos)
        elif opcao == '4':
            procurar_produtos(lista_produtos)
        elif opcao == '5':
            excluir_produto(lista_produtos)
        elif opcao == '6':
            listar_produtos_esgotados(lista_produtos)
        elif opcao == '7':
            listar_produtos_baixo_estoque(lista_produtos)
        elif opcao == '8':
            modificar_estoque(lista_produtos)
        elif opcao == '9':
            alterar_preco_venda(lista_produtos)
        elif opcao == '10':
            calcular_valor_total_estoque(lista_produtos)
        elif opcao == '11':
            calcular_lucro(lista_produtos)
        elif opcao == '12':
            relatorio_geral(lista_produtos)
        elif opcao == '13':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
