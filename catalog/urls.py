from django.urls import path

from catalog.views import index, contacts

urlpatterns = [
    path('', contacts),
    path('', index)
]
