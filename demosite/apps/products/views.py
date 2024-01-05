from django.shortcuts import render
from .models import Item
from django.db.models import Sum

# Create your views here.

def dashboard(request):
    user = request.user
    items = Item.objects.filter(user=user)
    context = {
        "items" : items
    }
    return render(request, "products/dashboard.html", context)


def summary(request):
    user = request.user
    sum = Item.objects.filter(user=user).aggregate(Sum('price'))

    if sum["price__sum"]:
        total_cost = sum["price__sum"]
    else:
        total_cost = 0

    context = {
        "total_cost" : total_cost
    }
    return render(request, "products/summary.html", context)