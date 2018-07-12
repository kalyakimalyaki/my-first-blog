from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    url(r'', include('blog.urls')),
]
