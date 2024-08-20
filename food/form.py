
from django import forms
 
# creating a form 
class UserForm(forms.Form):
 
    name = forms.CharField(max_length = 200, error_messages={"required": "Please enter your name"})
    
    phonenumber = forms.IntegerField(
                     max_value=9999999999, error_messages={"required": "Please enter your phonenumber"}
                     )
    
    address= forms.CharField(error_messages={"required": "Please enter your address"})