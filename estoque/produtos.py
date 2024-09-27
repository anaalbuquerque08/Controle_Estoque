# 1 -----Cadastro de produtos ||
def adicionar_produto(lista_produtos):
    nome_produto = input("Digite o nome do produto que deseja cadastrar: ")
    id_produto = input("Informe o código (ID) do produto: ")
    
    for produto in lista_produtos:
        if produto['id'] == id_produto:
            print("Já existe produto com esse código cadastrado!")
            return

    while True:
        quantidade_estoque = input("Informe a quantidade de produto disponível: ")
        if quantidade_estoque.isdigit():
            quantidade_estoque = int(quantidade_estoque)
            break
        else:
            print("Quantidade precisa ser um número inteiro!")

    while True:
        try:
            valor_custo = float(input("Informe o valor do custo (por unidade): "))
            break
        except ValueError:
            print("Valor de custo precisa ser um número válido (ex: 10.50).")

    while True:
        try:
            valor_venda = float(input("Informe o preço de venda: "))
            if valor_venda <= valor_custo:
                print("Preço de venda precisa ser maior que o valor de custo para garantir lucro!")
            else:
                break
        except ValueError:
            print("Preço precisa ser um número válido (ex: 100.00).")
  
    novo_produto = {
        'nome': nome_produto,
        'id': id_produto,
        'quantidade': quantidade_estoque,
        'custo': valor_custo,
        'preco': valor_venda
    }
      
    lista_produtos.append(novo_produto)
    print(f"Produto '{nome_produto}' adicionado com sucesso!")


# 3 ------ Função para exibir produtos cadastrados ||
def exibir_produtos(lista_produtos):
    for num, produto in enumerate(lista_produtos, start=1):
        print(f"\nProduto {num} »")
        print(f"  ° Nome: {produto['nome']}")
        print(f"  ° ID: {produto['id']}")
        print(f"  ° Quantidade: {produto['quantidade']}")
        print(f"  ° Custo: {produto['custo']:.2f}")
        print(f"  ° Preço: {produto['preco']:.2f}")
        print()


# 4---- Função para ordenar produtos por quantidade ||
def ordenar_quantidade(lista_produtos):
    print("Como deseja ordenar o estoque de produtos?")
    opcao = int(input("1 - Ordem crescente; \n2 - Ordem decrescente;\n "))

    if opcao == 1: 
        lista_ordenada = sorted(lista_produtos, key=lambda produto: produto['quantidade'])
        print("\nProdutos ordenados em ordem crescente:")
    elif opcao == 2: 
        lista_ordenada = sorted(lista_produtos, key=lambda produto: produto['quantidade'], reverse=True)
        print("\nProdutos ordenados em ordem decrescente:")
    else:
        print("Opção inválida!")
        return exibir_produtos(lista_produtos)

    exibir_produtos(lista_ordenada)

# 6 ------ Função para procurar produtos ||
def procurar_produtos(lista_produtos):
    busca_produto = input("Deseja buscar o produto por 'descricao' ou 'codigo'? ").lower()
    resultados = []

    if busca_produto == 'descricao':
        desc = input("Digite a descrição do produto: ")
        resultados = [produto for produto in lista_produtos if desc.lower() in produto['nome'].lower()]
    
    elif busca_produto == 'codigo':
        cod = input("Digite o código do produto: ")
        resultados = [produto for produto in lista_produtos if produto['id'] == cod]
    
    else:
        print("\nFunção não disponível, a busca precisa ser por 'codigo' ou 'descricao'.")
        return

    if resultados:
        print("\nProdutos encontrados:")
        exibir_produtos(resultados)
    else:
        print("\nNenhum produto encontrado com esse id")


# 7------ Função para excluir um produto ||
def excluir_produto(lista_produtos, ): 
    cod = input("Digite o código do produto que deseja remover: ")
    produto_encontrado = False
     
    for produto in lista_produtos:
        if produto['id'] == cod:
            lista_produtos.remove(produto)
            print(f"\nProduto com ID {cod} removido com sucesso.")
            produto_encontrado = True
            break 
    
    if not produto_encontrado:
        print(f"\n Nenhum produto encontrado com o código {cod}.")

# 8 ------- Função para listar produtos esgotados ||
def listar_produtos_esgotados(lista_produtos):
    esgotados = [produto for produto in lista_produtos if produto['quantidade'] == 0]

    if esgotados:
        print("\nProdutos esgotados:")
        exibir_produtos(esgotados)
    else:
        print("\nNenhum produto esgotado no estoque.")

# 9 ------ Função para identificar produtos com estoque baixo ||
def listar_produtos_baixo_estoque(lista_produtos):
    limite_input = input("Informe o limite de quantidade (padrão é 10): ")
     
    if limite_input.isdigit():
        limite = int(limite_input)
    else:
        print("Entrada inválida. Usando o valor padrão de limite (10).")
        limite = 10

    produtos_baixa_quantidade = [produto for produto in lista_produtos if produto['quantidade'] < limite]

    if produtos_baixa_quantidade:
        print("\nProdutos com quantidade abaixo do limite:")
        exibir_produtos(produtos_baixa_quantidade)
    else:
        print("\nNenhum produto com quantidade abaixo do limite no estoque.")

# 10 ----- Função para modificar a quantidade de um produto
def modificar_estoque(lista_produtos):
    cod = input("Digite o código do produto que deseja atualizar: ")

    for produto in lista_produtos:
        if produto['id'] == cod:
            tipo_modificacao = input("Escolha o tipo de modificação:\n1 - Entrada\n2 - Saída\nDigite a opção: ")
            
            if tipo_modificacao not in ['1', '2']:
                print("Opção inválida! Por favor, escolha 1 ou 2.")
                return

            try:
                quantidade_modificada = int(input("Digite a quantidade: "))
            except ValueError:
                print("Erro: Insira um número válido para a quantidade.")
                return
            
            if tipo_modificacao == '1':  
                nova_quantidade = produto['quantidade'] + quantidade_modificada
            elif tipo_modificacao == '2':  
                nova_quantidade = produto['quantidade'] - quantidade_modificada
                if nova_quantidade < 0:
                    print("Erro: Não há essa quantidade no estoque para ser removida.")
                    return

            produto['quantidade'] = nova_quantidade
            acao = "entrada" if tipo_modificacao == '1' else "saída"
            print(f"\nQuantidade do produto '{produto['nome']}' atualizada. Ação: {acao}. Novo estoque: {produto['quantidade']}.")
            return
    
    print("Produto não encontrado.")

            

# 11 ----- Função para alterar o preço de venda de um produto
def alterar_preco_venda(lista_produtos):
    cod = input("Digite o código do produto que deseja atualizar o preço: ")
    for produto in lista_produtos:
        if produto['id'] == cod:
            try:
                novo_preco = float(input("Digite o novo preço de venda: "))
                
                if novo_preco <= produto['custo']:
                    print("Erro: O novo preço não pode ser menor ou igual ao custo do produto.")
                    return
                
                produto['preco'] = novo_preco
                print(f"\nPreço do produto '{produto['nome']}' atualizado para R${novo_preco:.2f}.")
                return
            
            except ValueError:
                print("Erro: Insira um número válido para o preço.")
                return

    print("Produto não encontrado.")



# 13 ----- Função para calcular o valor total do estoque ||
def calcular_valor_total_estoque(lista_produtos):
    valor_total = 0  
    for produto in lista_produtos:
        valor_total += produto['quantidade'] * produto['preco']
    print(f"\nValor total do estoque: R${valor_total:.2f}") 

# 14 ----- Função para calcular o lucro presumido dos produtos ||
def calcular_lucro(lista_produtos):
    valor_total = 0
    custo_total = 0

    for produto in lista_produtos:
        valor_total += produto['quantidade'] * produto['preco']
        custo_total += produto['quantidade'] * produto['custo']
    
    lucro_presumido = valor_total - custo_total
    print(f"\nLucro presumido total do estoque: R${lucro_presumido:.2f}") 
    return lucro_presumido

# 16 --- Relatório geral
def relatorio_geral(produtos):
    """
    Exibe um relatório geral do estoque, incluindo detalhes dos produtos.

    :param produtos: Lista de produtos no estoque.
    :return: None
    """
    print("{:<10} {:<30} {:<10} {:<10} {:<10} {:<10}".format("Código", "Descrição", "Quantidade", "Custo", "Preço", "Valor Total"))
    total_custo = 0
    total_faturamento = 0


# 16 --- Relatório geral
def relatorio_geral(lista_produtos):
    """
    Exibe um relatório geral do estoque, incluindo detalhes dos produtos.

    :param lista_produtos: Lista de produtos no estoque.
    :return: None
    """ 
    print("\n{:<10} {:<30} {:<10} {:<10} {:<10} {:<10}".format("Código", "Descrição", "Quantidade", "Custo", "Preço", "Valor Total"))
    
    total_custo = 0
    total_faturamento = 0
 
    for produto in lista_produtos:
        codigo = produto['id']   
        nome = produto['nome']
        quantidade = produto['quantidade']
        custo = produto['custo']
        preco_venda = produto['preco']
        valor_total = quantidade * preco_venda
         
        print("{:<10} {:<30} {:<10} {:<10.2f} {:<10.2f} {:<10.2f}".format(codigo, nome, quantidade, custo, preco_venda, valor_total))
         
        total_custo += (quantidade * custo)
        total_faturamento += valor_total
        lucro = total_faturamento - total_custo
 
    print("\nCusto Total do Estoque: R${:.2f}".format(total_custo))
    print("Faturamento Total: R${:.2f}".format(total_faturamento))
    print("Lucro Total: R${:.2f}".format(lucro))
