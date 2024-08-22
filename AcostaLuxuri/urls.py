from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciar', views.iniciar, name='iniciar'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('accesorio/', views.accesorio, name='accesorio'),
    path('accesorio/crear/', views.create_accesorio, name='create_accesorio'),
    path('accesorio/insert', views.insert_accesorio, name='insert_accesorio'),

    path('accesorio/edit', views.edit_accesorio, name='edit_accesorio'),
    path('accesorio/update', views.update_accesorio, name='insert_accesorio'),

    path('accesorio/remove/', views.remove_accesorio, name='create_accesorio'),
    path('accesorio/delete', views.delete_accesorio, name='insert_accesorio'),

    # Nueva URL para añadir a favoritos
    path('accesorio/favoritos', views.insert_favoritos, name='insert_favoritos'),
]
