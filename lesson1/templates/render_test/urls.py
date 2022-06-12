from django.urls import path
from . import views

urlpatterns = [
    path('first_page/', views.first_page, name='first_page'),
    path('web_tech/', views.web_tech, name='web_tech'),
    path('samples_list', views.SampleModelView.as_view(), name='sample_list')
]