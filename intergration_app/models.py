from typing import Iterable
import uuid
from django.db import models
from users.models import User
import secrets
from datetime import timedelta
from django.utils import timezone      

# Create your models here.

PLAN_CHOICES = (
    ('FREE', 'FREE'),
    ('PREMIUM', 'PREMIUM'),
    ('ENTERPRISE', 'ENTERPRISE'),
)

DURATION_CHOICES = (
    ('MONTHLY', 'MONTHLY'),
    ('YEARLY', 'YEARLY'),
)   


class Plan(models.Model):
    name = models.CharField(max_length=100, choices=PLAN_CHOICES, default='FREE')
    duration = models.CharField(max_length=100, choices=DURATION_CHOICES, default='MONTHLY')
    price = models.FloatField()
    description = models.TextField()
    currency = models.CharField(max_length=100, default="TZS")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'plan'
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_payment')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plan_payment')
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    currency = models.CharField(max_length=100, default="TZS")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'payment'
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.user.username

    def is_expired(self):
        # check if the expire date is less than the current date
        return self.expire_date < timezone.now()
    


    
class UserIntergrationApp(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True) 
    api_key = models.CharField(max_length=100, unique=True)
    api_secret = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_intergration_app')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='payment_app', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


    class Meta:
        db_table = 'user_intergration_app'
        verbose_name = 'User Intergration App'
        verbose_name_plural = 'User Intergration Apps'
        

    def __str__(self):
        return self.user.username
    
    def calculate_expire_date(self):
        # based on payment, calculate the expire date and update the expire_date field 
        try: 
            payment = Payment.objects.get(app=self)
            self.expire_date = payment.expire_date      
            if self.expire_date < timezone.now():
                self.is_active = False
            else:
                self.is_active = True
        except Payment.DoesNotExist:
            self.is_active = False
            self.expire_date = None 
           


    def save(self, *args, **kwargs):
        self.calculate_expire_date()
        if not self.api_key:
            self.api_key = secrets.token_urlsafe(50)
        if not self.api_secret:
            self.api_secret = secrets.token_urlsafe(50)
        super().save(*args, **kwargs)

   
  
           
                 

    

    
       


    
   
