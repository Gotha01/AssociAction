from django.contrib.auth.models import (
    AbstractBaseUser as BaseUser,
    BaseUserManager as UserManager,
    PermissionsMixin
)
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from AssociAction.settings import AUTH_USER_MODEL


class UserManager(UserManager):
    def create_user(
        self,
        first_name,
        last_name,
        username,
        email,
        password=None
    ):

        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an username')
        if self.filter(email=email).exists():
            raise ValueError('This email is already in use')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        first_name,
        last_name,
        username,
        email,
        password=None
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(BaseUser, PermissionsMixin):
    # Common Fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    user_img = models.ImageField(null=True, blank=True, default=None)
    date_of_birth = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    # Permission fields
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_address(self):
        return UserAddress.objects.get(user=self).address


class Address(models.Model):
    """General class for all addresses (users, associations, events)"""
    postalcode = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99999),
        ]
    )
    cityname = models.CharField(max_length=100)
    addresslineone = models.CharField(max_length=100)
    addresslinetwo = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'address'

    def __str__(self):
        return f"{self.addresslineone}, {self.postalcode} {self.cityname}"


class UserAddress(models.Model):
    """Class used to model the relationship between users and their address"""
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'address')

    def __str__(self):
        return f"{self.user.username}, {self.address}"
