from django.urls import include,path
from myapp.views import *
from django.conf.urls import url

urlpatterns = [
	url(r"^$",index,name='index'),
	path("signin/",signin,name='signin'),
	path("signup/",signup,name='signup'),
	path("logout/",signout,name='logout')
]