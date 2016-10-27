from django.conf.urls import include, url;
from . import views;


app_name = 'FieldView'


urlpatterns = [
	
	url(r'^$', views.MainPageView.as_view(), name = 'mainpage'),
	url(r'^(?P<doc_id>[0-9]+)/select_pdf/$', views.select_pdf, name = 'select_pdf'),
	url(r'^contact_us/$', views.show_contact_info, name = 'contact_us'),
	url(r'^(?P<field_value_id>[0-9]+)/ajax_highlight/$', views.ajax_highlight, name = 'ajax_highlight'),
	url(r'^(?P<field_value_id>[0-9]+)/fix_field/$', views.fix_field, name = 'fix_field'),
	url(r'^(?P<field_value_id>[0-9]+)/false_field/$', views.false_field, name = 'fix_field'),
	url(r'^release_file/$', views.release_file, name = 'release_file'),	
	url(r'^(?P<doc_id>[0-9]+)/check_availability/$', views.check_availability, name = 'check_availability'),	
	# url(r'^(?P<doc_id>[0-9]+)/fields_in_doc/$', views.FieldGridView.as_view(), name = 'fieldgrid' ),	

];






# urlpatterns = [ 



# 	url(r'^$', views.IndexView.as_view(), name = 'index'), \
		
# 	url(r'^(?P<field_value_id>[0-9]+)/$', views.highlight, name = 'highlight'),\

# 	url(r'^(?P<field_value_id>[0-9]+)/ajax_highlight/$', views.ajax_highlight, name = 'ajax_highlight'),\

#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),\
#     # ex: /polls/5/results/
#     url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),\
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),



# 	];

