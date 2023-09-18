from django import forms
from models import User
from django.core.validators import EmailValidator, RegexValidator

    
class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email']
        first_name = forms.CharField(max_length=100)
        last_name = forms.CharField(max_length=100)
        phone_number = forms.CharField(validators=[RegexValidator(regex='^\d{15}$')])
        email = forms.EmailField(validators=[EmailValidator])

        def clean_email(self):
            email = self.cleaned_data['email']
            if not email.endswith('@gmail.com'):
                raise forms.ValidationError('Please enter a valid email address.')
                
        def clean_phone_number(self):
            phone_number = self.cleaned_data['phone_number']
            if not phone_number.startwith(+254):
                raise forms.ValidationError('Please enter avalid phone number.')
