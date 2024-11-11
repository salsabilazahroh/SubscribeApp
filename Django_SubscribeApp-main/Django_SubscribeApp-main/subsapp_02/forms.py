from django import forms
from subsapp_02.models import Customer

class NewSubscriber(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  # ['first_name', 'last_name', 'email', 'address', 'phone']
