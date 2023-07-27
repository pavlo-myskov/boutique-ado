from django.shortcuts import render, redirect


def view_bag(request):
    '''A view that renders the bag contents page'''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Store the quantity of the item to the session
    bag = request.session.get('bag', {})
    bag[item_id] = bag.get(item_id, 0) + quantity
    request.session['bag'] = bag

    return redirect(redirect_url)
