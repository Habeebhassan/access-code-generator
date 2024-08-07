from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from django.contrib.auth.hashers import make_password

class SecurityPersonnelManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class SecurityPersonnel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, default='user@myemail.com')
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    passport_photo = models.ImageField(upload_to='passports/')
    nin_number = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=15)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='security_personnel_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='security_personnel',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='security_personnel_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='security_personnel',
    )

    objects = SecurityPersonnelManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    class Meta:
        permissions = (
            ("can_view_dashboard", "Can view dashboard"),
        )

# class SecurityPersonnel(models.Model):
#     """
#     Model representing a security personnel.
#     """

#     name = models.CharField(max_length=100)
#     # A field to store the name of the security personnel

#     email = models.EmailField(unique=True, max_length=50, default='my@myemail.com')
#     #A field that stores security personnel's email

#     company_name = models.CharField(max_length=100)
#     # A field to store the name of the company the security personnel belongs to

#     passport_photo = models.ImageField(upload_to='passports/')
#     # An image field to store the security personnel's passport photo, uploaded to 'passports/' directory

#     nin_number = models.CharField(max_length=11)
#     # A field to store the National Identification Number (NIN) of the security personnel

#     phone_number = models.CharField(max_length=15)
#     # A field to store the phone number of the security personnel

#     password = models.CharField(max_length=128)
#     # a field that stores the password of the security personnel

#     def __str__(self):
#         """
#         String representation of the SecurityPersonnel object.
#         Returns the name of the security personnel when the object is printed or displayed.
#         """
#         return self.name
#         # Returns the name of the security personnel when the object is printed or displayed

#     def set_password(self, raw_password):
#         """
#         Sets the password for the security personnel by hashing the raw password.
#         """
#         self.password = make_password(raw_password)