from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

import bsmain.views

# admin.autodiscover()
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'sometest.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^accounts/', include('allauth.urls')),

                       url(r'^hello/$', bsmain.views.home),
                       url(r'^accounts/login/$', login),
                       url(r'^accounts/logout/$', logout, {'next_page': '/'}),
                       url(r'^accounts/register/$', bsmain.views.register),  # point to bsmain/views.py register function

                       # url(r'^accounts/', include('allauth.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^comments/', include('django_comments.urls')),

                       url(r'^$', bsmain.views.get_bean_list),
                       url(r'^mbean/delete/(\d{1,10})/$', bsmain.views.delete_mbean),
                       url(r'^order/delete/(\d{1,10})/$', bsmain.views.delete_order),
                       url(r'^suborder/delete/(\d{1,5})/$', bsmain.views.get_bean_list),
                       url(r'^search/$', bsmain.views.search),
                       url(r'^save_order/$', bsmain.views.save_mbean),
                       url(r'^suborder/(\d{1,10})/$', bsmain.views.save_order),
                       url(r'^user/$', bsmain.views.user),
                       url(r'^user/beandetail/(\d{1,10})/$', bsmain.views.show_detailbean),

                       url(r'^test/$', bsmain.views.test),
                       url(r'^testFirebase/$', bsmain.views.testFirebase),
                       )
