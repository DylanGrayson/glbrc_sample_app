"""glbrc_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views as home_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', home_views.index, name="index"),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^add-app/', home_views.add_app, name="add-app"),
    url(r'^remove-app/', home_views.remove_app, name="remove-app"),
]
