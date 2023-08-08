from django.db import models
from authentication.models import CustomUser, Role, Address
from events.models import Event


class Sector(models.Model):
    """Class to define associative sectors"""
    idsector = models.IntegerField(primary_key=True)
    sectorname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.sectorname

    class Meta:
        db_table = 'sector'

class Association(models.Model):
    """Class for association information"""
    associationname = models.CharField(max_length=200, unique=True)
    acronym = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, unique=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    logo = models.ImageField(upload_to='association_logos/', null=True, blank=True)

    def __str__(self):
        return self.associationname

    def get_association_address(self):
        try:
            pass
        except:
            pass

    class Meta:
        db_table = 'association'

class association_address(models.Model):
    """Class defining association's address"""
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = 'association_address'

class UserRoleAssociation(models.Model):
    """Class used to define the user's role in the association"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_role_association'

class AssociationSector(models.Model):
    """Class defining a user's role in an association"""
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'sector_association'

class AssociationEvent(models.Model):
    """Class for linking events and associations"""
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)