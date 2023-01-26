from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack

# Thanks to JB @ CodeFellows for many of these tests
# Create your tests here.
class SnacksTests(TestCase):
    def test_index_page_status(self):
        url = reverse('index')
        print(f'the url is: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_page_template(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_snacks_page_status(self):
        url = reverse('snack_list')
        print(f'the url is: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snacks_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, '_base.html')

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="Qwerty$01"
        )

        self.snack = Snack.objects.create(
            name="cereal", rating=1, reviewer=self.user, description="cereal description",
            image_url="https://www.hitpromo.net/imageManager/show/ZBOX-MINCEREAL_blank2.jpg"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "cereal")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.name}", "cereal")
        self.assertEqual(f"{self.snack.reviewer}", "tester")
        self.assertEqual(self.snack.rating, 1)

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cereal")
        self.assertTemplateUsed(response, "snack_list.html")

    # def test_snack_detail_view(self):
    #     response = self.client.get(reverse("snack_detail", args="1"))
    #     no_response = self.client.get("/100000/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, "Reviewer: tester")
    #     self.assertTemplateUsed(response, "snack_detail.html")

    # def test_snack_create_view(self):
    #     response = self.client.post(
    #         reverse("snack_create"),
    #         {
    #             "name": "Pops",
    #             "description": "Gotta have 'em",
    #             "reviewer": self.user.id,
    #             "rating": 2
    #
    #         }, follow=True
    #     )
    #
    #     self.assertRedirects(response, reverse("snack_detail", args="2"))
    #     self.assertContains(response, "Pops")

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"name": "Updated name", "rating": 3, "reviewer": self.user.id, "description": "test description",
             "image_url": "testimageurl.com"}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"), target_status_code=200)

    def test_snack_update_bad_url(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"name": "Updated name", "rating": 3, "reviewer": self.user.id, "description": "test description",
             "image_url": "badurl"}
        )

        self.assertEqual(response.status_code, 200)

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)

