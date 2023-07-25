from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q

from .models import Category, Product


def all_products(request):
    """A view to show all products, including sorting and
    search queries"""
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            # get the category name from the request.GET
            categories = request.GET['category'].split(',')
            # filter the products by the category name
            products = products.filter(category__name__in=categories)
            # get the category object from the database
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            # get the search query from the request.GET
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("products"))

            # look for the query in the name or description fields
            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product detail"""

    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)
