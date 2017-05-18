import server_schema as servers
import socket

class DummyDNSServer(servers.DNSServerHandler):
	def on_request_recieve( self , request):
		print("recieved: \n{}\n".format(str(request)))
		return False
	def on_request_resolve( self , request, response):
		print("resolved: \n{}\n with: \n{}\n".format(str(request),str(response)))
	def on_request_fail( self , request):
		print("failed to resolve: \n{}\n".format(str(request)))

class LazyDNSServer(servers.DNSServerHandler):
	def on_request_recieve( self , request):
		print("recieved: \n{}\n".format(str(request)))
		try:
			ip = socket.gethostbyname(request["hostname"])
			response = {}
			response["hostname"] = request["hostname"]
			response["timestamp"] = request["timestamp"]
			response["target_ip"] = ip
			return response
		except:
			return False
		return False
	def on_request_resolve( self , request, response):
		print("resolved: \n{}\n with: \n{}\n".format(str(request),str(response)))
	def on_request_fail( self , request):
		print("failed to resolve: \n{}\n".format(str(request)))


if __name__ == "__main__":
    ip = 'localhost'
    port = 8888
    print("serving on port ", port)
    server = servers.DNSServer(ip,port,LazyDNSServer)
    server.run()