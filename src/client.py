from __future__ import print_function
from cmd import Cmd
import sys

class Client(Cmd):

	def __init__(self, whitelist_location='whitelist.txt'):
		Cmd.__init__(self)
		self.prompt = '> '

		self.whitelist_location = whitelist_location
		self.whitelist= []

		# load ip's into cache
		with open(self.whitelist_location, 'r') as whitelist:
			for ip in whitelist: 
				self.whitelist.append(ip.rstrip('\n'))

	def run(self):
		self.cmdloop('Welcome fellow anarchist!\nWelcome to the future that is P2P-DNS!')

	def do_list(self, args):
		"""List IPs in whitelist"""
		for ip in self.whitelist:
			print(ip)

	def do_get(self, args):
		"""Search for given hostname"""
		if len(args) == 0:
			print('Error: No hostname argument passed')
		else:
			print(send_request())

	def do_add(self, args):
		"""Add given ip to list of trusted servers"""
		if len(args) == 0:
			print('Error: No ip argument passed')
		elif args in self.whitelist:
			print('Error: ip already exists in whitelist')
		else:
			try:
				with open(self.whitelist_location, 'a') as f: 
					f.write(args+'\n')
				self.whitelist.append(args)
			except:
				print("Unexpected error:", sys.exc_info()[0])
				raise

	def do_remove(self, args):
		"""Delete given ip from list of trusted servers"""
		if len(args) == 0:
			print('Error: No ip argument passed')
		elif not args in self.whitelist:
			print('Error: ip not in whitelist')
		else:
			try:
				ips = []
				with open(self.whitelist_location,'r') as f:
					ips = f.readlines()
					f.close()
				with open(self.whitelist_location,'w') as f:
					self.whitelist= []
					for ip in ips:
						if ip.rstrip('\n') != args:
							f.write(ip)
							self.whitelist.append(ip.rstrip('\n'))
			except:
				print("Unexpected error:", sys.exc_info()[0])
				raise

	def send_request():
		raise NotImplementedError
			

	def do_quit(self, args):
		"""Quits the program."""
		print('Quitting.')
		raise SystemExit


class SimpleClient(Client):
	def send_request():
		pass

if __name__ == '__main__':
	SimpleClient().run()