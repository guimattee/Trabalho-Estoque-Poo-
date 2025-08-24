class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self,item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop
        return None
    
    def vazia(self):
        return len(self.itens) == 0
    
    def topo (self):
        if not self.vazia():
            return self.itens[-1]
        return None
    
