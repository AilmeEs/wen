from django.urls import path
from . import views
urlpatterns=[
    path('',views.edit,index='index'),
    path('edit/',views.edit,name='post_edit'),
    path('post/delete_/<int:id>/', views.delete_, name='delete_'),

]