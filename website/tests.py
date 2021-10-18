from django.test import TestCase
from django.shortcuts import reverse


class TestViews(TestCase):
    
    def test_index_view_renders(self):
        url = reverse("website:index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("Healthy Living".encode(), resp.content)
    
    def test_about_view_renders(self):
        url = reverse("website:about")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("About Us".encode(), resp.content)
        self.assertIn("Our Doctors".encode(), resp.content)

    def test_contact_view_renders(self):
        url = reverse("website:contact")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("Get in Touch".encode(), resp.content)
        self.assertIn("contact".encode(), resp.content)

    def test_gallery_view_renders(self):
        url = reverse("website:gallery")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("Our Gallery".encode(), resp.content)
        self.assertIn("Gallery".encode(), resp.content)

    
       