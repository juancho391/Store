from django.urls import path
from .views import home , contact


app_name = "mystore"

urlpatterns = [
    path('', home, name='store'),
    path('contact/', contact, name='contact')
]