from django.contrib import admin
from django.urls import path
from timeline_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hoje/', views.hoje, name='hoje'),
    path('adicionar-tarefa/', views.adicionar_tarefa, name='adicionar_tarefa'),
]