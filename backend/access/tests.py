from django.test import TestCase
from residents.models import Resident, Landlord
from .models import AccessCode
from datetime import datetime, timedelta

class AccessCodeModelTest(TestCase):
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

        # Calculate expiry date, e.g., 30 days from today
        expires_at = datetime.now() + timedelta(days=30)

        self.access_code = AccessCode.objects.create(
            code='123456',
            resident=self.resident,
            created_at='2023-01-01',
            expires_at=expires_at
        )

    def test_access_code_creation(self):
        self.assertEqual(self.access_code.code, '123456')
        self.assertEqual(self.access_code.resident.name, 'Jane Doe')
        self.assertEqual(self.access_code.expires_at, self.access_code.expires_at)

class AccessCodeViewTest(TestCase):
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

    def test_generate_code_view(self):
        response = self.client.post('/generate_code/', {'resident_id': self.resident.id})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access_code' in response.json())
