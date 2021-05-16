from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):

    def create_superuser(self, email, first_name, last_name, phone, password):
        user = User.objects.create(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            is_superuser=True,
            is_staff=True
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(null=True, unique=False, max_length=150)
    customer_id = models.IntegerField(null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True, blank=True)
    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
    USERNAME_FIELD = 'email'
    groups = None
    user_permissions = None

    class Meta:
        ordering = ['id']
