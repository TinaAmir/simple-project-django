from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    email = forms.CharField(label='Your Email', max_length=100,widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))
    subject = forms.CharField(label='subject', max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    message = forms.CharField(label='message', max_length=100,widget=forms.Textarea(attrs={
        'class':'form-control'
    }))
    