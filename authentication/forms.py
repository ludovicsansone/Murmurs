from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label = "Nom d'utilisateur", max_length=30, required = True)
    email = forms.EmailField(label = 'Adresse de courriel', required = True)
    password = forms.CharField(label = 'Mot de passe', widget = forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(label = "Nom d'utilisateur", max_length=30, required = True)
    password = forms.CharField(label = 'Mot de passe', widget = forms.PasswordInput)
