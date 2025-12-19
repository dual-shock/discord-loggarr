#http://127.0.0.1:8080/
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

forwarded_host_port = os.environ.get("HOST-PORT")

content = """
This docker application is running on: {
    container_port: 8080,
    host_port: 12345
} :3
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

local_port = ("", 8080)
httpd = HTTPServer(local_port, Handler)

print(f"server started on container port: {8080}, host port: {forwarded_host_port}")

httpd.serve_forever()

