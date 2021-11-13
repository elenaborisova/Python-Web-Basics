from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from app.forms.profiles import ProfileForm
from app.models import Profile, Expense


def profile_index(request):
    profile = Profile.objects.all()[0]
    expenses = Expense.objects.all()
    expenses_cost = sum(expense.price for expense in expenses)
    context = {
        'profile': profile,
        'budget_left': profile.budget - expenses_cost,
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
    pass


def delete_profile(request):
    pass
