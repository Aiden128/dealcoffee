# -*-coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Mbean (models.Model):

    m_b_name = models.CharField(max_length=50)
    m_b_unitprice = models.DecimalField(max_digits=8, decimal_places=1)
    m_b_weight = models.DecimalField(max_digits=8, decimal_places=1)
    m_b_minimum = models.DecimalField(max_digits=8, decimal_places=1)
    m_b_e_date = models.DateTimeField() # end day
    m_b_d_date = models.DateTimeField() # delivery day
    m_b_c_date = models.DateTimeField(auto_now_add=True) # create day
    m_b_deleted = models.BooleanField(default=False)
    m_b_shipping_fee = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    m_b_remark = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey(User)
    m_p_phone = models.CharField(max_length=10)

    def calculate_orders(self):
        return Orders.objects.filter(o_m_b=self, o_b_deleted=False).count()

    orders = property(calculate_orders)

    def __unicode__(self):
        return self.m_b_name

class Orders (models.Model):

    o_m_b = models.ForeignKey(Mbean)
    user = models.ForeignKey(User)

    o_b_set = models.DecimalField(max_digits=5, decimal_places=1)
    o_b_remark = models.CharField(max_length=300, blank=True)
    o_p_phone = models.CharField(max_length=10)
    o_p_address = models.CharField(max_length=100)
    o_b_c_date = models.DateTimeField(auto_now_add=True)
    o_b_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.o_m_b.m_b_name

class Score (models.Model):

    s_user = models.ForeignKey(User)
    s_success = models.DecimalField(max_digits=8, decimal_places=1)
    s_fail = models.DecimalField(max_digits=8, decimal_places=1)
    s_comment = models.CharField(max_length=300, blank=True)