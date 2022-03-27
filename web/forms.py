from django.forms import ModelForm
from .models import *

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields =['name','college','department','email','number']