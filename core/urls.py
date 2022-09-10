from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema
from ninja import NinjaAPI
from fund.api import api

urlpatterns = [
    # path("api/", api.urls),
    path("control_pannel/", admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
