import os, sys, re
from http.server import SimpleHTTPRequestHandler, HTTPServer

class RangeRequestHandler(SimpleHTTPRequestHandler):
    def copyfile(self, source, outputfile):
        try:
            super().copyfile(source, outputfile)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            pass

    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            return super().send_head()
        
        ctype = self.guess_type(path)
        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(404, "File not found")
            return None

        fs = os.fstat(f.fileno())
        total_size = fs[6]
        
        range_header = self.headers.get('Range')
        if not range_header or not range_header.startswith('bytes='):
            self.send_response(200)
            self.send_header("Content-type", ctype)
            self.send_header("Content-Length", str(total_size))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.end_headers()
            return f

        match = re.match(r'bytes=(\d*)-(\d*)', range_header)
        if not match:
            self.send_error(416, "Requested Range Not Satisfiable")
            f.close()
            return None

        start_str, end_str = match.groups()
        start = int(start_str) if start_str else 0
        end = int(end_str) if end_str else total_size - 1
        
        if start >= total_size:
            self.send_error(416, "Requested Range Not Satisfiable")
            f.close()
            return None

        if end >= total_size:
            end = total_size - 1

        length = end - start + 1
        f.seek(start)
        
        self.send_response(206)
        self.send_header("Content-type", ctype)
        self.send_header("Content-Range", f"bytes {start}-{end}/{total_size}")
        self.send_header("Content-Length", str(length))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f

def run():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    server = HTTPServer(('0.0.0.0', port), RangeRequestHandler)
    print(f"Serving on port {port} with Range support...")
    server.serve_forever()

if __name__ == '__main__':
    run()
