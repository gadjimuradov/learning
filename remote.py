import socket

def get_remote_machine():
	remote_host = 'www.python.org'
	try:
		print(socket.gethostbyname(remote_host))
	except socket.error as err_msg:
		print(err_msg)

if __name__ == '__main__':
	get_remote_machine()

		