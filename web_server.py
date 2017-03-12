from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
import time

class S(SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print "got get request %s" % (self.path)
        if self.path == '/':
          self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        print "got post!!"
        if self.path.find("/save")==0:
            state = self.path.split("/")[2]
            content_len = int(self.headers.getheader('content-length', 0))
            print content_len
            post_body = self.rfile.read(content_len)
            output=open("images/"+state+"/"+str(time.time())+".png","wb")
            output.write(post_body)
            output.close()
        else:
            return SimpleHTTPRequestHandler.do_POST(self)

def run(handler_class=S, port=80):
    httpd = SocketServer.TCPServer(("", port), handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

run(port=8080)
