from datetime import timedelta

from django.db import models
from django.utils import timezone


class EngineeringContent(models.Model):
    CATEGORY_CHOICES = [
        ('did_you_know', 'Did You Know?'),
        ('breakthrough', 'Engineering Breakthrough'),
        ('inventor', 'Inventor Spotlight'),
        ('principle', 'Engineering Principle'),
        ('milestone', 'Historical Milestone'),
        ('innovation', 'Modern Innovation'),
        ('africa', 'African Engineering'),
        ('kenya', 'Kenyan Engineering'),
        ('energy', 'Energy & Sustainability'),
        ('technology', 'Technology'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='did_you_know'
    )
    published_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(days=2)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title