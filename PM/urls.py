"""define PM's url model"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # main page
    url(r'^$', views.index, name='index'),
    # all project
    url(r'^projects/$', views.projects, name='projects'),
    # add new project 
    url(r'^new_project/$', views.new_project, name='new_project'),
    # delete project
    url(r'^del_project/(?P<project_id>\d+)/$', views.del_project, name='del_project'),
    # renew project
    url(r'^renew_project/(?P<project_id>\d+)/$', views.renew_project, name='renew_project'),
    # finished
    url(r'^finished/(?P<project_id>\d+)/$', views.finished, name='finished'),
    # search
    url(r'^search/$', views.search, name='search'),
]
