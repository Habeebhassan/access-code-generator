from django.test import TestCase
from .models import Resident, Landlord

class ResidentModelTest(TestCase):
    def setUp(self):
        self.landlord = Landlord.objects.create(name='John Doe', phone_number='1234567890')
        self.resident = Resident.objects.create(
            name='Jane Doe',
            landlord=self.landlord,
            phone_number='0987654321',
            date_moved_in='2023-01-01',
            rent_due_date='2024-01-01',
            estate_name='Green Estate',
            passport_photo='path/to/photo.jpg'
        )

    def test_resident_creation(self):
        self.assertEqual(self.resident.name, 'Jane Doe')
        self.assertEqual(self.resident.landlord.name, 'John Doe')
        self.assertEqual(self.resident.phone_number, '0987654321')
        self.assertEqual(self.resident.estate_name, 'Green Estate')

class ResidentViewTest(TestCase):
    def setUp(self):
        self.landlord = Landlord.objects.create(name='John Doe', phone_number='1234567890')
        self.resident = Resident.objects.create(
            name='Jane Doe',
            landlord=self.landlord,
            phone_number='0987654321',
            date_moved_in='2023-01-01',
            rent_due_date='2024-01-01',
            estate_name='Green Estate',
            passport_photo='path/to/photo.jpg'
        )

    def test_dashboard_view(self):
        response = self.client.get(f'/residents/{self.resident.id}/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jane Doe')
