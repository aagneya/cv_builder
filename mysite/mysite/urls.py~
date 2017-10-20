"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include,url
from django.contrib import admin


from django.conf.urls.static import static
from django.conf import settings

from blog.views import index,post_new,post_ONE,resume,form1detail,post_edit,post_remove,detail,form2detail,post_TWO,post_THREE,form3detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    ########## Project ############
    url(r'^$', index, name='index'),
# Three posts urls
    url(r'^post_new/', post_new, name='post_new'),
    url(r'^post_ONE/', post_ONE, name='post_ONE'),
    url(r'^post_TWO/', post_TWO, name='post_TWO'),
    url(r'^post_THREE/', post_THREE, name='post_THREE'),
   


############ Three Resume designs
    
    url(r'^(?P<pk>\d+)/', form1detail, name='form1detail'),

    url(r'^formtwo/(?P<pk>\d+)/', form2detail, name='form2detail'),
    
    url(r'^formthree/(?P<pk>\d+)/', form3detail, name='form3detail'),
  
   

####### Last updated Resume List ###################
    url(r'^resume/', resume, name='resume'),

############ detail of the person ###############
    url(r'^formtwo/(?P<pk>\d+)/$', detail, name='detail'),

    

    ## edit ######
    url(r'^post/(?P<pk>\d+)/edit/$', post_edit, name='post_edit'),
    ### delete #########

    url(r'^post/(?P<pk>\d+)/remove/$', post_remove, name='post_remove'),


    url(r'^accounts/', include('registration.backends.simple.urls')),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
