from django.urls import path, include

urlpatterns = [
    path('contacts', include('shop.urls')),
    path('delevery', include('shop.urls')),
]
