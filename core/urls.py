from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from ninja import NinjaAPI
from fund.api import api

urlpatterns = [
    # path("api/", api.urls),
    path("control_pannel/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
