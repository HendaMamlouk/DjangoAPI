from django.conf.urls import url
from EmployeeApp import views

urlpatterns=[
    url(r'^departement/$', views.departementApi),
    url(r'^departement/([0-9]+)$', views.departementApi)

    #url(r'^employee/$', views.departementApi),
    #url(r'^employee/([0-9]+)$', views.departementApi)
]