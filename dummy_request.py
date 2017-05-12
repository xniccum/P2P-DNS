import socket
import server_schema as servers


def listen(port):
	HOST = 'localhost'                 # Symbolic name meaning all available interfaces
	PORT = port              # Arbitrary non-privileged port
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen(1)
		conn, addr = s.accept()
		with conn:
			response = servers.bytes_to_json(conn.recv(1024))
			return response
	return {}with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:


ip = 'localhost'
port = 8888

message = {"client_ip":"127.0.0.1:3333","hostname":"www.google.com","timestamp":"12030213014121321"}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))
try:
	sock.sendall(servers.json_to_bytes(message))
	response = listen(3333)
	print(response)
finally:
    sock.close()

