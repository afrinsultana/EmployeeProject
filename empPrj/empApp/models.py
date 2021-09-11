from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):    
    id=models.AutoField(primary_key=True)
    name=models.CharField('Depatment Name',max_length=100)
   
    def __str__(self) -> str:
        return f'{self.id} {self.name}'


class Employee(models.Model):    
    id=models.AutoField(primary_key=True)
    name=models.CharField('Employee Name ',max_length=100)
    email=models.EmailField('E-mail Address ',unique=True,blank=True)
    dob=models.DateField('Birth Date ',default=timezone.now,blank=True,help_text='Format: yyyy-mm-dd')
    salary=models.DecimalField('Monthly Salary ',max_digits=8,decimal_places=2,blank=True,null=True)
    photo=models.FileField(upload_to='myimage',default='myimage/blank.png',blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} {self.name}'
