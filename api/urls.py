from django.urls import path
from . import views

urlpatterns = [
    path('getuser/', views.returnUser, name='returnUser'),
    path('sentiment',views.senttxt)
]