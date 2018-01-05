from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail)
]
# to be able to view format based response
# e.g /snippets.json for json and /snippets.api for browsable api
urlpatterns = format_suffix_patterns(urlpatterns)
