#!/usr/bin/env python3
"""
Simple local HTTP server for the project.
Usage:
  python server.py [port]
This serves the current directory on the given port (default 8000)
and attempts to open the default browser to the site.
"""
import http.server
import socketserver
import socket
import webbrowser
import sys

PORT = 8000

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow cross-origin requests (useful for some local fetches)
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()


def find_host():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            pass

    host = find_host()
    url = f'http://{host}:{PORT}/'
    print(f'Serving HTTP on 0.0.0.0 port {PORT} (accessible at {url})')
    try:
        webbrowser.open(url)
    except Exception:
        pass

    with socketserver.TCPServer(("", PORT), CORSHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nServer stopped by user')
            httpd.server_close()
