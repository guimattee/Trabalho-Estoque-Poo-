class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.vazia():
            return self.itens.pop(0)

    def listar(self):
        return self.itens  # pode até devolver direto, não precisa copiar

    def remover(self, item):
        if item in self.itens:
            self.itens.remove(item)

    def vazia(self):
        return len(self.itens) == 0
    
    


        
