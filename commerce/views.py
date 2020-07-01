from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from . models import LeaguePackage, LeagueCart, LeagueOrder


class PackageView(View):
    template_name = 'commerce/package.html'
    packages = LeaguePackage.objects.all()
    context = {'packages': packages}

    def get(self, request):
        return render(request, self.template_name, self.context)


def add_to_cart(request, id):
    user_profile = request.user.userprofile
    package = get_object_or_404(LeaguePackage, id=id)
    order_package, created = LeagueCart.objects.get_or_create(
        league_package=package, user_profile=user_profile)

    order_qs = LeagueOrder.objects.filter(
        user_profile=user_profile, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.league_packages.filter(league_package_id=package.id).exists():
            order_package.quantity += 1
            order_package.save()
        else:
            order.league_packages.add(order_package)
            return redirect('/shop/')
    else:
        order = LeagueOrder.objects.create(user_profile=user_profile)
        order.league_packages.add(order_package)

    return redirect('/shop/')


def reduce_from_cart(request, id):
    user_profile = request.user.userprofile
    package = get_object_or_404(LeaguePackage, id=id)
    cart_qs = LeagueCart.objects.filter(
        user_profile=user_profile, league_package=package)
    if cart_qs.exists():
        cart = cart_qs[0]
        if cart.quantity > 1:
            cart.quantity = cart.quantity - 1
            cart.save()
        else:
            cart_qs.delete()

    return redirect('/shop/cart/')


def remove_from_cart(request, id):
    user_profile = request.user.userprofile
    package = get_object_or_404(LeaguePackage, id=id)
    order_qs = LeagueOrder.objects.filter(
        user_profile=user_profile, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        print(order)

        if order.league_packages.filter(league_package_id=package.id).exists():
            order_item = LeagueCart.objects.filter(
                league_package=package, user_profile=user_profile)[0]
            order.league_packages.remove(order_item)
            order_item.delete()
            return redirect('/shop/cart/')

    return redirect('shop/cart/')


class CartView(View):
    def get(self, request):
        order = LeagueCart.cart_manager.get_cart_items(request)
        order_total = LeagueCart.cart_manager.get_cart_total(request, order)
        context = {'order_items': order, 'order_total': order_total}

        return render(request, 'commerce/cart.html', context)


class CheckoutView(View):
    context = {'id': 'book', 'price': 5000}

    def post(self, request):
        return render(request, 'commerce/checkout.html', self.context)

    def get(self, request):
        return render(request, 'commerce/checkout.html', self.context)
