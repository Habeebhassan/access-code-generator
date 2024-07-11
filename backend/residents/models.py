from django.db import models


class Landlord(models.Model):
    """
    Model representing a landlord.
    """

    name = models.CharField(max_length=100)
    # A field to store the name of the landlord
    phone_number = models.CharField(max_length=20, default='00000000000')
    # A feild to store landlord phone number

    def __str__(self):
        """
        String representation of the Landlord object.
        """
        return self.name
        # Returns the name of the landlord when the object is printed or displayed

class Resident(models.Model):
    """
    Model representing a resident.
    """

    name = models.CharField(max_length=100)
    # A field to store the name of the resident

    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    # A foreign key linking Resident to Landlord, with CASCADE deletion behavior
    # (deleting a Landlord deletes all associated Residents)

    phone_number = models.CharField(max_length=15)
    # A field to store the phone number of the resident

    date_moved_in = models.DateField()
    # A field to store the date the resident moved into the estate

    rent_due_date = models.DateField()
    # A field to store the date when rent is due

    estate_name = models.CharField(max_length=100)
    # A field to store the name of the estate where the resident lives

    passport_photo = models.ImageField(upload_to='passports/')
    # An image field to store the resident's passport photo, uploaded to 'passports/' directory

    def __str__(self):
        """
        String representation of the Resident object.
        """
        return self.name
        # Returns the name of the resident when the object is printed or displayed

