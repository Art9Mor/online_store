from django.urls import path

from catalog.apps import MainConfig
from catalog.views import index, contacts, password, product_card, categories, ProductListView, ProductDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', contacts, name='contacts'),
    path('ind/', index, name='index'),
    path('pass/', password, name='password'),
    path('prod_list/', ProductListView.as_view(), name='products_list'),
    path('<int:pk>/prod_card/', product_card, name='product_card'),
    path('cat/', categories, name='categories'),
    path('<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail')

]
