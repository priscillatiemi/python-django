class Evento:
    def altera_nome_evento(self, novo_nome):#o self assume o valor do objeto que chamou essa função(no caso é o ev)
        print("Alterando nome do evento")
        self.nome = novo_nome

ev = Evento()
#Parece a chamada de uma função, mas é a chamada de uma classe(Evento)
#Parece com valor referência. Podemos adicionar atributos dinamicamente
ev.nome = "Aula de python"
print(ev.nome)

ev.altera_nome_evento("Aula de javascript")#chama um método a partir do objeto altera_nome_evento
#Evento.altera_nome_evento(ev, ev, "..."), está como se estivesse passando ev duas vezes.
# No python, é como se já estivesse usando o primeiro parâmetro.
# O primeiro parâmetro sempre é referência para o proprio metodo 
print(ev.nome)
#o self é parecido com o this.nome no java. Referencia o próprio objeto
#obj.metodo(1, 2, 3) => Evento.metodo(obj, 1, 2, 3)