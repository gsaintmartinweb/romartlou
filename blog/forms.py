from django import forms


class contactformemail(forms.Form):
    Email = forms.EmailField(required=True)
    Objet = forms.CharField(required=True)
    Message = forms.CharField(widget=forms.Textarea, required=True)
