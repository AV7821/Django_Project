from django import forms
from django.core import validators
from.models import User
from django.contrib.auth.forms import  AuthenticationForm, UsernameField


class StudentRegistation(forms.ModelForm):

    class Meta :
        model =User 

        fields=['first_name','last_name','username', 'email','password','profile_picture','confirm_password','category']
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}
            ),
            # 'profile_picture': forms.ImageField(upload_to="profile_images", blank=True),
            'confirm_password': forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'})
        }
        def clean(self):
            cleaned_data = super(StudentRegistation, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
             raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class MyLoginForm(AuthenticationForm):
     username = UsernameField(widget=forms.TextInput(
         attrs={'autofocus': True, 'class': 'form-control'}))
     password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


