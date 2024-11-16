from django.urls import path

from AgriCulture import settings
from . import views
from django.conf.urls.static import static

app_name = 'farm'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog-details/<id>/', views.blogDetails, name='blog-details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('insert_image/', views.insert_image, name='insert_image'),
    path('insert_testimonial/', views.insert_testimonial, name='insert_testimonial'),
    path('insert_blog/', views.insert_blog, name='insert_blog'),
    path('insert_contact/', views.insert_contact, name='insert_contact'),
    path('insert_team/', views.insert_team, name='insert_team'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('insert_post/', views.insert_post, name='insert_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)