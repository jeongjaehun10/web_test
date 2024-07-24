"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from blog import views  # blog 앱의 views 모듈을 import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('401/', views.error_401, name='error_401'),
    path('404/', views.error_404, name='error_404'),
    path('500/', views.error_500, name='error_500'),
    path('charts/', views.charts, name='charts'),
    path('layout-sidenav-light/', views.layout_sidenav_light, name='layout_sidenav_light'),
    path('layout-static/', views.layout_static, name='layout_static'),
    path('login/', views.login, name='login'),
    path('password/', views.password, name='password'),
    path('register/', views.register, name='register'),
    path('tables/', views.tables, name='tables'),
]

