"""YiQ URL Configuration

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
from django.urls import path
from StuLogin.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stulogin/', stulogin),
    path('login/',login),
    path('facility/',showFacility),
    path('facility/<str:fid>',facilityDetail),
    path('facility/<str:fid>/comment',showComment),
    path('showInfo/<str:id>',showInfo),
    path('repair/',repair),
    # path(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
]
