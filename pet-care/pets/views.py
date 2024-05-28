from django.shortcuts import render, redirect, get_object_or_404
from .forms import PetsForm
from .models import Pets

def pets(request):
    pets = Pets.objects.all() 
    return render(request, 'pets/pets.html', {'pets': pets})


def add_pets(request):
    if request.method == 'POST':
        form = PetsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = PetsForm()
    return render(request, 'website/account.html', {'form': form})




def delete_pet(request, pk):
    pet = get_object_or_404(Pets, pk=pk)
    pet.delete()
    return redirect('pets')