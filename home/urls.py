from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommendations', views.recommendations, name='recommendations'),
    path('clustering', views.clustering, name='clustering'),
    path('api', views.api, name='api'),

]