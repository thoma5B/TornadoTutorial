from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from tornado import gen
import tornado.tcpserver
import tornado.autoreload
import time

from settings import *

logger = init_logging_mode(__name__)

class Server(tornado.tcpserver.TCPServer):

	def read_string(self, data):
		print data

	@gen.engine
	def handle_stream(self, stream, address):
		print 'Hello new user', address
		data = yield gen.Task(stream.read_until, "\n")
		self.read_string(data)
		stream.close()



class HelloHandler(RequestHandler):
    
    @gen.coroutine
    def get(self):
        #x = yield self.do_test()
        self.render('hello.html', name="Thomas")
        #self.write('hello')

    @gen.coroutine
    def do_test(self):
		yield gen.sleep(3)
		raise gen.Return('test')

routes = [url(r"/", HelloHandler)]
app = Application(routes, debug=DEBUG)

def main():
    app.listen(8888)
    logger.info("listening on localhost:8888")

    # server = Server()
    # server.listen(8889)
    # print "TCPSserver listening on localhost:8889"
    tornado.autoreload.start()

    IOLoop.instance().start()
    

if __name__ == "__main__":
    main()
