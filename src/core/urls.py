from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from strawberry.django.views import AsyncGraphQLView
from .schemas import schema

urlpatterns = [
    # path("api/", api.urls),
    path("control_pannel/", admin.site.urls),
    path("graphql", AsyncGraphQLView.as_view(schema=schema)),
    path("api/auth/", include("user.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
