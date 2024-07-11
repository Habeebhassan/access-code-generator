from django.db import models


from django.db import models
from residents.models import Resident

class AccessCode(models.Model):
    """
    Model to store access codes for residents.
    """

    code = models.CharField(max_length=6, unique=True)
    """
    The access code string, limited to 6 characters, unique for each instance.
    """

    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    """
    ForeignKey relationship with the Resident model. Each AccessCode is associated
    with a single Resident. When a Resident is deleted, all associated AccessCodes
    are also deleted (CASCADE behavior).
    """

    created_at = models.DateTimeField(auto_now_add=True)
    """
    DateTimeField automatically set to the current date and time when the
    AccessCode instance is created.
    """

    expires_at = models.DateTimeField()
    """
    DateTimeField specifying when the access code expires.
    """

    used_entrances = models.IntegerField(default=0)
    """
    IntegerField to track the number of times the access code has been used for entrances.
    """

    used_exits = models.IntegerField(default=0)
    """
    IntegerField to track the number of times the access code has been used for exits.
    """

    def __str__(self):
        """
        String representation of the AccessCode instance. It returns the code itself,
        which is useful for displaying in the Django admin interface and other contexts.
        """
        return self.code
