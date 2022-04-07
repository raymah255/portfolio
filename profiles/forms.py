from .models import Profile
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()



class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False, max_length=255)
    last_name = forms.CharField(required=False, max_length=255)
    email_address = forms.CharField(required=False, max_length=255)

    class Meta:
        model = Profile
        fields = ["profile_img", "first_name", "last_name", "email_address", "location"]
    
    def get_is_profile_pic(self, obj):
        return obj.is_profile_pic()
