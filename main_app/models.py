from django.db import models

# Create your models here.
class Department(models.Model):
    Depart_name = models.CharField(max_length=100, null=False)
    Depart_location = models.CharField(max_length=100)

    def __str__(self):
        return self.Depart_name

class Role(models.Model):
    Role_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.Role_name

class Employee(models.Model):
    Emp_first_name = models.CharField(max_length=100, null=False)
    Emp_last_name = models.CharField(max_length=100)
    Emp_Depart = models.ForeignKey(Department, on_delete=models.CASCADE)
    Emp_Salary = models.IntegerField(default=0)
    Emp_bonus = models.IntegerField(default=0)
    Emp_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Emp_phone = models.IntegerField(default=0)
    Emp_hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.Emp_first_name, self.Emp_last_name, self.Emp_phone)