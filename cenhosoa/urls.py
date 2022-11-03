"""cenhosoa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', app.views.home, name='home'),
    re_path('^auth/$', app.views.auth, name='auth'),
    re_path('^sudo/(\w+)/', app.views.sudo, name='sudo'),
    re_path('^goto/', app.views.goto, name='goto'),
    re_path('^sudoQuery/', app.views.sudoQuery, name='sudo'),
    re_path('^hiala/', app.views.hiala, name='hiala'),
    re_path('^register/$', app.views.register, name='register'),

    # tabs
    re_path('^mofonaina/$', app.views.mofonaina, name='mofonaina'),
    re_path('^sampana/$', app.views.sampana, name='sampana'),
    re_path('^vaovao/$', app.views.vaovao, name='vaovao'),
    re_path('^fiangonana/$', app.views.fiangonana, name='rantsana'),
    re_path('^hafa/$', app.views.hafa, name='hafa'),
    re_path('^hikaroka/$', app.views.hikaroka, name='hikaroka'),

    # article
    re_path('^mofonaina/vaovao/$', app.views.mofonaina_vaovao, name='mofonaina_vao'),
    re_path('^mofonaina/(\d+)$', app.views.mofonaina_mamaky, name='mofonaina_mamaky'),

    # about
    re_path('^terms/$', app.views.terms, name='terms'),

    # check sampana
    re_path('^sampana/(\w+)/$', app.views.view_sampana),
    re_path('^rooter/', app.views.rooter),

    re_path('^boite_a_idee/', app.views.boite_a_idee, name='boite_a_idee'),

    # update and delete
    re_path('^update/', app.views.update),
    re_path('^remove/', app.views.remove),

    # download
    re_path('^download/', app.views.downloader),

]
