from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
#  path(r'^$', views.IndexView.as_view(), name = 'index'  ),

    path('<int:pk>/', views.LocatonView.as_view(), name = 'property'),
    path('<int:cpk>/<int:pk>/', views.PropertyDetail.as_view(), name = 'propertyview'),

]
