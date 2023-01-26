from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SnacksTests(TestCase):
    def test_home_page_status(self):
        url = reverse('home')
        print(f'the url is: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snacks_page_status(self):
        url = reverse('snack_list')
        print(f'the url is: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snacks_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')