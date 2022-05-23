from django import forms
import re


def validate_email(email):
    if re.match(r'^[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$', email):
        return True
    return False


def validate_phone(number):
    k = 0
    if re.match(r'^09\d{9}$' , number):
        k = 1
    if re.match(r'^\+98\d{10}$' , number):
        k = 1
    if re.match(r'^0098\d{10}$' , number) :
        k = 1

    if k == 1:
        return True
    return False
