from django.urls import path
from .views import home, xburger, pizza, contato

urlpatterns = [
    path('', home, name='home'),
    path('xburger/', xburger, name='xburger'),
    path('pizza/', pizza, name='pizza'),
    path('contato/', contato, name='contato'),
]
