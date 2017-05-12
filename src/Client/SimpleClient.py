import time
import socket
from client import Client

class SimpleClient(Client):
	def __init__(self, ip):
		Client.__init__(self)
		self.ip = ip

	def send_request(self,hostname):
		for whitelist_ip_port in self.whitelist:
			request = {"client_ip": self.ip, "hostname":hostname,"timestamp": str(time.time())}
			ip, port = whitelist_ip_port.split(':')
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				port = int(port)
				s.connect((ip, port))
				try:
					s.sendall(json_to_bytes(request))
					response = self.listen(3333)
					return response
				except socket.error as msg:
					s = None
					continue
				finally:
					s.close()
		return {}			

if __name__ == '__main__':
	SimpleClient("127.0.0.1:3333").run()