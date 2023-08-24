from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.db.models import Q
from django.db.models.functions import Lower

from .forms import ProductForm
from .models import Category, Product


def all_products(request):
    """A view to show all products, including sorting and
    search queries"""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            # get the sort key from the request.GET
            sortkey = request.GET["sort"]
            sort = sortkey
            # annotate the products with the lower name if sorting by name
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
                if sortkey == "category":
                    sortkey = "category__name"
            if "direction" in request.GET:
                # get the direction from the request.GET
                direction = request.GET["direction"]
                if direction == "desc":
                    # reverse the order of the sort key
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            # get the category name from the request.GET
            categories = request.GET["category"].split(",")
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

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product detail"""

    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Add a product to the store"""

    # only store owners can manage products
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""

    # only store owners can manage products
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""

    # only store owners can manage products
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
