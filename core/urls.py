from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from strawberry.django.views import AsyncGraphQLView
from fund.schemas import schema

urlpatterns = [
    # path("api/", api.urls),
    path("control_pannel/", admin.site.urls),
    path("graphql", AsyncGraphQLView.as_view(schema=schema)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
