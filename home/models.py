# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Products(models.Model):

    #__Products_FIELDS__
    1 = models.TextField(max_length=255, null=True, blank=True)

    #__Products_FIELDS__END

    class Meta:
        verbose_name        = _("Products")
        verbose_name_plural = _("Products")


class Price(models.Model):

    #__Price_FIELDS__
    1 = models.TextField(max_length=255, null=True, blank=True)

    #__Price_FIELDS__END

    class Meta:
        verbose_name        = _("Price")
        verbose_name_plural = _("Price")


class Customer(models.Model):

    #__Customer_FIELDS__
    1 = models.CharField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Suplier(models.Model):

    #__Suplier_FIELDS__
    2 = models.CharField(max_length=255, null=True, blank=True)

    #__Suplier_FIELDS__END

    class Meta:
        verbose_name        = _("Suplier")
        verbose_name_plural = _("Suplier")



#__MODELS__END
