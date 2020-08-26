from django import forms

class UniversHomeForm(forms.Form):
    pseudo = forms.CharField(label = "Votre Pseudo", max_length=30, required = True)
    sexe = forms.ChoiceField(label = "Vous êtes", choices = [('femme', 'Une Femme'), ('homme', 'Un homme'), ('couple', 'Un couple')], required = True)
    recherche = forms.ChoiceField(label = "Vous recherchez", choices = [('femme', 'Une femme'), ('homme', 'Un homme'), ('couple', 'Un couple')], required = True)
    dateDeNaissance = forms.DateField(label = "Vous êtes né le", required = True, widget = forms.DateInput)
    villeDeResidence = forms.CharField(label = "Votre ville de résidence est", max_length=50, required = True)
    presentation = forms.CharField(label = "Votre présentation", max_length = 800, required = True, widget = forms.Textarea)

class UniversBook(forms.Form):
    livrePrefere = forms.CharField(label = 'Votre livre préféré', max_length = 100, required = True)
    aProposDuLivre = forms.CharField(label = 'Dites-en quelques mots', max_length = 1000, required = True, widget = forms.Textarea)
