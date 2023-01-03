from django.db import models

# Create your models here.
class Employe(models.Model):
    id=models.AutoField(primary_key=True)
    Empid=models.IntegerField()
    Name=models.CharField(max_length=55)
    Email=models.EmailField(max_length=55)
    Password=models.CharField(max_length=55)
    Designation=models.CharField(max_length=44,choices=(('android developer','Android Developer'),
                                                        ('backend developer)','Backend Developer')))

