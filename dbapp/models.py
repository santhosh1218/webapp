from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_salory=models.FloatField()
    emp_address=models.TextField()
    emp_dept=models.CharField(max_length=100)

    def __str__(self):
        return self.emp_name
        
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profile_pics/sachin.jpg',upload_to='profile_pics',blank=True)

    def __str__(self):
        return f'{self.user.username} profile'