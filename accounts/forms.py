from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile

class createNewUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class updateProfile(ModelForm):
    class Meta:
        model=UserProfile
        fields=['adresse','sexe','phone','city','country','image']
class updateUserProfile(ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']