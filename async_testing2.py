"""
This is a test for my new DasKeyboard

Let's see how much I like it when coding.
"""

from tornado import testing

class MyTestCase(testing.AsyncTestCase):
    def test_delay(self):
        start = time.time()
        delay_async(1, callback=self.stop)
        self.wait()
        duration = time.time() - start
        self.assertAlmostEqual(duration, 1, places=2)





"""
I don't know, if I like this kind of DasKeyboard

a problem, is with the signs =

and the actually very frequently used _ according 
to pep-8 rules




"""

from motor import MotorClient
from tornado import testing


class MyTestCase(testing.AsyncTestCase):
    def setUp(self):
        super().setUp()
        self.client = MotorClient()

    def test_find_one(self):
        collection = self.client.test.collection
        document = yield collection.find_one({})


