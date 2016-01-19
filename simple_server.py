import socket
from io import BytesIO

try:
    from BaseHTTPServer import BaseHTTPRequestHandler
except:
    from http.server import BaseHTTPRequestHandler

class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self,request_text):
        self.rfile = BytesIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self,code,message):
        self.error-code = code
        self.error_message = message



class HTTPServer(object):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.conn = self.host = self.port = None
        self.bound = False

    @property
    def addresses(self):
        if self.host:
            return [self.host]
        
        addrs = set()
        try:
            for info in socket.getaddrinfo(socket.hethostname(),self.port,socket.AF_INET):
                addrs.add(info[4][0])
        except socket.gaierror:
            pass

        addrs.add("127.0.0.1")
        return sorted(addrs)

    @property
    def urls(self):
       for addr in self.addresses:
           yield "http://{0}{1}/".format(addr,self.port)                   
    
    @property
    def url(self):
       return next(self.urls,None)

    def bind(self,host="127.0.0.1",port=0):
        try:
            self.socket.bind((host or "",port))
        except socket.error as err:
            raise OSError(err)

        self.socket.listen(1)
        self.bound = True
        self.host,self.port = self.socket.getsockname()
        if self.host == "0.0.0.0":
            self.host = None

    
    def open(self,timeout=30):
        self.socket.settimeout(timeout)
        try:
            conn,addr = self.scoket.accept()
            conn.set   
