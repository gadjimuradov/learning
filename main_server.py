import logging
import socket
import multiprocessing


def handle(connection, address):
    logging.basicConfig(level=logging.DEBUG)
	logger = logging.getLogger("process-%r" % (address,))
	try:
		print("handle start")
		logger.debug("Connected %r at %r", connection, address)
		while True:
			print("f")
			data = connection.recv(1024)
			connection.sendall(data)
	except:
		logger.exception("We have problems")


class Server(object):
	def __init__(self, hostname, port):
		self.logger = logging.getLogger('server')
		self.hostname = hostname
		self.port = port
    
    def start(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((self.hostname, self.port))
		self.socket.listen(1)
		print("Server start")
		while True:
			conn,address = self.socket.accept()
			self.logger.debug("Got connection")
			process = multiprocessing.Process(target=handle,args=(conn,address))
			process.daemon = True
			print("Daemon thread")
			process.start()
			self.logger.debug("Started process %r", process)
			print("Start process")


if __name__ == "__main__":
	server = Server("0.0.0.0",9000)
	try:
		logging.info("Listening")
		server.start()
		logging.debug('This is a debug message' )
	except:
		logging.exception("Exception")
	finally:
		logging.info("Shutting down")
		for pr in multiprocessing.active_children():
			logging.info("Shutting down process %r",process)
			process.terminate()
			process.join()
