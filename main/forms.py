from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class UserRegistrationForm(forms.ModelForm):
    '''
    Form for user registration. Includes fields for email, password, and password confirmation.
    '''
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_email(self):
        '''
        Validate that the email is not already in use.
        '''
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

    def clean(self):
        '''
        Ensure that the password and confirm_password fields match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise ValidationError("Passwords doesn't match")
        
        return cleaned_data
    
    def save(self, commit=True):
        '''
        Save the user, setting the username to the email and hashing the password.
        '''
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    '''
    Custom login form that uses email as the username field.
    '''
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        '''
        Authenticate the user and raise an error if authentication fails.
        '''
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError('Invalid email or password.')
        return super().clean()