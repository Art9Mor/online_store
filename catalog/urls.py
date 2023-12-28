from django.urls import path

from catalog.apps import MainConfig
from catalog.views import contacts, password, product_card, ProductListView, ProductDetailView, \
    CategoryListView, ReviewListView, ReviewCreateView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView, IndexView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', contacts, name='contacts'),
    path('ind/', IndexView.as_view(), name='index'),
    path('pass/', password, name='password'),
    path('prod_list/', ProductListView.as_view(), name='products_list'),
    path('<int:pk>/prod_card/', product_card, name='product_card'),
    path('cat/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('reviews_lst/', ReviewListView.as_view(), name='reviews'),
    path('create_review/', ReviewCreateView.as_view(), name='create_review'),
    path('review_detail/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('review_edit/<int:pk>/', ReviewUpdateView.as_view(), name='review_edit'),
    path('review_delete/<int:pk>/', ReviewDeleteView.as_view(), name='delete_review'),
    path('prod_create/<int:pk>', ProductCreateView.as_view(), name='prod_create'),
    path('prod_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('prod_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete')

]
