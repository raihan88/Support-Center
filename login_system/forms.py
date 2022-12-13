from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from login_system.models import User
from django import forms

user_role = [
    ('1', 'Admin'),
    ('2', 'Member'),
    ('3', 'Expert'),
    ]

class SignupForm(UserCreationForm):
    role = forms.CharField(label='Select a Role', widget=forms.Select(choices=user_role, attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','role')
    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'


    
