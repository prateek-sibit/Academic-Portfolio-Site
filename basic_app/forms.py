from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),required=True)
    contact_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),required=True)
    message = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Name'}))
