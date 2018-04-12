# _*_ coding: utf-8 _*_
__author__ = 'xiaoke'
__date__ = '2018/4/12 14:22'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)