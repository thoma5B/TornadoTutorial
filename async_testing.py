import time
# import unittest

from tornado import gen
# from tornado.ioloop import IOLoop
# from tornado.stack_context import ExceptionStackContext


# def delay(seconds):
#     time.sleep(1)
#     return


@gen.coroutine
def delay_async(seconds, callback=lambda: None):
    yield gen.sleep(seconds)
    callback()
    raise gen.Return(True)


# class MyTestCase(unittest.TestCase):
#     def test_delay(self):
#         start = time.time()
#         io_loop = IOLoop.instance()

#         def done():
#             duration = time.time() - start
#             self.assertAlmostEqual(duration, 1, places=2)
#             io_loop.stop()
        
#         self.failure = None
        
#         def handle_exception(typ, value, tb):
#             print typ, value, tb
#             io_loop.stop()
#             self.failure = value
#             return True  # Stop propagation.

#         with ExceptionStackContext(handle_exception):
#             delay_async(2, done)

#         # delay_async(2, done)
#         io_loop.start()
#         if self.failure:
#             raise self.failure


from tornado import testing


class MyTestCase(testing.AsyncTestCase):
    def test_delay(self):
        start = time.time()
        delay_async(1, callback=self.stop)
        self.wait()
        duration = time.time() - start
        self.assertAlmostEqual(duration, 2, places=2)
