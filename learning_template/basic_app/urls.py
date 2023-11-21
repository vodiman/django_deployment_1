from django.contrib import admin
from django.urls import path,re_path
from basic_app import views

# Setup namespace for template tagging:
app_name='basic_app'

urlpatterns = [
    # re_path(r"^$",views.index,name="index"),
    # re_path(r"^admin/", admin.site.urls,name="admin"),
    re_path(r"^relative/",views.relative,name="relative"),
    re_path(r"^other/",views.other,name="other"),
]
