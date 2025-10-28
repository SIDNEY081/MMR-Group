from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ventures/', views.ventures, name='ventures'),
    path('ventures/tech/', views.tech_solutions, name='tech'),
    path('ventures/construction/', views.construction, name='construction'),
    path('ventures/aluminium/', views.aluminium_glass, name='aluminium'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
]