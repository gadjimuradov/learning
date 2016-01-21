import subprocess
import shlex

class Pinger(object):

	def __init__(self, target_host, count=4,timeout=2):
		self.target_host = target_host
		self.count = count
		self.timeout = timeout

	def checksum(self, source_string):
		sum = 0
		max_count = (len(source_string)/2) * 2
		count = 0
		while  count < max_count:
			val = ord(source_string[count + 1]) * 256 + 
			ord(source_string[count])
			sum += val
			sum = sum & 0xffffffff
			count += 2
		if max_count < len(source_string):
			pass
			
			

