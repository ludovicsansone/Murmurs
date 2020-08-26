import json
from django.shortcuts import render, redirect
from .models import Univers
from django.contrib.auth.models import User
from . import services
from django import forms
from .forms import UniversHomeForm, UniversBook
from django.urls import reverse
from django.core import serializers

def home(request, user_id):
    user = User.objects.get(id = user_id)

    try:
        univers = Univers.objects.get(utilisateur = user)


    except:
        univers = Univers.objects.create(pseudo = user.username, utilisateur = user)
    if univers.dateDeNaissance:
        age = services.getAge(univers.dateDeNaissance)
    
    if univers.informations == 0:
        empty_univers = True
    else:
        empty_univers = False
    univers_json = serializers.serialize("json", Univers.objects.filter(id = user_id))

    return render(request, 'univers_home.html', locals())

def homeForm(request, user_id, verbe):
    error = False
    user = User.objects.get(id = user_id)
    univers = Univers.objects.get(utilisateur = user)

    if request.POST:
        form = UniversHomeForm(request.POST)
        if form.is_valid():
            univers.pseudo = form.cleaned_data['pseudo']
            univers.sexe = form.cleaned_data['sexe']
            univers.recherche = form.cleaned_data['recherche']
            univers.dateDeNaissance = form.cleaned_data['dateDeNaissance']
            univers.villeDeResidence = form.cleaned_data['villeDeResidence']
            univers.presentation = form.cleaned_data['presentation']
            univers.informations = 1
            univers.save()
            return redirect('univers_home', user_id = request.user.id)
        else:
            error = True
            
    else:
        form = UniversHomeForm(initial = {
            'pseudo': univers.pseudo,
            'dateDeNaissance': univers.dateDeNaissance,
            'sexe': univers.sexe,
            'recherche': univers.recherche,
            'villeDeResidence': univers.villeDeResidence,
            'presentation': univers.presentation
            })
    if verbe == 'create':
        buttonValue = 'Suivant'
    else:
        buttonValue = 'Modifier'

    return render(request, 'univers_home_form.html', locals())
    
def artistic_tastes(request, user_id):
    user = User.objects.get(id = user_id)
    univers = Univers.objects.get(utilisateur = user)
    empty = services.artisticTastesIsEmpty(univers)

    return render(request, 'univers_artistic_tastes.html', locals())

def appearance(request, user_id):
    user = User.objects.get(id = user_id)
    univers = Univers.objects.get(utilisateur = user)
    
    return render(request, 'univers_appearance.html', locals())

def reaction(request, user_id):
    user = User.objects.get(id = user_id)
    univers = Univers.objects.get(utilisateur = user)
    
    return render(request, 'univers_reaction.html', locals())

def book(request, user_id):
    user = User.objects.get(id = user_id)
    univers = Univers.objects.get(utilisateur = user)

    if request.POST:
        form = UniversBook(request.POST)
        if form.is_valid():
            univers.livrePrefere = form.cleaned_data['livrePrefere']
            univers.aProposDuLivre = form.cleaned_data['aProposDuLivre']
            univers.save()
            return redirect('univers_artistic_tastes', user_id = request.user.id)
    else:
        form = UniversBook(initial = {
            'livrePrefere': univers.livrePrefere,
            'aProposDuLivre': univers.aProposDuLivre
        })
    return render(request, 'univers_book.html', locals())
