from django.conf.urls import url, include
from pract.apps.users.views import LogOut
from .views import ExtraDataView, UserDetailView
urlpatterns = [
    url(r'^log-out/', LogOut, name='logout'),
    url(r'^extra-data/', ExtraDataView.as_view(), name='extra-data'),
    # url(r'^usuario/(?P<pk>\d+)/$', UserDetailView.as_view(), name='userdetail'),
    url(r'^usuario/(?P<slug>[-\w]+)/$', UserDetailView.as_view(), name='userdetail'),
]
