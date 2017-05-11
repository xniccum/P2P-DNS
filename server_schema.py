import socket
import socketserver
import json

max_message_length = 1024

def json_to_bytes(js):
    return json.dumps(js).encode('utf-8')
def bytes_to_json(bts):
    return json.loads(bts.decode('utf-8'))

class DNSServerHandler(socketserver.BaseRequestHandler):

    def on_request_recieve( self , request):
        raise NotImplementedError( "Tried to run abstract method" )
    def on_request_resolve( self , request, response):
        raise NotImplementedError( "Tried to run abstract method" )
    def on_request_fail( self , request):
        raise NotImplementedError( "Tried to run abstract method" )

    def recieve(self):
        return bytes_to_json(self.request.recv(max_message_length))

    def send(self, ip, port, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        try:
            sock.sendall(json_to_bytes(message))
        finally:
            sock.close()

    def handle(self):
        request = self.recieve()
        response = self.on_request_recieve(request)
        if response:
            ip, port = request['client_ip'].split(':')
            port = int(port)
            self.send(ip,port,response)
            self.on_request_resolve(request, response)
        else:
            self.on_request_fail(request)

class DNSServer(socketserver.TCPServer):

    stopped = False
    allow_reuse_address = True

    def __init__(self, ip, port, handler):
        super(DNSServer, self).__init__((ip,port), handler)

    def serve_forever(self):
        while not self.stopped:
            self.handle_request()

    def force_stop(self):
        self.server_close()
        self.stopped = True
        self.serve_forever()
        
    def run(self):
        try:
            self.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self.force_stop()
