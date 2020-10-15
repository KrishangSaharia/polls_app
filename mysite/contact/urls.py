from django.urls import path
from contact import views 

urlpatterns = [
        path('',views.main, name='main'),
        path('sample/<int:guess>',views.sample,name='sample')
        ]

