class ControleDeEstoque:
    def __init__(self, nome ,validade, quantidade):
        self.nome = nome
        self.validade = validade
        self.quantidade = quantidade
        
from datetime import datetime
data_validade = '02/01/2024'
data_fabricacao = '01/01/2024'
dv_converter = datetime.strptime(data_validade, '%m/%d/%Y')
df_converter = datetime.strptime(data_fabricacao, '%m/%d/%Y')
qts_dias = abs((df_converter - dv_converter).days)
#print(qts_dias)
class Validade(ControleDeEstoque):
    def __str__(self,):
        return f'O produto {self.nome} tem a validade {self.nome}'

class Quantidade(ControleDeEstoque):
    def __str__(self):
        return f'O produto {self.nome} com validade até  {self.validade} vencerá em {qts_dias}  dias , contém {self.quantidade} no estoque. '
    
sabonete = Quantidade('Dove', '02/03/2024', 3)
print(sabonete)