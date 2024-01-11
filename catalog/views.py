from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Review, Version
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Главная',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()[:3]
        return context_data


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/products_list.html'

    def get_queryset(self):
        queryset = super().get_queryset().all()
        if not self.request.user.is_staff:
            return queryset.filter(user=self.request.user, is_published=True)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['version'] = Version.objects.all()
        context['title'] = 'Все товары'
        return context


def contacts(request):
    context = {
        'title': 'O.S.Ky: Вход/Регистрация'
    }
    return render(request, 'catalog/contacts.html', context)


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'catalog/categories.html'
    extra_context = {
        'title': 'Категории'
    }


@login_required
def product_card(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Товары категории {category_item.category_name}'
    }

    return render(request, 'catalog/product_card.html', context)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['versions'] = self.object.version_set.all()
        return context_data


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


class ReviewCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Review
    permission_required = 'catalog.add_review'
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


class ReviewUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Review
    permission_required = 'catalog.change_review'
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


class ReviewDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Review
    permission_required = 'catalog.delete_review'
    success_url = reverse_lazy('catalog:reviews')


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    permission_required = 'catalog.add_product'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_card', args=[self.kwargs.get('pk')])


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    permission_required = 'catalog.change_product'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_card', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    form_class = ProductForm

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse('catalog:product_card', args=[self.kwargs.get('pk')])
