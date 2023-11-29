from django.urls import path

from catalog.views import index, contacts, password

urlpatterns = [
    path('', contacts),
    path('ind', index),
    path('pass', password)
]
