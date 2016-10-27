from django.conf.urls import include, url;
from . import views;


app_name = 'polls';



urlpatterns = [ 



	url(r'^$', views.IndexView.as_view(), name = 'index'), \
		
	url(r'^(?P<field_value_id>[0-9]+)/$', views.highlight, name = 'highlight'),\

	url(r'^(?P<field_value_id>[0-9]+)/ajax_highlight/$', views.ajax_highlight, name = 'ajax_highlight'),\

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),\
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),\
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),



	];

