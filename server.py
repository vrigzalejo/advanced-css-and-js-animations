import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = "."
IGNORE_FILES = {".git", ".gitignore", ".history", "server.py", "readme.md"}

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def list_directory(self, path):
        """Generate an HTML page listing directory contents with clickable links."""
        try:
            files = os.listdir(path)
        except OSError:
            self.send_error(404, "Directory not found")
            return None
        
        html = "<html><head><title>Directory Listing</title></head><body>"
        html += f"<h2>Files in {path}</h2><ul>"

        for file in files:
            if file in IGNORE_FILES:
                continue  # Skip ignored files

            link = f'<li><a href="{file}">{file}</a></li>'
            html += link
        
        html += "</ul></body></html>"
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving HTTP on port {PORT}")

    # Auto-open the browser
    webbrowser.open(f"http://localhost:{PORT}/")
    
    httpd.serve_forever()
