import time
import socket
from client import Client
import util

class SimpleClient(Client):
	def __init__(self, ip):
		Client.__init__(self)
		self.ip = ip

	def send_request(self,hostname):
		for whitelist_ip_port in self.whitelist:
			request = {"client_ip": self.ip, "hostname":hostname,"timestamp": str(time.time())}
			ip, port = whitelist_ip_port.split(':')
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				print(ip)
				s.connect((ip, 8888))
				try:
					s.sendall(util.json_to_bytes(request))
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