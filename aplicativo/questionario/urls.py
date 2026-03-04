from django.urls import path
from . import views
urlpatterns = [
    path('questionario/', views.abrir_questionario, name='questionario'),
    path('detalhequestionario/', views.detalhe_questionario, name='detalhe_questionario'),
]