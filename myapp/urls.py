from django.conf.urls import url
from myapp import views

urlpatterns = [
        url(r'^library/$', views.library),
        url(r'^library/([0-9]+)$', views.library)
]