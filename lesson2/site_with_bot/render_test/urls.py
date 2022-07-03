from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('web_tech', views.web_tech, name='web_tech'),
    path('samples_list', views.SampleModelView.as_view(), name='sample_list'),
    path('aiogram-testing', views.AiogramTesting.as_view(), name="aiogram_testing"),
    path('ajax-check1', views.AjaxSendingMessageView.as_view(), name='ajax_check1')
]