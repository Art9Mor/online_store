from django.shortcuts import render

from catalog.models import Product, Category


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    context = {
        'title': 'O.S.Ky: Вход/Регистрация'
    }
    return render(request, 'catalog/contacts.html', context)


def password(request):
    if request.method == 'GET':
        password_pr = request.GET.get('password')
        print(f'Пароль: {password_pr}')
    context = {
        'title': 'O.S.Ky: Пароль'
    }
    return render(request, 'catalog/password.html', context)


def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'O.S.Ky: Главная'
    }
    return render(request, 'catalog/index.html', context)


def products_list(request):
    prod_list = Product.objects.all()
    context = {
        'object_list': prod_list,
        'title': 'O.S.Ky: Товары'
    }

    return render(request, 'catalog/products_list.html', context)


def product_card(request):
    prod_card = Product.objects.all()
    context = {'object_list': prod_card}

    return render(request, 'catalog/product_card.html', context)


def categories(request):
    categories_list = Category.objects.all()
    context = {
        'object_list': categories_list,
        'title': 'O.S.Ky: Категории'
    }

    return render(request, 'catalog/categories.html', context)
