from django.urls import path

from manage_index import views

urlpatterns = [
    path('', views.index_admin, name='index'),
    path('add/', views.addcategory, name='addcategory'),
    path('list-category/', views.index_category, name='index_category'),
    path('update-category/<int:id>', views.update_category, name='update_category'),
    path('geturl/', views.geturl, name='geturl'),
]