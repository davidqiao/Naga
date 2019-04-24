from django.conf.urls import url, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'blog', BlogAPI)
app_name = 'blog'


extra_pattern = [
    url(r'^details/(?P<bid>.+)$', blog_details, name='details'),
    url(r'^tags$', tags, name='tags'),
    url(r'^categories$', categories, name='categories'),
    url(r'^archives$', archives, name='archives'),
    url(r'^comment$', comment, name='comment'),
    url(r'^blogtags$', blogtags, name='blogtags'),
]


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^b/', include(extra_pattern)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'feed/', RssFeed(), name="RSS"),
    url(r'^search/', QSearchView(), name='haystack_search'),
]