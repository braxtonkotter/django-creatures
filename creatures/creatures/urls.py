"""
URL configuration for creatures project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from creaturesApp import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

app_name = 'creaturesApp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('account/', views.account, name='account'),
    path('admin-dashboard/', views.adminDashboard, name='admin-dashboard'),
    path('details/<int:item_id>', views.details, name='details'),
    path('results/', views.results, name='results'),
    path('sign-up/', views.signUp, name='sign-up'),
    path('tickets/', views.tickets, name='tickets'),
    path('login/', LoginView.as_view(template_name='creaturesApp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', views.search, name='search'),
    path('results/<int:id>', views.results, name='results'),
    path('popular/', views.popular, name='popular'),

    path('edit/<int:item_id>', views.tickets, name='edit'),
    path('delete/<int:item_id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('message/<int:ticket_id>/<int:ruling_id>', views.message, name='message'),


]
