from django.urls import path
from . import views
urlpatterns=[
    path('',views.edit,index='index'),
    path('edit/',views.edit,name='post_edit'),
]