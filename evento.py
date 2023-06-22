import json
class Evento:
    id = 1

    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1
        
    def imprime_informacao(self):
        print(f"ID do evento: {self.id}" )
        print(f"Nome do local: { self.local}")
        print(f"Nome do evento: {self.nome}") 
        print("---------------")
    

    def to_json(self):
        return json.dumps({
            "id":self.id,
            "local":self.local,
            "nome":self.nome
    })

    @staticmethod
    def calcula_limite_pessoas_area(area):
        if area >= 5 and area < 10:
            return 5
        elif area >= 10 and area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0
        


ev = Evento("aula de python")
ev2 = Evento("aula de python","Sao paulo")

print(ev.nome)
print(ev.local)
print(ev2.nome)
print(ev2.local)

ev2.imprime_informacao()

