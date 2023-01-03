from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.Employeesignup.as_view(),name='signup'),
]