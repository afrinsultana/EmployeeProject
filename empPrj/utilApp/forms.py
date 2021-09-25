from django import forms

class EmailForm(forms.Form):
    email=forms.EmailField(max_length=100)
    subject=forms.CharField(max_length=100)
    message=forms.CharField(max_length=200,widget=forms.Textarea())
    attach=forms.FileField(required=False)
    
