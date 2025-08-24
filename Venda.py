class Venda:
    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = produto.preco * quantidade

    def __str__(self):
        return f"Cliente: {self.cliente.nome} - Produto: {self.produto.nome} - Quantidade: {self.quantidade} - Valor: R${self.valor_total}: "

