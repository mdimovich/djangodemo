from django.conf.urls import url
from . import views #. means import from the current package

urlpatterns=[url(r'^$', views.index, name='index')]

