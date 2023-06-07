"""cclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from page.views import (
    home_view,
    about_us_view, 
    contact_us_view,
    project_us_view,
    links_us_view,
    director_us_view,
    announcement_us_view,
    )

urlpatterns = [
    path('', home_view, name='home'),
    path('hakkimizda/', about_us_view, name='about_us'),
    path('iletisim/', contact_us_view, name='contact_us'),
    path('projeler/', project_us_view, name='project_us'),
    path('faydali-linkler/', links_us_view, name='links_us'),
    path('ekibimiz/', director_us_view, name='director_us'),
    path('duyurular/', announcement_us_view, name='announcement_us'),
    path("admin/", admin.site.urls),
]
