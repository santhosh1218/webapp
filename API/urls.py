from django.urls import path
from API import views
app_name='API'
urlpatterns=[
    path('getemp/',views.empget,name='getemp'),
]