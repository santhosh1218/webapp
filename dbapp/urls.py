from django.urls import path
from dbapp import views
app_name='dbapp'
urlpatterns=[
   
    path('display/<int:pno>',views.Display,name='display'),
    path('empcreate/',views.empcreate,name='empcreate'),
    path('empupdate/<int:id>',views.empupdate,name='empupdate'),
    path('empdelete/<int:id>',views.empdelete,name='empdelete'),
    path('profile/',views.Profile,name='profile'),
    path('search/',views.empsearch,name='search')
   
  
]
