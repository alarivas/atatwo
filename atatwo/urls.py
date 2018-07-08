"""atatwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from front import views as front_views
from graph.views import qr_generate
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve 
from graph.views import compute_risk

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front_views.index),
    path('beneficios/', front_views.beneficios, name="beneficios"),
    path('producto/<str:producto>/', front_views.producto, name="producto"),
    path('descuento/', front_views.descuento_single, name="descuento"),
    path('generate_qr/', qr_generate, name="generate_qr"),
    path('', include('notifications.urls')),
    path('send_email/<str:producto>/', front_views.send_email, name='send_email'),
    path('risk/', compute_risk, name='compute_risk'),
    path('dashboard/', front_views.dashboard, name='dashbaord'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
