from __future__ import print_function
from cmd import Cmd
import sys
import re
import json
import socket
import util

# www.google.com

class Client(Cmd):

	def __init__(self, whitelist_location='whitelist.txt'):
		Cmd.__init__(self)
		self.prompt = '> '

		self.whitelist_location = whitelist_location
		self.whitelist= []
		self.r = re.compile('.*..*..*:.*')
		# TODO load this in configuration
		self.timeout = 1

		# load ip's into cache
		with open(self.whitelist_location, 'r') as whitelist:
			for ip in whitelist: 
				self.whitelist.append(ip.rstrip('\n'))

	def listen(self,port):
		HOST = 'localhost' 
		PORT = port              # Arbitrary non-privileged port
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			#s.setdefaulttimeout(self.timeout)
			s.settimeout(self.timeout)
			s.bind((HOST, PORT))
			try:
				s.listen(1)
				conn, addr = s.accept()
				with conn:
					response = util.bytes_to_json(conn.recv(1024))
					return response
			except Exception as e:
				print("request timed out")
		return {}			

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
			print(self.send_request(args))

	def do_add(self, args):
		"""Add given ip to list of trusted servers"""
		if len(args) == 0:
			print('Error: No ip argument passed')
		elif self.r.match(args)	is None:
			print('Error: Ip argument not proper format')
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
		elif self.r.match(args)	is None:
			print('Error: Ip argument not proper format')	
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

	def do_set_timeout(self,args):
		if len(args) == 0:
			print('Error: argument passed')
		elif self.r.match(args)	is None:
			print('Error: Ip argument not proper format')	
		self.timeout = float(args)			

	def do_quit(self, args):
		"""Quits the program."""
		print('Quitting.')
		raise SystemExit

	def send_request(self,hostname):
		raise NotImplementedError( "Tried to run abstract method" )