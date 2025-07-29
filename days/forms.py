from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class Contactform(forms.Form):
    name=forms.CharField(label=' ',max_length=30,required="True",widget=forms.TextInput(attrs={'class':'form-contol my-2 b-3','placeholder':'enter your name'}))
    email=forms.EmailField(label=' ',max_length=40,required="True",widget=forms.EmailInput(attrs={'class':'form-contol my-2 b-3','placeholder':'enter your email'}))
    message=forms.CharField(label=' ',max_length=400,required="True",widget=forms.Textarea(attrs={'class':'form-contol my-1 b-3','placeholder':'enter your query'}))

    def clean(self):
        if self.errors:
            return self.cleaned_data
        
        cleaned_data=super().clean()

        valid_name=cleaned_data['name']

        if len(valid_name) <3:
            raise forms.ValidationError("min 3 char required")

class studentform(forms.ModelForm):
     name=forms.CharField(label=' ',max_length=30,required="True",widget=forms.TextInput(attrs={'class':'form-contol my-2 b-3','placeholder':'enter your name'}))
     age=forms.IntegerField(label='',widget=(forms.NumberInput(attrs={'class':'form-comtrol','placeholder':'age'})))

    
     class Meta:
         model = Student
         fields = '__all__'

    
  
#DASHBOARD

        










































































