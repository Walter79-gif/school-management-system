from django.conf import settings
from django.db import models


class Student(models.Model):
    class Gender(models.TextChoices):
        MALE= "M", "Male"
        FEMALE= "F", "Female"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    admission_number = models.CharField(
        max_length=20,
        unique=True
    )

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices
    )

    date_of_birth = models.DateField()

    admission_date = models.DateField()

    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.admission_number} - {self.user.get_full_name()}"
