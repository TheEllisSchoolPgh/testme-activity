import http.server
import socketserver

PORT = 8000

class CustomHeaderHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add the specific headers you requested
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        
        # Call the superclass method to finish sending headers
        super().end_headers()

# Prevent "Address already in use" errors during restarts
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), CustomHeaderHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.shutdown()