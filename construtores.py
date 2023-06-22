#Como forçar um objeto ao ser criado a ter um conjunto de atributos
#Serve para inicialização do nosso objeto, 
#Para que nosso objeto, ao ser instanciado tenha um conjunto de valores e atributos
class Evento:
    def __init__(self,nome, local):
        self.nome = nome
        self.local = local
    def altera_nome_evento(self, novo_nome):#o self assume o valor do objeto que chamou essa função(no caso é o ev)
        print("Alterando nome do evento")
        self.nome = novo_nome

ev = Evento("Aula de Python", "Inglaterra")
ev2 = Evento("Aula de Javascript", "Alemanha")


print(ev.nome)
print(ev.local)
print(ev2.nome)
print(ev2.local)