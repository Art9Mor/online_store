from django.urls import path

from catalog.apps import MainConfig
from catalog.views import index, contacts, password, products_list, product_card, categories

app_name = MainConfig.name

urlpatterns = [
    path('', contacts, name='contacts'),
    path('ind/', index, name='index'),
    path('pass/', password, name='password'),
    path('prod_list/', products_list, name='products_list'),
    path('prod_card/', product_card, name='product_card'),
    path('cat', categories, name='categories'),

]
