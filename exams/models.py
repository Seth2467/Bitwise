from django.db import models
from units.models import Unit

# Create your models here.
class Exam(models.Model):

    EXAM_TYPE_CHOICES = [
        ('CAT', 'CAT'),
        ('Main', 'Main'),
    ]

    MODE_CHOICES = [
        ('Physical', 'Physical'),
        ('Online', 'Online'),
        ('Take-away', 'Take-away'), 
    ]

    unit = models.ForeignKey( Unit, on_delete = models.CASCADE)
    exam_type = models.CharField(max_length = 10, choices = EXAM_TYPE_CHOICES)
    exam_date = models.DateField( blank = True, null = True)
    start_time = models.TimeField( blank = True, null = True)
    end_time = models.TimeField( blank = True, null = True)
    due_date = models.DateField( blank= True, null = True)
    mode = models.CharField( max_length = 10, choices = MODE_CHOICES)
    room = models.CharField(max_length = 20, blank = True)
    online_link = models.URLField( blank = True )
    notes = models.TextField( blank = True )
    is_cancelled = models.BooleanField( default = False )

    def __str__(self):
        return f"{self.unit.code} - {self.exam_type} - {self.exam_date or self.due_date}"
    