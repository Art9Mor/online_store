from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Category, Review
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    extra_context = {
        'title': 'Все товары'
    }


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


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/categories.html'
    extra_context = {
        'title': 'Категории'
    }


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


class ReviewListView(ListView):
    model = Review
    template_name = 'catalog/review_list.html'
    extra_context = {
        'title': 'Все отзывы'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ReviewCreateView(CreateView):
    model = Review
    fields = ('title', 'text', 'photo', 'is_published')
    success_url = reverse_lazy('catalog:reviews')
    extra_context = {
        'title': 'Написать отзыв'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_review = form.save()
            new_review.slug = slugify(new_review.title)
            new_review.save()
        return super().form_valid(form)


class ReviewUpdateView(UpdateView):
    model = Review
    fields = ('title', 'slug', 'text', 'photo')

    def form_valid(self, form):
        if form.is_valid():
            new_review = form.save()
            new_review.slug = slugify(new_review.title)
            new_review.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:review_detail', args=[self.kwargs.get('pk')])


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'catalog/review_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('catalog:reviews')
