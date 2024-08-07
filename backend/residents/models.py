from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

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

class ResidentManager(BaseUserManager):
    """
    Manager class for Resident model to handle custom user creation.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular Resident user with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Resident(AbstractBaseUser, PermissionsMixin):
    """
    Model representing a resident.
    """

    name = models.CharField(max_length=100)
    # A field to store the name of the resident

    email = models.EmailField(unique=True)
    # foreign unique email address for residents

    password = models.CharField(max_length=128, default='temporarypassword')  # Placeholder password

    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, null=True, blank=True)
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

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='resident_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='resident',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='resident_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='resident',
    )

    objects = ResidentManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name', 'phone_number', 'date_moved_in', 
        'rent_due_date', 'estate_name'
    ]


    def __str__(self):
        """
        String representation of the Resident object.
        """
        return self.email
        # Returns the email of the resident when the object is printed or displayed

    class Meta:
        permissions = (
            ("can_view_dashboard", "Can view dashboard"),
        )