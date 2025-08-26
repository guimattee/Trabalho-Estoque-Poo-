from Cliente import Cliente
from Produto import Produto
from Venda import Venda
from Fila import Fila
from Pilha import Pilha
from main import clientes, estoque, fila_vendas, pilha_operacoes

def cadastrar_cliente():
    id_cliente = len(clientes) + 1
    nome = input("Digite o nome do cliente: ")
    cliente = Cliente(id_cliente, nome)
    clientes.append(cliente)
    pilha_operacoes.empilhar(("cadastro_cliente", cliente))
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    for cliente in clientes:
        print(cliente)
    

def listar_clientes_valores():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    for cliente in clientes:
        print(f"{cliente.nome} gastou R${cliente.total_gasto}")


def cadastrar_produto():
    id_produto = len(estoque) + 1
    nome = input("Digite o nome do produto: ")
    try:
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço: "))
    except ValueError:
        print("Entrada inválida!")
        return
    produto = Produto(id_produto, nome, quantidade, preco)
    estoque.append(produto)
    pilha_operacoes.empilhar(("cadastro_produto", produto))
    print(f"Produto cadastrado com sucesso! (ID: {id_produto})")

def listar_produtos():
    if not estoque:
        print("Estoque vazio.")
    for produto in estoque:
        print(produto)

def valor_total_estoque():
    total = sum(p.quantidade * p.preco for p in estoque)
    print(f"Valor total do estoque: R${total}")


def realizar_venda():
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
        id_produto = int(input("Digite o ID do produto: "))
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Entrada inválida!")
        return

    cliente = next((cliente for cliente in clientes if cliente.id == id_cliente), None)
    produto = next((produto for produto in estoque if produto.id == id_produto), None)

    if not cliente:
        print("Cliente não encontrado!")
        return
    if not produto:
        print("Produto não encontrado!")
        return
    if produto.quantidade < quantidade:
        print("Estoque insuficiente!")
        return

    venda = Venda(cliente, produto, quantidade)
    produto.quantidade -= quantidade
    cliente.total_gasto += venda.valor_total
    fila_vendas.enfileirar(venda)
    pilha_operacoes.empilhar(("venda", venda))
    print("Venda realizada com sucesso!")
    print(venda)

def listar_vendas():
    if fila_vendas.vazia():
        print("Nenhuma venda realizada.")
    for venda in fila_vendas.listar():
        print(venda)

def valor_total_vendas():
    total = sum(venda.valor_total for venda in fila_vendas.listar())
    print(f"Valor total de vendas realizadas: R${total}")


def desfazer():
    if pilha_operacoes.vazia():
        print("Nenhuma operação para desfazer.")
        return

    operacao, objeto = pilha_operacoes.desempilhar()  # desempilha a tupla

    if operacao == "cadastro_produto":
        if objeto in estoque:
            estoque.remove(objeto)
        print(f"Desfeito cadastro do produto '{objeto.nome}'.")

    elif operacao == "cadastro_cliente":
        if objeto in clientes:
            clientes.remove(objeto)
        print(f"Desfeito cadastro do cliente '{objeto.nome}'.")

    elif operacao == "venda":
        objeto.produto.quantidade += objeto.quantidade
        objeto.cliente.total_gasto -= objeto.valor_total

        vendas = fila_vendas.listar()
        if objeto in vendas:
            vendas.remove(objeto)

        print(f"Venda do produto '{objeto.produto.nome}' desfeita com sucesso!")
