from django.urls import path
from . import views

app_name = 'farm'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog-details/', views.blogDetails, name='blog-details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
]