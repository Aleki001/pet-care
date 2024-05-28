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




# def delete_pet(request):
#     if request.method == 'POST':
#         pet_id = request.POST.get('pet_id')
#         if pet_id:
#             try:
#                 pet = get_object_or_404(Pets, pk=pet_id)
#                 pet.delete()
#                 return redirect('pets')
#             except Exception as e:
#                 print(f"Error deleting pet: {e}")
#         else:
#             print("Pet ID not provided")
#     else:
#         print("Request method is not POST")
#     return redirect('pets')

def delete_pet(request, pk):
    pet = get_object_or_404(Pets, pk=pk)
    pet.delete()
    return redirect('pets')