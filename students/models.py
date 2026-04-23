from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key = True)
    full_name = models.CharField(max_length=100)
    
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    course = models.CharField(max_length=50)
    year = models.IntegerField()
    gpa = models.FloatField()

    def __str__(self):
        return self.full_name
