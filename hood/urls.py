from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^all-hoods', views.hoods, name='hood'),
    url(r'join_hood/(\d+)', views.join_hood, name='join-hood'),
    url(r'leave_hood/(\d+)', views.leave_hood, name='leave-hood'),
    url(r'new-hood/', views.create_hood, name='new-hood'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^new/business$', views.new_business, name='new_business'),
    # url(r'single_hood/(\d+)', views.single_hood, name='single-hood'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^edit/profile', views.profile_edit, name='profile_edit'),
    # url(r'<hood_id>/members', views.hood_members, name='members'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)