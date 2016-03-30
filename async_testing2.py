from motor import MotorClient
from tornado import gen, testing
from tornado.testing import gen_test

from pymongo import MongoClient


class MyTestCase(testing.AsyncTestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()
        self.client = MotorClient()
        # wait for the setup coroutine to complete before beginning the test
        self.io_loop.run_sync(self.setup_coro)
        
        # for visual control
        client = MongoClient()
        db = client.test
        cursor = db.collection.find()
        for document in cursor:
            print(document)

    @gen.coroutine
    def setup_coro(self):
        collection = self.client.test.collection

        # Clean up from prior runs:
        yield collection.remove()

        yield collection.insert({'_id': 0})
        yield collection.insert({'_id': 1, 'key': 'value'})
        yield collection.insert({'_id': 2})

    @gen_test
    def test_find_one(self):

        collection = self.client.test.collection
        document = yield collection.find_one({'_id': 1})
        self.assertEqual({'_id': 1, 'key': 'value'}, document)
