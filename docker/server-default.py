from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = socket
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello from hostname: ' + socket.gethostname().encode())

SERVER_PORT = 8000
httpd = HTTPServer(('0.0.0.0', SERVER_PORT),SimpleHTTPRequestHandler)
print(f'Listening on port {SERVER_PORT} ...')
httpd.serve_forever()