from django.shortcuts import render, redirect

from app.common.budget import calculate_budget_left
from app.common.profile import get_profile
from app.forms.profiles import ProfileForm


def profile_index(request):
    profile = get_profile()
    expenses = profile.expense_set.all()
    profile.budget_left = calculate_budget_left(expenses, profile)
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm,
        }
        return render(request, 'home-no-profile.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        context = {
            'form': form
        }
        return render(request, 'profile-edit.html', context)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile index')

        context = {
            'form': form,
        }
        return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile),
        }
        return render(request, 'profile-delete.html', context)
    else:
        profile.delete()
        return redirect('index')
