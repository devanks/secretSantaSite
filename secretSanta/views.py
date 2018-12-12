# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

from django.contrib import messages


from .forms import CustomUserCreationForm

from random import shuffle

import copy

from .models import CustomUser

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def super_shuffle(lst):
    new_lst = copy.copy(lst)
    shuffle(new_lst)
    for old, new in zip(lst, new_lst):
        if old == new:
            return super_shuffle(lst)

    return new_lst

def pickSecretSanta(request):
    if request.user.is_superuser:
        setSantaList = CustomUser.objects.all()
        randomList = list(CustomUser.objects.all())
        countOfSanta = CustomUser.objects.all().count()
        if countOfSanta > 2:
            randomList = super_shuffle(randomList)
            for santa, randomSanta in zip(setSantaList, randomList):
                santa.secret_santa_of = randomSanta.first_name + ' ' + randomSanta.last_name
                santa.save()
            messages.error(request, 'The Santas have been assigned.')
        else:
            messages.error(request, 'The number of Santas need to be more than 2.')
    else:
        messages.error(request, 'Please ping the admin to do the "Secret Santa" assignment. Ho Ho Ho!')
    response = redirect('home')
    return response
