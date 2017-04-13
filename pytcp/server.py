import socket
import sys
import logging


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



class server:
	def __init__(self,host,port):
		self.host = host
		self.port = port

	def start(self):
		
		socket.bind((self.host,self.port))
		socket.listen(10) # Number of clients
		#Loop while the connection terminate with keyboard ineterruption ctr+c
		try:
			while True:
				conn, address = socket.accept()
				logging.info("connected from", address)
				print("connected from",address)

				while True:
					data = conn.recv(1024)
					if not data : break
					conn.send(data)

		
				conn.close( )
				logging.info("Disconnected from ",address)
		finally:
			socket.close( )

a=server(host='0.0.0.0',port=9998)
a.start()