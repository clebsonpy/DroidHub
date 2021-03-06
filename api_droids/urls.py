"""api_droids URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

admin.site.site_header = "Administração do DroidHub"

schema_view = get_schema_view(
   openapi.Info(
      title="DroidHub API",
      default_version='v1',
      description="Desafio para Desenvolvedor Backend \n"
                  "A vista do <code>ReDoc</code> pode ser encontrada <a rel='noopener noreferrer' target='_blank' href='/redoc/'>aqui</a> \n \n"
                  "Você pode entrar usando o usuário <code>admin</code> pré-existente com senha de acesso <code>admin123</code>.",
      contact=openapi.Contact(email="clebsonpy@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', RedirectView.as_view(url='swagger/', permanent=False), name='index'),
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/demands/', include('demands.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
