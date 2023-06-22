from evento import Evento
from evento_online import EventoOnline

ev_online = EventoOnline("Live de python")
ev2_online = EventoOnline("Live de Javascript")
# ev_online.imprime_informacao()
# ev2_online.imprime_informacao()
print(ev_online.to_json())
print(ev2_online.to_json())
ev = Evento("Aula de Python","Rio de Janeiro")

ev.imprime_informacao()

#Evento importou EventoOnline
#EventoOnline importando Evento
#app importa tanto Evento quanto EventoOnline
#EventoOnline depende de Evento
