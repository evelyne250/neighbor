from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'new-hood/', views.create_hood, name='new-hood'),
    url(r'^new/post$', views.new_post, name='new-post'),
    # url(r'single_hood/(\d+)', views.single_hood, name='single-hood'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^edit/profile', views.profile_edit, name='profile_edit'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)