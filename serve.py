#!/usr/bin/env python3
"""Local preview server (standard library only).

    python3 serve.py            -> http://127.0.0.1:8000/

Serves the built site the way GitHub Pages does: /accommodation resolves to
accommodation.html and unknown paths get 404.html. Plain `python3 -m http.server`
also works but will not resolve the extensionless page URLs.
"""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def translate_path(self, path):
        full = super().translate_path(path)
        if not os.path.exists(full) and not os.path.splitext(full)[1] and os.path.isfile(full + ".html"):
            return full + ".html"
        return full

    def send_error(self, code, message=None, explain=None):
        if code == 404 and os.path.isfile(os.path.join(ROOT, "404.html")):
            with open(os.path.join(ROOT, "404.html"), "rb") as f:
                body = f.read()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().send_error(code, message, explain)

    def log_message(self, *args):
        if "-q" not in sys.argv:
            super().log_message(*args)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8000
    print("Serving %s at http://127.0.0.1:%d/" % (ROOT, port))
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
