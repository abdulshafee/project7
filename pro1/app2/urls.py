from django.urls import
from app2 import views

app_name='app2'

urlpatterns=[
    path('',views.index,name='index'),
    path("sample",views.sample,name="sample"),
]