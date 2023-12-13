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
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def products_list(request):
    prod_list = Product.objects.all()
    context = {
        'object_list': prod_list,
        'title': 'Все товары'
    }

    return render(request, 'catalog/products_list.html', context)


def categories(request):
    categories_list = Category.objects.all()
    context = {
        'object_list': categories_list,
        'title': 'Категории'
    }

    return render(request, 'catalog/categories.html', context)


def product_card(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Товары категории {category_item.category_name}'
    }

    return render(request, 'catalog/product_card.html', context)


# def products_category(request, pk):
#     category_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Category.objects.filter(product_id=pk),
#         'title': ''
#     }

def product_detail(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(product_id=pk),
        'title': f'Товар {product_item.name}'
    }

    return render(request, 'catalog/product_detail.html', context)
