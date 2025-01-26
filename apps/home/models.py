from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField()

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="redactors_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="redactors_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Newspaper(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,
                              related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    def __str__(self):
        return self.title
