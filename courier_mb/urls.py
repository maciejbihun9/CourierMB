
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls import include
from rest_framework import routers




urlpatterns = [
    url(r'^home/', views.get_home_page, name="home_page"),
    url(r'^signup/', views.get_signup_form, name="sign_up_form"),
    url(r'^send_inter_package/', views.get_send_package_page, name="send_package_page"),
    url(r'^login/', views.get_login_form, name="login_form"),
    url(r'^package_details/', views.get_package_details_page, name="package_details_page"),
    url(r'^login/', views.get_login_form, name="log_in_form"),
    url(r'^profile/', views.get_my_profile, name="my_profile"),
]
