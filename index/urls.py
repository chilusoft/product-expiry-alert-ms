from django.urls import path, include
from . import views

app_name='index'

urlpatterns=[
    path('', views.index, name='index'),
    path('products/', include('products.urls'))
]