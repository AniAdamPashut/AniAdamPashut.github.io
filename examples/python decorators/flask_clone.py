import socket
from typing import Callable

class Server:
    def __init__(self):
        self.ip = '0.0.0.0'
        self.port = 8080
        self._endpoints: dict[str, Callable] = dict()

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self._socket.bind((self.ip, self.port))
        self._socket.listen()

        while True:
            client, addr = self._socket.accept()
            print("Connected from + ", addr)

            self._handle(client)
            client.close()

    def _extract_http_request(self, client_socket):
        # ChatGPT
        # Set a timeout for socket operations
        client_socket.settimeout(1)
        
        # Initialize an empty buffer to store received data
        request_buffer = b""
        
        # Read data from the socket until the end of the HTTP request
        while True:
            try:
                # Receive data from the socket
                data = client_socket.recv(4096)
                
                # If no more data is received, break the loop
                if not data:
                    break
                
                # Append received data to the buffer
                request_buffer += data
                
                # Check if the end of the HTTP request headers is reached
                if b"\r\n\r\n" in request_buffer:
                    break
            except socket.timeout:
                # If a timeout occurs, break the loop
                break
        
        # Convert the received data to a string (assuming it's ASCII)
        request_str = request_buffer.decode()
        
        # Return the full HTTP request
        return request_str

    def _handle(self, client: socket.socket):
        data = self._extract_http_request(client)
        """
        GET / HTTP/1.1
        """
        splitted = data.split()
        ep = splitted[1]

        # You should have a 404 function if this fails
        response = self._endpoints[ep]()
        client.send(response.encode())

    def route(self, ep):
        def inner(method): 
            self._endpoints[ep] = method
            return method
        return inner


app = Server()

@app.route("/")
def index():
    return "Hello, World"

app.run()

