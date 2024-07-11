# security/tests.py
from datetime import date
from django.test import TestCase
from access.models import AccessCode  # Corrected import
from .models import SecurityPersonnel
from django.core.files.uploadedfile import SimpleUploadedFile
from residents.models import Resident, Landlord

class SecurityPersonnelModelTest(TestCase):
    def setUp(self):
        # Create a mock image file for testing purposes
        mock_image = SimpleUploadedFile("test_passport.jpg", b"file_content", content_type="image/jpeg")
        
        self.landlord = Landlord.objects.create(
            name='John Doe',
            phone_number='1234567890'
        )

        self.resident = Resident.objects.create(
            name='Jane Doe',
            landlord=self.landlord,
            phone_number='0987654321',
            date_moved_in='2023-01-01',
            rent_due_date='2024-01-01',
            estate_name='Green Estate',
            passport_photo='path/to/photo.jpg'
        )

        self.security_personnel = SecurityPersonnel.objects.create(
            name='Security Officer',
            company_name='Security Company',
            passport_photo=mock_image,
            nin_number='12345678901',
            phone_number='1234567890',
            registration_code='ABCDE'
        )
        self.access_code = AccessCode.objects.create(
            code='ABCD12',
            resident=self.resident,
            created_at='2023-01-01',
            expires_at='2023-12-31T23:59:59Z'
        )

    def test_security_personnel_creation(self):
        self.assertEqual(self.security_personnel.name, 'Security Officer')
        self.assertEqual(self.security_personnel.company_name, 'Security Company')

    def test_access_code_creation(self):
        self.assertEqual(self.access_code.code, 'ABCD12')

if __name__ == "__main__":
    import unittest
    unittest.main()
