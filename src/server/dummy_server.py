import socketserver
import threading
import bus_sim

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"Received: {self.data}")
        self.request.sendall(b"Connection successful")
        
if __name__ == "__main__":
    HOST, PORT = "localhost", 8888
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True  # Allow program to exit even if this thread is still running
        server_thread.start()
        print(f"Server started at {HOST}:{PORT}")
        
        try:
            while True:
                pass  # Keep the main thread running to keep the server alive
        except KeyboardInterrupt:
            print("Shutting down server.")
            server.shutdown()
            server.server_close()
            