from django.shortcuts import render, redirect, get_object_or_404
from .forms import PetsForm, AdoptionRequestForm
from .models import Pets
from django.contrib import messages

def pets(request):
    pets = Pets.objects.all() 
    return render(request, 'pets/pets.html', {'pets': pets})


def add_pets(request):
    if request.method == 'POST':
        form = PetsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet added to gallery successfully.')
            return redirect('account')
    else:
        form = PetsForm()
    return render(request, 'website/account.html', {'form': form})


def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pets, id=pet_id)

    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.pet = pet
            adoption_request.user = request.user
            adoption_request.save()
            messages.success(request, 'Thanks for your application. Kindly wait for our feedback. We will be happy to reach out')
            return redirect('pets')
    else:
        form = AdoptionRequestForm(initial={'pet': pet})

    return render(request, 'pets/pet_adoption.html', {'form': form, 'pet': pet})

def delete_pet(request, pk):
    pet = get_object_or_404(Pets, pk=pk)
    pet.delete()
    return redirect('pets')