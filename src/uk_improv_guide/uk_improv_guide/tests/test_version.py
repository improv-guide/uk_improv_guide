from django.test import TestCase


class TestSettings(TestCase):
    def testVersion(self):
        from uk_improv_guide import __version__
        a,b,c = [int(x) for x in __version__.split(".")]
        self.assertTrue(any(x > 0 for x in [a,b,c]))
