from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'$^', include('pract.apps.home.urls', namespace='home')),
    # url(r'^', include('pract.apps.users.urls', namespace='users')),

    #PYTHON SOCIAL AUTH
    url('', include('social.apps.django_app.urls', namespace='social')),
]
