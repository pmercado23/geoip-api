from django.test import TestCase
from django.urls import reverse
from django.test import Client

# Create your tests here.

class ViewsTests(TestCase):

    def test_sanity(self):
        # Testing Sanity...
        self.assertEqual(1,1)
        self.assertEqual(True, True)


    def test_status(self):
        # Testing /status/ url
        self.client = Client()
        url = reverse('status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_where_am_i(self):
        # Testing /where_am_i/<IPv4>/
        self.client = Client()
        ip0, ip1, ip2, ip3 = '129', '168', '65', '12'
        url = reverse('locate', args=(ip0, ip1, ip2, ip3))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
