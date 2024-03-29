from django.shortcuts import render, redirect

from pets.forms.comment_form import CommentForm
from pets.forms.pet_form import PetForm
from pets.models import Pet, Like, Comment


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),
    }

    return render(request, 'pet_list.html', context)


def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
        }

        return render(request, 'pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.save()
            return redirect('pet details or comment', pk)

        context = {
            'pet': pet,
            'form': form,
        }

        return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like()
    like.pet = pet
    like.save()

    return redirect('pet details or comment', pk)


def persist_pet(request, pet, template_name):
    if request.method == 'GET':
        form = PetForm(instance=pet)
        context = {
            'pet': pet,
            'form': form,
        }

        return render(request, template_name, context)
    else:
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details or comment', pet.pk)

        context = {
            'pet': pet,
            'form': form,
        }

        return render(request, template_name, context)


def create_pet(request):
    pet = Pet()
    return persist_pet(request, pet, 'pet_create.html')


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    return persist_pet(request, pet, 'pet_edit.html')


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
        }

        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')
