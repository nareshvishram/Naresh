from django import forms
from .models import *

class AddUser_Form(forms.ModelForm):
    class Meta:
        model=UserDataBase
        exclude=("usr",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", }),
            "email": forms.EmailInput(attrs={"class": "form-control", }),
            "number": forms.NumberInput(attrs={"class": "form-control", }),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
            "about": forms.Textarea(attrs={"class": "form-control", "rows": "5"}),
            "email": forms.EmailInput(attrs={"class": "form-control", }),
            "number": forms.NumberInput(attrs={"class": "form-control", }),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
            "about": forms.Textarea(attrs={"class": "form-control", "rows": "5"}),
            "dob": forms.DateInput(attrs={"class": "form-control", }),
            "location": forms.TextInput(attrs={"class": "form-control", }),
            "degree": forms.TextInput(attrs={"class": "form-control", }),
            "website": forms.TextInput(attrs={"class": "form-control", }),
            "experience": forms.TextInput(attrs={"class": "form-control", }),
            "company": forms.TextInput(attrs={"class": "form-control", }),
            "profile_title": forms.TextInput(attrs={"class": "form-control", }),
            "tweeter": forms.URLInput(attrs={"class": "form-control", }),
            "linkedin": forms.URLInput(attrs={"class": "form-control", }),
            "facebook": forms.URLInput(attrs={"class": "form-control", }),
            "instagram": forms.URLInput(attrs={"class": "form-control", }),

        }



class Education_Form(forms.ModelForm):
    class Meta:
        model=Education
        exclude=("usr",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", }),
            "admission_date": forms.DateInput(attrs={"class": "form-control", }),
            "graduate_date": forms.DateInput(attrs={"class": "form-control", }),
            "result": forms.TextInput(attrs={"class": "form-control", }),
            "count_edu": forms.NumberInput(attrs={"class": "form-control", }),
            "about": forms.Textarea(attrs={"class": "form-control", "rows": "5"}),

        }