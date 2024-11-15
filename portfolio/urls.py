from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('contact/',views.contact_create,name='contact_create'),
    path('contact/success/',views.contact_success_view,name='contact_success')
]