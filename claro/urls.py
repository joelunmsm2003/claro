
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', 'claroapp.views.home'),
    url(r'^subir$', 'claroapp.views.subir'),
    url(r'^cliente$', 'claroapp.views.cliente'),
    url(r'^uploadfile$', 'claroapp.views.uploadfile'),

]
