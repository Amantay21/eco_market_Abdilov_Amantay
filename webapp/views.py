from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import ProdCategory, Product


def index_view(request):
    prod_categories = ProdCategory.objects.all()
    context = {"prod_categories": prod_categories}
    return render(request, 'index.html', context)


def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product,  pk=pk)
    category = get_object_or_404(ProdCategory, pk=pk)
    return render(request, 'product_view.html', {'product': product, 'category': category})

# Create your views here.
