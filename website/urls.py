from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('blog.html', views.blog, name="blog"),
    path('pricing.html', views.pricing, name="pricing"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),
    path('contact.html', views.contact, name="contact"),
    path('blog-details.html', views.blogdetails, name="blog-details"),

]
