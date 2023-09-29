from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from authentication.models import CustomUser, Address


class Sector(models.Model):
    """Class to define associative sectors"""
    sectorname = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    
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
    logo = models.ImageField(upload_to='img/', default='img/test_sans_image.png')
    siret_number = models.BigIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99999999999999),
        ]
    )
    
    def __str__(self):
        return self.associationname
    
    def get_sector(self):
        return AssociationSector.objects.get(association=self).sector
    
    def get_address(self):
        return AssociationAddress.objects.get(association=self).address

    class Meta:
        db_table = 'association'

class AssociationAddress(models.Model):
    """Class defining association's address"""
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = 'association_address'
        unique_together =('association', 'address')

class AssociationSector(models.Model):
    """Class defining a user's role in an association"""
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'sector_association'
        unique_together =('association', 'sector')

class Role(models.Model):
    """Class defining all possible user roles"""
    rolename = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=450, null=True, blank=True)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.rolename

class UserRoleAssociation(models.Model):
    """Class used to define the user's role in the association"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_role_association'
        unique_together = ('user', 'association')

    def __str__(self):
        return f"{self.user} est {self.role} dans {self.association}"