from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
from django.utils.timezone import now


class Status(models.Model):
    STATUS_CHOICE = [('request', 'Request'), ('pending', 'Pending'), ('aproved', 'Aproved'), ('reject', 'Reject')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(default='request',
        max_length=10, choices=STATUS_CHOICE,
        blank=True, null=True)

    def __str__(self):
        return self.user.username
class Employee(models.Model):

    GENDER_CHOICE=(('male','Male'),('female','Female'))
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=300)
    fname=models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,default='abc@gmail.com')

    dob=models.DateField()

    gender=models.CharField(max_length=100,choices=GENDER_CHOICE,default='Male')
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    def __str__(self):
        return self.fname

class Profiles(models.Model):
    GENDER_CHOICE = (('male', 'Male'), ('female', 'Female'))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',primary_key=True)
    #photo = models.FileField(upload_to='images/',default='images/def.jpg')
    #DOB = models.DateField(default=datetime.datetime.today())
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE,null=True)
    city = models.CharField(max_length=100,null=True)
    #father_name = models.CharField(max_length=200,blank=True, null=True)
    #mother_name = models.CharField(max_length=200,blank=True, null=True)
    #designation = models.CharField(max_length=200,blank=True, null=True)
    #department = models.CharField(max_length=200,blank=True, null=True)


    def __str__(self):
        return self.user.username
class Hospit(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    book_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    bg = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=100,)
    date=models.DateTimeField(default=now)
    problem = models.TextField(max_length=1000)
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return self.name
class Canteen_Product(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pro_id=models.AutoField
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    image = models.FileField(upload_to='images' ,default="")
    date=models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."


class Hospi(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICE = (('male', 'Male'), ('female', 'Female'))

    email=models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    bg = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)
    problem = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
class Salary(models.Model):
    GENDER_CHOICE = (('male', 'Male'), ('female', 'Female'))
    email=models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    bg = models.CharField(max_length=20)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)
    problem = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
class Timesheet(models.Model):
    email = models.EmailField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)
    date =models.DateField()

    def __str__(self):
        return self.email

class Leave(models.Model):

    STATUS_CHOICE = [('request', 'Request'),('pending', 'Pending'),('aproved', 'Aproved'), ('reject', 'Reject')]
    email = models.EmailField(max_length=200)
    leave_description = models.CharField(max_length=400)
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.CharField(default='request',max_length=100, choices=STATUS_CHOICE,blank=True,null=True)

    def __str__(self):
        return self.email


class AboutUs(models.Model):
    text = models.TextField(max_length=1000)