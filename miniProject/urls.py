from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    url(r'^$',views.user_login,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
