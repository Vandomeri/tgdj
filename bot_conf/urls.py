from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    # path('payment/', include(('payment.urls', 'payment'), namespace='payment')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
