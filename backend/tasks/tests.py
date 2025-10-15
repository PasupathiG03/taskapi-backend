from django.test import TestCase

class SimpleTest(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

class FailTest(TestCase):
    def test_fail(self):
        self.assertEqual(1, 2)  # This test will fail intentionally
