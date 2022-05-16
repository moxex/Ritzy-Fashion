from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='product')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('mart.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)