from django import forms

class EmailForm(forms.form):
    email=forms.EmailField(max_length=100)
    subject=forms.CharField(max_length=100)
    message=forms.CharField(max_length=200)
    attach=forms.FileField(required=False)
    
