class Evento:
    def metodo_instancia(self):
        return("método de instancia chamado", self)

    @classmethod
    def metodo_classe(cls): #cls abreviação de class
        return("método de classe chamado",cls)

    @staticmethod
    def metodo_estatico():
        return "estático chamado"

ev = Evento()
a = ev.metodo_instancia() #Evento.metodo_instancia(ev)
print(a)

b = Evento.metodo_classe()#python chama Evento.metodo_classe(Evento)
print(b)

c= Evento.metodo_estatico()#Evento.metodo_estatico()
print(c)

