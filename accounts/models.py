from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.name = name
        user.save(using=self._db)
        return user

    def create_user(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,name, password, **extra_fields)

    def create_superuser(self, email,name, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        return self._create_user(email,name, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        error_messages = {'unique': 'A user with this email address already exists'}
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]
    name = models.CharField(verbose_name='Name',max_length = 40)
    year = models.CharField(verbose_name='Name',max_length = 40,default='1')
    phone_no=  models.CharField(verbose_name='Number',max_length = 10)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    def get_username(self):
        return self.email
    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def get_name(self):
        return self.name

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
