from http.server import HTTPServer, BaseHTTPRequestHandler
from evento_online import EventoOnline
from evento import Evento

ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de Javascript")
ev3_online = Evento("aula de python","Sao paulo")
eventos = [ev_online, ev2_online, ev3_online]

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type","text/html; charset=utf-8")
            self.end_headers()
            data = f"""
            <html>
                <head>
                    <title>Olá, Mundo!</title>
                </head>
                <body>
                    <p>Testando nosso servidor HTTP</p>
                    <p>Diretorio: {self.path}</p>
                </body>
            </html>
            """.encode()
            self.wfile.write(data)
        elif self.path == "/eventos":
            self.send_response(200)
            self.send_header("Content-type","text/html; charset=utf-8")
            self.end_headers()
            eventos_html = ""
            for ev in eventos:
                eventos_html += f"<p>{ev.id} {ev.nome} {ev.local}</p>"
            data = f"""
            <html>
            {eventos_html}
            </html>
            """.encode()
            self.wfile.write(data)
server = HTTPServer(('localhost',8000),SimpleHandler)
server.serve_forever()