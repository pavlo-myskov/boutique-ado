from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone


# _____Overide UserManager and Base User Model_____


class UserManager(BaseUserManager):
    def _create_user(
        self, email, name, password, is_staff, is_superuser, **extra_fields
    ):
        """Create and save a User with the given email, name and password."""
        if not email:
            raise ValueError("User must have an email address")
        if not name.strip():
            raise ValueError("User must have a name")
        now = timezone.now()
        # normalize email address (lowercase)
        email = self.normalize_email(email)
        # create user model
        user = self.model(
            email=email,
            name=name,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        # set password
        user.set_password(password)
        # save user model
        user.save(using=self._db)
        return user

    def create_user(self, email, name, password, **extra_fields):
        """Create and save a regular User with the given email,
        name and password."""
        return self._create_user(
            email, password, name, False, False, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        return self._create_user(
            email, "admin", password, True, True, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Serve email field as a unique identifier instead of username
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        """Return string representation of our user"""
        return self.email
