from django.forms import ModelForm, EmailInput

from app.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
