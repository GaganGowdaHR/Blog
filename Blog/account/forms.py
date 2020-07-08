from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from account.models import User, Profile
from django import forms
class SignUpform(UserCreationForm):

    # email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ('username','password1','password2','email','first_name','last_name') 

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','image']


