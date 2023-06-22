from evento import Evento

class EventoOnline(Evento):
    def __init__(self, nome, _=""):
       local = f"https://tamarcado.com/eventos?id={EventoOnline.id}"
       super().__init__(nome, local)

    def imprime_informacao(self):
        print(f"ID do evento: {self.id}" )
        print(f"Link para acessar: { self.local}")
        print(f"Nome do evento: {self.nome}") 
        print("---------------")