from django.shortcuts import render
from .models import Product, Rubric


def index(request):
    prods = Product.objects.all()
    rubs = Rubric.objects.all()
    context = {'prods': prods, "rubs": rubs}

    return render(request, 'index.html', context)


def by_rubric(request, rubric_id):
    rub = Rubric.objects.get(pk=rubric_id)
    prods = Product.objects.filter(rubric=rub)
    rubs = Rubric.objects.all()
    context = {"rub": rub, "prods": prods, "rubs": rubs}

    return render(request, 'rubric.html', context)
