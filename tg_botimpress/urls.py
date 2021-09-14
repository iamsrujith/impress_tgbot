"""tg_botimpress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from bot_app.views import handle_bot_request,view_clicks
from django.conf.urls import url

urlpatterns = [
    url(r'^c817304a3d163ebd58b44dd446eba29572300724098cdbca1a/?$', handle_bot_request),
    url(r'^admin/', admin.site.urls),
    url(r'view-clicks/',view_clicks)
]
