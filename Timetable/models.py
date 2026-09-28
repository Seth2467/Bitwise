from django.db import models


# Create your models here.
class TimetableEntry(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

    MODE_CHOICES = [
        ('Physical', 'Physical'),
        ('Online', 'Online'),
    ]

    day = models.CharField(max_length = 10, choices = DAY_CHOICES)
    unit_code = models.CharField(max_length = 20, blank = True)
    unit = models.CharField( max_length=50)
    lecturer = models.CharField( max_length=50)
    mode = models.CharField(max_length=10, choices = MODE_CHOICES, default= 'Physical')
    bounced = models.BooleanField(default=False)
    room = models.CharField( max_length=10, blank = True)
    online_link = models.URLField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f" {self.unit_code} - {self.unit}"
    