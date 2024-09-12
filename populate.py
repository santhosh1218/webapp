import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dbproject.settings')
import django
django.setup()
from dbapp.models import Employee
from faker import Faker
import random
fake=Faker()
dept=['HR','Developer','Accounting','Testing','Management']
def populate():
    fake_name=fake.name()
    fake_sal=fake.random.randrange(100000,500000)
    fake_address=fake.address()
    fake_dept=random.choice(dept)
    emp_record=Employee.objects.get_or_create(emp_name=fake_name,emp_salory=fake_sal,emp_address=fake_address,emp_dept=fake_dept)
    return emp_record
def creating(N):
    for n in range(1,N):
        populate()
print('generating....')
creating(30)
print('completed!')