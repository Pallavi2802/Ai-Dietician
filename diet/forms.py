from django import forms

class Login(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(max_length=40,widget=forms.PasswordInput)

class Signup(forms.Form):
    Name=forms.CharField(max_length=40)
    Email = forms.EmailField(max_length=60)
    Username = forms.CharField(max_length=50,widget=forms.TextInput)
    Password = forms.CharField(max_length=40,widget=forms.PasswordInput)
    Confirmpassword = forms.CharField(max_length=50,widget=forms.PasswordInput)

class bmi(forms.Form):
   height=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'type':'number'}))
   weight=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'type':'number'}))