from django.conf.urls import url
from .views import IndexView
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', IndexView.as_view()),
]
