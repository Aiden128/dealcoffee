__author__ = 'klein'

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField

class MbeanForm(forms.Form):
    m_b_name = forms.CharField(max_length=20)
    m_b_unitprice = forms.FloatField()
    m_b_weight = forms.IntegerField()
    m_b_minimum = forms.IntegerField()
    m_b_e_date = forms.DateField()
    m_b_d_date = forms.DateField()
    m_b_shipping_fee = forms.FloatField()
    m_p_phone = forms.CharField(max_length=20)
    m_b_remark = forms.CharField(required=False, widget=forms.Textarea())

class OrderForm(forms.Form):
    o_b_set = forms.IntegerField()
    o_b_remark = forms.CharField(required=False, widget=forms.Textarea())
    o_p_phone = forms.CharField(max_length=20)
    o_p_address = forms.CharField(max_length=100)


class UserCreateForm(UserCreationForm): #register form, call by views.py:register
    email = forms.EmailField(required=True)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()