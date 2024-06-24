from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('noticia2/', views.noticia2, name='noticia2'),
    path('noticia3/', views.noticia3, name='noticia3'),
    path('noticia4/', views.noticia4, name='noticia4'),
    path('carrete/', views.carrete, name='carrete'),
    path('servicios/', views.servicios, name='servicios'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('revistas/', views.revistas, name='revistas'),
    path('revista', views.revista, name='revista')
]
