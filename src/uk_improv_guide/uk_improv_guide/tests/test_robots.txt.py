from django.test import TestCase


class YourTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_sitemap_can_be_loaded(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
