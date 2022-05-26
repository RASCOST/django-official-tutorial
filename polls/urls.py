from django.urls import path
import . from views

urlpatterns = [
    path('', views.index, name='index')
]
