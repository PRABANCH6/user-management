from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

    
class Contact_Us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class user_register(models.Model):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=100,)
    confirm_password = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    is_staff = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.username
    
class AddUser(models.Model):
    username = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    fullname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'User_adduser'

class UserRegister(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'User_register'
    
class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



    class Meta:
        db_table = 'User_login'