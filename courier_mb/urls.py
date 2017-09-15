
from django.conf.urls import url
from django.contrib import admin
from . import views
from . import actions
from django.conf.urls import include
from rest_framework import routers
from django.contrib.auth import views as auth_views




urlpatterns = [

    #actions
    url(r'^actions/save_package/$', actions.save_package, name="save_package"),
    url(r'^actions/run_computations/$', actions.run_computations, name="run_computations"),
    url(r'^actions/get_airport/$', actions.get_airport, name="get_airport"),
    url(r'^actions/logout/$',actions.logout_action, name="logout"),
    url(r'^actions/init_database/$',actions.init_database, name="init_database"),
    url(r'^actions/add_to_database/$', actions.add_to_database, name="add_to_database"),
    url(r'^actions/clear_database/$', actions.clear_database, name="clear_database"),
    url(r'^actions/remove_packages/$', actions.remove_packages, name="remove_packages"),

    #views
    url(r'^home/$', views.get_home_page, name="home_page"),
    url(r'^package_details/$', views.get_package_details_page, name="package_details_page"),
    url(r'^profile/$', views.get_my_profile, name="my_profile"),
    url(r'^login/$', views.get_login_form, name="login_form"),
    url(r'^admin_panel/$', views.get_admin_panel, name="admin_panel"),
    url(r'^signup/$', views.get_signup_form, name="sign_up_form"),
    url(r'^send_inter_package/$', views.get_send_package_page, name="send_package_page"),
]
