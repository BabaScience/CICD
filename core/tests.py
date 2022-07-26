from django.test import TestCase



class BaseTest(TestCase):
    def test_abc(self):
        self.assertTrue(False)