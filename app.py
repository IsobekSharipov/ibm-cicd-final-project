"""Minimal HTTP application for the IBM CI/CD OpenShift project."""

import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    """Handle health-check and application HTTP requests."""

    def do_GET(self):
        """Return a simple response for the application and health checks."""
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"SERVICERUNNING\n")


def main():
    """Start the HTTP server on the configured port."""
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), RequestHandler)
    print(f"SERVICERUNNING on port {port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
