from django import forms
from accounts.models import Profile


class RegisterForm(forms.Form):
    error_messages = {
        'password_mismatch':"passwords are not the same"
    }
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
    email = forms.EmailField()

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    

class ProfileForm(forms.ModelForm):
    
    user = forms.CharField()
    age = forms.CharField()
    gender = forms.CharField()
    bio = forms.CharField()
    
    class Meta:
        model = Profile
        fields = '__all__'

    
        