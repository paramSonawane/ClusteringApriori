from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('dashboard', views.home, name='home'),
    path('recommendations', views.recommendations, name='recommendations'),
    path('clustering', views.clustering, name='clustering'),
    path('aprOnClustering', views.aprOnClustering, name='aprOnClustering'),
    path('api', views.api, name='api'),

]