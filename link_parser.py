from queue import Queue
import threading
import urllib.request as urllib2
import time
from bs4 import BeautifulSoup


class Consumer(threading.Thread):
    def __init__(self, queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while True:
			content = self._queue.get()		
			if isinstance(content,str) and content == 'quit':
				break
			response = urllib2.urlopen(content)
			html = response.read()
			soup = BeautifulSoup(html)
			title = soup.html.head.title
			print(title)
			self._queue.task_done()

def build_worker_pool(queue, size):
	workers = []
	for _ in range(size):
		worker = Consumer(queue)
		worker.start()
		workers.append(worker)
	return workers	

def main():
	urls = [
		'http://www.python.org', 'http://www.yahoo.com',
		'http://www.scala.org','http://www.php.net',
		'http://www.scala.org',	'http://www.python.org', 'http://www.yahoo.com',
	] 

	queue = Queue()
	worker_threads = build_worker_pool(queue,2)
	start_time = time.time()

	for url in urls:
		queue.put(url)

	for worker in worker_threads:
		queue.put('quit')

	for worker in worker_threads:
		worker.join()
	print (format(time.time() - start_time))
		
if __name__ == '__main__':
	main()
