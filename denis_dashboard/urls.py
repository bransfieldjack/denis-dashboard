from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accounts_urls
from accounts.views import index, login


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'), 
    url(r'^accounts/', include(accounts_urls)),
    url(r'^accounts/login/$', login, name='login'),
]
