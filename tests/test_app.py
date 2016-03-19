from selenium import webdriver
import unittest
# import tornado.testing
from tornado import gen
from tornado.testing import AsyncHTTPTestCase, AsyncTestCase, gen_test
from tornado.ioloop import IOLoop

from colorama import Fore

import app

#app.main()  # doesn't work; must be called asyncronously, see below


# class TestHelloApp(AsyncHTTPTestCase):
#     def get_app(self):
#         return app.app

#     def test_homepage(self):
#         response = self.fetch('/')
#         print response
#         self.assertEqual(response.code, 200), 
#         self.assertEqual(response.body, 'Hello K')

class MyTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	#@gen.coroutine
	def client_accesses_api_via_browser(self):
		
		self.browser.get('http://localhost:8888')
		print Fore.RED + '=============================\n\n' + Fore.RESET
		print self.browser.title, self.browser.__dict__
		# self.assertIn('http', self.browser.title)		# raise gen.Return(True)
		self.assertIn('Hello Thomas', self.browser.page_source)


	def test_post(self):
		self.client_accesses_api_via_browser()

