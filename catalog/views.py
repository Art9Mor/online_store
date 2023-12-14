from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
