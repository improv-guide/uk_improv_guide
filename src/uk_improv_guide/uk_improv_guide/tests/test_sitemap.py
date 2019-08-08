from django.test import TestCase

class TestSitemap(TestCase):


    def test_sitemap_can_be_loaded(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)