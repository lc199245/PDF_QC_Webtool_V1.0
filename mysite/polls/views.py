from django.shortcuts import get_object_or_404, render;
from django.http import HttpResponseRedirect, HttpResponse;
from django.urls import reverse;
from django.views import generic;
from .models import *;
import sys;
import json;

# Create your views here.


class IndexView(generic.ListView):
	template_name = 'polls/index.html';
	context_object_name = 'first_test_field_value_list';
	def get_queryset(self):
		# print Question.objects.order_by('-pub_date')[:5];
		return Doc_Field_Value().get_test_field_values();

class DetailView(generic.DetailView):
	model = Question;
	template_name = 'polls/detail.html';

class ResultsView(generic.DetailView):
	model = Question;
	template_name = 'polls/results.html';

def highlight(request,field_value_id):
	print field_value_id; 	
	from Show_highlight_Pic import draw_and_show_pic;
	binpic = draw_and_show_pic(int(field_value_id));
	print type(binpic);
	print binpic[:20];
	return render(request, 'polls/temp.html', {'field_value_id':field_value_id, 'binpic':binpic});

def request_page(request):
	if(request.GET.get('hlbtn')):
		from Show_highlight_Pic import draw_and_show_pic;
		binpic = draw_and_show_pic(int(request.GET.get('')))
	return render(request, 'polls/index.html', {'field_value_id':field_value_id, 'binpic':binpic});


def ajax_highlight(request, field_value_id):
	from Show_highlight_Pic import draw_and_show_pic;
	binpic = draw_and_show_pic(int(field_value_id));
	pic_list = [];
 	pic_list.append({"binpic" : binpic});
 	pic_json = json.dumps(pic_list);
 	response = HttpResponse();
 	response['Content-Type'] = "text/javascript";
 	response.write(pic_json);
 	print 'hehe!';
 	return response;



def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id);
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice']);
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			});
	else:
		selected_choice.votes += 1;
		selected_choice.save();
		return HttpResponseRedirect(reverse('polls:results', args=(question.id, )));
