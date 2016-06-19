"""myword URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'learn.views.index', name='index'),
	url(r'^function/(?P<function_slug>[^/]+)/$', 'learn.views.function_detail', name='function'),
	url(r'^column/(?P<column_slug>[^/]+)/$', 'learn.views.column_detail', name='column'),
	url(r'^word/(?P<pk>\d+)/(?P<word_slug>[^/]+)/$', 'learn.views.word_detail', name='word'),
	url(r'^function/danci/bdc/$', 'learn.views.bdc', name='bdc'),
	url(r'^function/(?P<function_slug>[^/]+)/reset/$', 'learn.views.reset', name='reset'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('learn.urls')),
]


