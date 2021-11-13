from django.shortcuts import render

from app.common.budget import calculate_budget_left
from app.models import Profile
from app.views.profiles import create_profile


def index(request):
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        expenses = profile.expense_set.all()
        profile.budget_left = calculate_budget_left(expenses, profile)
        context = {
            'profile': profile,
            'expenses': expenses,
        }

        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)
