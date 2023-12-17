from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import ProdCategory


def index_view(request):
    prod_categories = ProdCategory.objects.all()
    context = {"prod_categories": prod_categories}
    return render(request, 'index.html', context)

# Create your views here.
