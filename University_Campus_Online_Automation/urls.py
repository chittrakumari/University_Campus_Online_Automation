
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('student/', include('Student.urls')),
    path('', views.home_page),


]

urlpatterns += staticfiles_urlpatterns()
