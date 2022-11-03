from django import forms
from django.forms import ModelForm
from app.models import Sudo, Mofonaina, Sampana


class Auth(forms.Form):
    tel = forms.IntegerField(widget=forms.NumberInput(attrs={
        'style': 'width:100%;height:75px;margin-top:15px;text-align:center',
        'placeholder': 'Finday'
    }))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'style': 'width:100%;height:75px;text-align:center',
        'placeholder': 'Teny Miafina'
    }))


class Register(ModelForm):
    class Meta:
        model = Sudo
        fields = ['name', 'tel', 'password']


class SampanaForm(ModelForm):
    class Meta:
        model = Sampana
        fields = ['name', 'picture']


class MofonainaForm(ModelForm):
    class Meta:
        model = Mofonaina
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'style': 'border:none; border-bottom: 2px solid black;background:none;color:white;text-align:center;width:75%',
                'placeholder': 'Lohateny'
            }),
            'content': forms.Textarea(
                attrs={
                    'style': 'width:75%; padding:1%'
                }
            ),
        }
