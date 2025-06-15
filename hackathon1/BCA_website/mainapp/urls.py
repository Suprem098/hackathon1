from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('semester/<str:semester_name>/', views.semester_detail, name='semester_detail'),
    path('account/signin/', views.sign_in, name='sign_in'),
    path('account/create/', views.create_account, name='create_account'),
    path('notices/', views.notices, name='notices'),
    path('contact/', views.contact, name='contact'),
]
