from django.db import models


from django.db import models

class SecurityPersonnel(models.Model):
    """
    Model representing a security personnel.
    """

    name = models.CharField(max_length=100)
    # A field to store the name of the security personnel

    company_name = models.CharField(max_length=100)
    # A field to store the name of the company the security personnel belongs to

    passport_photo = models.ImageField(upload_to='passports/')
    # An image field to store the security personnel's passport photo, uploaded to 'passports/' directory

    nin_number = models.CharField(max_length=11)
    # A field to store the National Identification Number (NIN) of the security personnel

    phone_number = models.CharField(max_length=15)
    # A field to store the phone number of the security personnel

    registration_code = models.CharField(max_length=6, unique=True)
    # A unique field to store the registration code of the security personnel

    def __str__(self):
        """
        String representation of the SecurityPersonnel object.
        """
        return self.name
        # Returns the name of the security personnel when the object is printed or displayed
