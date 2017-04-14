#Cuncurrent client support is to be included
import socket
import sys
import logging


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



class tcpserver:
	def __init__(self,host,port):
		self.host = host
		self.port = port

	def start(self):
		
		socket.bind((self.host,self.port))
		socket.listen(10) # Number of clients
		print("listening on",self.port)
		#Loop while the connection terminate with keyboard ineterruption ctr+c
		try:
			while True:
				conn, address = socket.accept()
				logging.info("connected from", address)
				print("connected from",address)

				while True:
					data = conn.recv(1024)
					if not data : break
					size=str(len(data.decode("utf-8")))
					size=bytes(size, 'utf=8')
					conn.send(size)

		
				conn.close( )
				print("Disconnected from ",address)
		finally:
			socket.close( )


