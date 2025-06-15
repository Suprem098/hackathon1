from django.db import models
from django.contrib.auth.models import User

class Semester(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.semester.name})"

class Notice(models.Model):
    NOTICE_TYPES = [
        ('program', 'Upcoming Program'),
        ('result', 'Result'),
        ('exam', 'Exam Date'),
        ('holiday', 'Holiday'),
        ('schedule', 'Class Schedule'),
    ]
    title = models.CharField(max_length=200)
    notice_type = models.CharField(max_length=20, choices=NOTICE_TYPES)
    description = models.TextField(blank=True)
    date = models.DateField()
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.date}"

# Extend User model if needed, or use default User model for login info
