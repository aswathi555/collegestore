from django.db import models

# Create your models here.
class department(models.Model):
    dept=models.CharField(max_length=200)

    def __str__(self):
        return self.dept

class courses(models.Model):
    dept=models.ForeignKey(department,on_delete=models.CASCADE)
    course=models.CharField(max_length=200)

    def __str__(self):
        return self.course

class student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    phone=models.CharField(max_length=15)
    address=models.TextField(max_length=250)
    email=models.EmailField(max_length=250)
    dept = models.ForeignKey(department, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(courses, on_delete=models.SET_NULL, null=True)
    purpose = models.CharField(max_length=20)


