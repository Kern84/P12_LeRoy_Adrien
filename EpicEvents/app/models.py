from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique indentifiers for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """Create and save a user with the given email and password."""

        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Class for the user information."""

    class User_Role(models.TextChoices):
        """Class where user role is chosen."""

        SALES = "Sales"
        SUPPORT = "Support"
        MANAGEMENT = "Management"

    username = None
    date_joined = None
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    role = models.CharField(
        max_length=50,
        choices=User_Role.choices,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"


class Client(models.Model):
    """Class for the creation of a client."""

    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, blank=True, unique=True)
    mobile = models.CharField(max_length=20, blank=True, unique=True)
    compagny_name = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sale_contact = models.ForeignKey(
        blank=True,
        null=True,
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        limit_choices_to={"role": "Sales"},
    )
    actual_client = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()} - {self.compagny_name.capitalize()}"


class Contract(models.Model):
    """Class for the creation of a contract."""

    sale_contact = models.ForeignKey(
        blank=True,
        null=True,
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        limit_choices_to={"role": "Sales"},
    )
    client = models.ForeignKey(
        "app.Client", blank=True, null=True, on_delete=models.PROTECT
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField(blank=True)
    payment_due = models.DateField(blank=True)


class Event(models.Model):
    """Class for the creation of an event after signing a contract."""

    client = models.ForeignKey(
        "app.Client", blank=True, null=True, on_delete=models.PROTECT
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        blank=True,
        null=True,
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        limit_choices_to={"role": "Support"},
    )
    event_status = models.ForeignKey(
        "app.Event_Status", blank=True, null=True, on_delete=models.PROTECT
    )
    attendees = models.IntegerField(
        blank=True,
    )
    event_date = models.DateField(blank=True)
    notes = models.TextField(blank=True, max_length=1000)


class Event_Status(models.Model):
    """Class where the event status is chosen."""

    STATUS = [
        ("NOT STARTED", "Not Started"),
        ("IN PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
    ]

    status = models.CharField(max_length=50, choices=STATUS, default="NOT STARTED")

    class Meta:
        verbose_name = "Event Status"
        verbose_name_plural = verbose_name
