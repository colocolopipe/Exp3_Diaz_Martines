from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

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
    path('revista', views.revista, name='revista'),
    path('revista/crear', views.crear, name='crear'),
    path('revista/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('revista/editar/<int:id>', views.editar, name='editar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
