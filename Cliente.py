class Cliente:
    def __init__(self,id, nome):
        self.id = id
        self.nome = nome
        self.total_gasto = 0
    
    def __str__(self):
        return f"ID: {self.id} - Nome: {self.nome} - Total Gasto: R${self.total_gasto}: "