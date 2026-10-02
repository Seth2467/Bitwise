from django.db import models
from units.models import Unit
from cloudinary.models import CloudinaryField
# Create your models here.

class StudyResource(models.Model):
    CATEGORY_CHOICES = [
        ('lecture_notes', 'Lecture Notes'),
        ('past_paper', 'Past Examination Paper'),
        ('past_cat', 'Past CAT Test'),
        ('solution', 'Solutions and Marking Schemes'),
        ('lab_material', 'Laboratory Materials'),
        ('reference', 'Reference Materials'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name= 'resources')
    title= models.CharField( max_length=200)
    file = CloudinaryField('file', resource_type='raw', blank=True, null=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.unit.code}"
    