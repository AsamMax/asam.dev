from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.portfolio, name='about_me'),
    path('about_me', views.portfolio, name='about_me'),
    path('curriculum_vitae', views.cv, name='curriculum_vitae'),
    path('contact', views.contact, name='contact')
]