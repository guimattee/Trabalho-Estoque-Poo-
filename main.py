from Cliente import Cliente
from Produto import Produto
from Venda import Venda
from Fila import Fila
from Pilha import Pilha
from funcoes import *
estoque = []
clientes = []
fila_vendas = Fila()
pilha_operacoes = Pilha()


def menu():
    while True:
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar produto")
        print("4 - Listar produtos do estoque")
        print("5 - Realizar venda")
        print("6 - Ver fila de vendas")
        print("7 - Desfazer última operação")
        print("8 - Exibir valor total do estoque")
        print("9 - Exibir valor total de vendas realizadas")
        print("10 - Exibir clientes e valores gastos")
        print("11 - Sair")

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("Opção inválida!")
            continue

        if opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            listar_clientes()
        elif opcao == 3:
            cadastrar_produto()
        elif opcao == 4:
            listar_produtos()
        elif opcao == 5:
            realizar_venda()
        elif opcao == 6:
            listar_vendas()
        elif opcao == 7:
            desfazer()
        elif opcao == 8:
            valor_total_estoque()
        elif opcao == 9:
            valor_total_vendas()
        elif opcao == 10:
            listar_clientes_valores()
        elif opcao == 11:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()