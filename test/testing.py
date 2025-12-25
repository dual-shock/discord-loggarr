#http://127.0.0.1:8080/
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from dotenv import load_dotenv

load_dotenv()


forwarded_host_port = os.environ.get("HOST_PORT")
container_port = os.environ.get("CONTAINER_PORT")
discord_token = os.environ.get("DISCORD_TOKEN")


content = f"""
This docker application is running on: {{
    container_port: {container_port},
    host_port: {forwarded_host_port},
    the token is: {discord_token}
}} :3
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

local_port = ("", int(forwarded_host_port))
httpd = HTTPServer(local_port, Handler)

print(f"server started on container port: {container_port}, host port: {forwarded_host_port}")

httpd.serve_forever()

