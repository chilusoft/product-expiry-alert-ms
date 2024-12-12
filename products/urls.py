from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name='products'
urlpatterns=[
    path('create-product/', views.create_product,name='create-product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)