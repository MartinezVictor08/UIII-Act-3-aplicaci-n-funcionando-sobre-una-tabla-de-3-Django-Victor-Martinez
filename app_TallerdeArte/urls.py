from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_TallerdeArte, name='inicio_TallerdeArte'),
    path('agregar_instructor/', views.agregar_instructor, name='agregar_instructor'),
    path('ver_instructor/', views.ver_instructor, name='ver_instructor'),
    path('actualizar_instructor/<int:id>/', views.actualizar_instructor, name='actualizar_instructor'),
    path('realizar_actualizacion_instructor/<int:id>/', views.realizar_actualizacion_instructor, name='realizar_actualizacion_instructor'),
    path('borrar_instructor/<int:id>/', views.borrar_instructor, name='borrar_instructor'),
]