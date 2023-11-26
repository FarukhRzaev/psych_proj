from django.db import models
from django.core.validators import MinLengthValidator


class Contact(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    mail = models.EmailField()
    phone_number = models.CharField(
        max_length=12, validators=[MinLengthValidator(10)], null=True, blank=True
    )
    message = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
