from django.urls import re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/', views.signup, name='signup'),
    re_path(r'^login/', views.loginview, name='login'),
    re_path(r'^logout/', views.logout_view, name='logout'),

]