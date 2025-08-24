class Fila:
    def __init__(self):
        self.itens  = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.vazia():
            self.itens.pop(0)
            print("Item removido")
            return
        return None
    
    def vazia(self):
        return len(self.itens) == 0
    
    def listar (self):
        return self.itens
    
    


        
