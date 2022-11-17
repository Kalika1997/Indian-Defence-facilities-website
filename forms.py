from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Leave, Employee,Profiles


class DateInput(forms.DateInput):
    input_type = 'date'


class Userprofile(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
class Upprofile(forms.ModelForm):
    class Meta:
        model=Profiles

        #fields=['photo','city','DOB','gender','father_name','mother_name','department','designation']
        fields = [ 'city',  'gender']
        widgets = {
            'DOB': DateInput(),

        }




class SignUpForm(UserCreationForm):
    STATUS_CHOICE = (('request', 'Request'), ('pending', 'Pending'), ('aproved', 'Aproved'), ('reject', 'Reject'))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    status = forms.ChoiceField( choices=STATUS_CHOICE,required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'status'

            ]
        widgets = {
            'status': forms.TextInput(attrs={'readonly': 'True'})

        }

class StatusForm(forms.Form):
    STATUS_CHOICE = (('request', 'Request'), ('pending', 'Pending'), ('aproved', 'Aproved'), ('reject', 'Reject'))
    status = forms.ChoiceField(choices=STATUS_CHOICE,disabled=True)

    # Profile Form





class LeaveForm(ModelForm):


    class Meta:
        model = Leave
        fields = ['email','leave_description','from_date','to_date','status']
        widgets = {
            'from_date': DateInput(),
            'to_date': DateInput(),
            'status' :forms.TextInput(attrs={'readonly':'True'})

        }


class MyLogin(forms.Form):
    UserName=forms.CharField(max_length=100)
    Password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        u=self.cleaned_data['UserName']
        p=self.cleaned_data['Password']
        v=authenticate(username=u,password=p)
        print(v)
        #login(v)
        if v is None:

            raise forms.ValidationError('Incorrect credentials or Your login status is not approved by admin')

class Register(forms.ModelForm):
    #STATUS_CHOICE = (('request', 'Request'), ('pending', 'Pending'), ('aproved', 'Aproved'), ('reject', 'Reject'))
    Password = forms.CharField(widget=forms.PasswordInput)
    Re_Password=forms.CharField(widget=forms.PasswordInput)
    #status = forms.ChoiceField(choices=STATUS_CHOICE, required=False)


    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets = {
            'status': forms.TextInput(attrs={'readonly': 'True'})

        }

    def clean(self):
        data=super(Register,self).clean()
        p=data['Password']
        p1=data['Re_Password']
        if p!= p1:
            raise forms.ValidationError('Both password did not match')

class Hospital(UserCreationForm):
    STATUS_CHOICE = (('male', 'Male'), ('female', 'Female'))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    gender = forms.ChoiceField( choices=STATUS_CHOICE,required=False)
    age=forms.IntegerField()
    blood_group = forms.CharField(max_length=30, required=False, help_text='Optional')
    problem = forms.Textarea( )
