from django.shortcuts import get_object_or_404, render;
from django.http import HttpResponseRedirect, HttpResponse;
from django.urls import reverse;
from django.views import generic;
from .models import *;
import sys,os;
import json;
from django.db import connection, transaction;
# Create your views here.
pdf_file_list_global = 0;
page_pic_list_global = 0;
fields_for_selected_PDF_list_global = 0;
doc_id_global = 0;
# class MainPageView(generic.ListView):
# 	template_name = 'FieldView/mainpage.html';
# 	context_object_name = 'pdf_file_list';
# 	print 'hoho?';
# 	def get_queryset(self):
# 		print 'haha>?'
# 		return Doc_PDF().get_doc_pdf_all();

class MainPageView(generic.ListView):
	template_name = 'FieldView/mainpage.html';
	context_object_name = 'pdf_file_list';
	def get_queryset(self):
		# print 'haha>?'
		pdf_file_list = Doc_PDF.objects.raw("""SELECT xdp.[Doc_ID],\
			xdp.[Agency_Name], 
			xdp.[Doc_Version],
			xdp.[PDF_File_Name], 
			xdp.[Import_Date_Time], 
			xdli.[Login_User_Name],
			xdli.[QC_Start_Time],
			xdli.[Current_Status], 
			xdli.[Number_Of_Items] 
			FROM [xtr].[Doc_PDF] xdp 
			LEFT JOIN (SELECT *, ROW_NUMBER() OVER (PARTITION BY xdli.[Doc_ID] ORDER BY xdli.[QC_Start_Time] DESC) as seqnum 
				FROM [xtr].[UI_Doc_User_Status] xdli) xdli ON xdp.[Doc_ID] = xdli.[Doc_ID] and seqnum=1 ORDER BY [Doc_ID] DESC;""");
		for i in pdf_file_list:
			print i.Doc_ID;
		global pdf_file_list_global;
		pdf_file_list_global = pdf_file_list;

		pdf_file_list = list(pdf_file_list);

		for item in pdf_file_list:
			number_of_items_sql_str = """SELECT COUNT(*) FROM
			(
			SELECT  [Field_Value_ID]
					[Doc_ID]
					FROM
			 (SELECT 
					[Field_Value_ID],
					all_raw.[Field_Name_ID],
					[Calcrt_Value_Sent_DT],
					all_raw.[Calcrt_ID],
					[Check_Flag],
					[Tranche_ID]
			  FROM
			 (SELECT * FROM 
				(
				SELECT * FROM [xtr].[Doc_Field_Value] 
				WHERE [Check_Flag] > 1 AND [Field_Name_ID] in 
				 (SELECT [Field_Name_ID] FROM [xtr].[Doc_Field_Name] 
					WHERE [Tranche_ID] in 
					( SELECT [Tranche_ID] FROM [xtr].[Doc_Tranche] 
						WHERE [Deal_ID] = (SELECT [Deal_ID] FROM [xtr].[Doc_Deal] WHERE [Doc_ID]=""" + str(item.Doc_ID)+ """)) 
					)) as fvt INNER JOIN [xtr].[Doc_Field_Pic_Info] fpit ON fvt.Field_Value_ID = fpit.Doc_Field_Value_ID ) as all_raw INNER JOIN [xtr].[Doc_Field_Name] xdf 
					on all_raw.[Field_Name_ID] = xdf.[Field_Name_ID]) as all_raw_2 INNER JOIN [xtr].[Doc_Tranche] xdt ON all_raw_2.[Tranche_ID] = xdt.[Tranche_ID]  WHERE ([Field_Value_ID] not in (SELECT [Field_Value_ID] FROM [xtr].[UI_User_Action_Hist])) 
					OR ([Calcrt_Value_Sent_DT] > (SELECT TOP 1 [Date_Marked] FROM [xtr].[UI_User_Action_Hist] xuw WHERE xuw.[Field_Value_ID] = [Field_Value_ID] ORDER BY xuw.[Date_Marked] DESC)) ) total ;""";
			cursor = connection.cursor();
			cursor.execute(number_of_items_sql_str);
			number_of_items = cursor.fetchall()[0][0];
			# print number_of_items;
			item.Number_Of_Items = number_of_items;

			# print item.Number_Of_Items;
			# print '--------------------------';

		for item in pdf_file_list:
			# print item.Number_Of_Items,item.Current_Status;
			if item.Number_Of_Items > 0 and item.Current_Status == 'Processed':
				# print 'HEHE!';
				update_lockup_info_sqlstr = """UPDATE [xtr].[UI_Doc_User_Status] SET [Current_Status] = 'Processing', [Number_Of_Items] = """ + str(item.Number_Of_Items) + """ WHERE [Doc_ID] = """ + str(item.Doc_ID) + """;""";				
				cursor = connection.cursor();
				cursor.execute(update_lockup_info_sqlstr);
				transaction.commit();

		return pdf_file_list;


def get_all_fields_by_doc_id(doc_id):




	query_all_fields_by_doc_id_sqlstr = """  SELECT [Field_Value_ID],\
		all_raw_2.[Field_Name_ID],
		[Field_Value],
		[Field_Value_Is_Numeric],
		[Calcrt_Value],
		[Calcrt_Value_Sent_DT],
		all_raw_2.[Calcrt_ID],
		[Check_Flag],
		[Doc_Field_Pic_Info_ID],
		[Doc_Page_Pic_ID],
		[Doc_Pic_Rotation_Degree],
		[Pos_Minpoint_X],
		[Pos_Minpoint_Y],
		[Pos_Maxpoint_X],
		[Pos_Maxpoint_Y],
		all_raw_2.[Tranche_ID],
		[Deal_ID],
		[Tranche_Name],
		[Cusip]
		FROM
 (SELECT 
		[Field_Value_ID],
		all_raw.[Field_Name_ID],
		[Field_Value],
		[Field_Value_Is_Numeric],
		[Calcrt_Value],
		[Calcrt_Value_Sent_DT],
		all_raw.[Calcrt_ID],
		[Check_Flag],
		[Doc_Field_Pic_Info_ID],
		[Doc_Page_Pic_ID],
		[Doc_Pic_Rotation_Degree],
		[Pos_Minpoint_X],
		[Pos_Minpoint_Y],
		[Pos_Maxpoint_X],
		[Pos_Maxpoint_Y],
		[Tranche_ID]
  FROM
 (SELECT * FROM 
	(
	SELECT * FROM [xtr].[Doc_Field_Value] 
	WHERE [Check_Flag] > 1 AND [Field_Name_ID] in 
	 (SELECT [Field_Name_ID] FROM [xtr].[Doc_Field_Name] 
		WHERE [Tranche_ID] in 
		( SELECT [Tranche_ID] FROM [xtr].[Doc_Tranche] 
			WHERE [Deal_ID] = (SELECT [Deal_ID] FROM [xtr].[Doc_Deal] WHERE [Doc_ID]=""" + str(doc_id) +""")) 
		)) as fvt INNER JOIN [xtr].[Doc_Field_Pic_Info] fpit ON fvt.Field_Value_ID = fpit.Doc_Field_Value_ID ) as all_raw INNER JOIN [xtr].[Doc_Field_Name] xdf 
		on all_raw.[Field_Name_ID] = xdf.[Field_Name_ID]) as all_raw_2 INNER JOIN [xtr].[Doc_Tranche] xdt ON all_raw_2.[Tranche_ID] = xdt.[Tranche_ID]  WHERE ([Field_Value_ID] not in (SELECT [Field_Value_ID] FROM [xtr].[UI_User_Action_Hist])) 
		OR ([Calcrt_Value_Sent_DT] > (SELECT TOP 1 [Date_Marked] FROM [xtr].[UI_User_Action_Hist] xuw WHERE xuw.[Field_Value_ID] = [Field_Value_ID] ORDER BY xuw.[Date_Marked] DESC))  ORDER BY [Field_Value_ID] ASC;""";
	
	# print query_all_fields_by_doc_id_sqlstr;
	fields_for_selected_PDF_list = Doc_Field_Value.objects.raw(query_all_fields_by_doc_id_sqlstr);
	
	return fields_for_selected_PDF_list;
	

def lockup_pdf_file(doc_id):
	user_name = os.environ.get("USERNAME");
	user_full_name_sqlstr = """ SELECT * FROM [Mortgages].[xtr].[User_Details_View] WHERE CorpUserName = \'""" + str(user_name) + """';""";	
	cursor = connection.cursor();
	cursor.execute(user_full_name_sqlstr);
	user_info_list  = cursor.fetchall();
	if len(user_info_list) > 0:
		user_full_name = ' '.join(user_info_list[0][1:3]);
	else:
		user_full_name = user_name;
	# print user_full_name;
	lockup_sqlstr = """IF NOT EXISTS (SELECT * FROM [xtr].[UI_Doc_User_Status] WHERE [Doc_ID] = """ + str(doc_id) + """)""";
	number_of_items = len(list(fields_for_selected_PDF_list_global));
	lockup_sqlstr = lockup_sqlstr + """INSERT INTO [xtr].[UI_Doc_User_Status] VALUES(""" + str(doc_id) + """, \' """  + user_full_name + """ \' , GETDATE(), \'Processing\', """ + str(number_of_items) + """ ); """ ;
	cursor = connection.cursor();
	cursor.execute(lockup_sqlstr);
	transaction.commit(); 
	# print '--';







def get_all_page_pic_by_doc_id(doc_id):
	# print '--';
	query_all_page_pic_by_doc_id = "SELECT * FROM [xtr].[Doc_Page_Pic] WHERE [Doc_ID] = " + str(doc_id);
	page_pic_list = Doc_Page_Pic.objects.raw(query_all_page_pic_by_doc_id);
	global page_pic_list_global;
	page_pic_list_global = page_pic_list;
	# print '--';
	# print '---------------------';
	# for item in page_pic_list:
	# 	print item.Doc_Page_Pic_ID;

	return page_pic_list;


def check_file_lockup(doc_id):
	check_file_lockup_sqlstr = """ SELECT * FROM [xtr].[UI_Doc_User_Status] WHERE [Doc_ID] = """ + str(doc_id) + """ AND [Current_Status]='Processing' ORDER BY [QC_Start_Time] DESC""";
	cursor = connection.cursor();
	cursor.execute(check_file_lockup_sqlstr);
	lockup_result = cursor.fetchall();
	if len(lockup_result) > 0: 
		return True;
	else:
		return False;



def check_availability(request, doc_id):
	user_name = os.environ.get("USERNAME");
	user_full_name_sqlstr = """ SELECT * FROM [Mortgages].[xtr].[User_Details_View] WHERE CorpUserName = \'""" + str(user_name) + """';""";	
	cursor = connection.cursor();
	cursor.execute(user_full_name_sqlstr);
	user_info_list  = cursor.fetchall();
	if len(user_info_list) > 0:
		user_full_name = ' '.join(user_info_list[0][1:3]);
	else:
		user_full_name = user_name;
	# print user_full_name;
	current_name_sqlstr = """ SELECT TOP 1 [Login_User_Name] FROM [xtr].[UI_Doc_User_Status] WHERE [Doc_ID] = """ + str(doc_id) + """ ORDER BY [QC_Start_Time] DESC;""";	
	cursor.execute(current_name_sqlstr);
	current_user_list  = cursor.fetchall();
	if len(current_user_list) == 1 and user_full_name not in current_user_list[0][0]:
		# print len(current_user_list[0][0]), len(user_full_name);
		response = HttpResponse();
		response['Content-Type'] = "text/javascript";
		info_list = [];
		info_list.append({"" : "test"});
		info_json = json.dumps(info_list);
		response.write(info_json)
		return response;	
	else:
		print '                                         ',len(user_full_name),user_full_name;
		# select_pdf(request, doc_id);
	


def select_pdf(request, doc_id):
	global doc_id_global;
	doc_id_global = doc_id;
	user_name = os.environ.get("USERNAME");
	user_full_name_sqlstr = """ SELECT * FROM [Mortgages].[xtr].[User_Details_View] WHERE CorpUserName = \'""" + str(user_name) + """';""";	
	cursor = connection.cursor();
	cursor.execute(user_full_name_sqlstr);
	user_info_list  = cursor.fetchall();
	if len(user_info_list) > 0:
		user_full_name = ' '.join(user_info_list[0][1:3]);
	else:
		user_full_name = user_name;

	global pdf_file_list_global;
	for item in pdf_file_list_global:
		# print '';
		# print item.Doc_ID;
		if item.Doc_ID == int(doc_id):
			global fields_for_selected_PDF_list_global;
			fields_for_selected_PDF_list = get_all_fields_by_doc_id(int(doc_id));
			fields_for_selected_PDF_list_global = fields_for_selected_PDF_list;
			lockup_pdf_file(doc_id);

			number_of_items = len(list(fields_for_selected_PDF_list));
			if number_of_items == 0:
				lockup_sqlstr = """IF NOT EXISTS (SELECT * FROM [xtr].[UI_Doc_User_Status] WHERE [Doc_ID] = """ + str(doc_id) + """)""";
				lockup_sqlstr = lockup_sqlstr + """INSERT INTO [xtr].[UI_Doc_User_Status] VALUES(""" + str(doc_id) + """, \' """  + user_full_name + """ \' , GETDATE(), \'Processed\', 0 ); """ ;
				cursor = connection.cursor();
				cursor.execute(lockup_sqlstr);
				transaction.commit(); 


			from Front_End_Process import restructure_pdf_name;
			ori_file_name = restructure_pdf_name(item.PDF_File_Name);
			page_pic_list = get_all_page_pic_by_doc_id(doc_id);				
			return render(request, 'FieldView/selectedpdfinfo.html',{'doc_id':int(doc_id), 'original_file_name': ori_file_name,'selected_pdf_obj': item, 'fields_for_selected_PDF_list': fields_for_selected_PDF_list, 'number_of_items': number_of_items})

def release_file(request):
	doc_id = doc_id_global;
	number_of_items = int(request.GET.get('number_of_items'));
	user_name = os.environ.get("USERNAME");
	user_full_name_sqlstr = """ SELECT * FROM [Mortgages].[xtr].[User_Details_View] WHERE CorpUserName = \'""" + str(user_name) + """\';""";	
	cursor = connection.cursor();
	cursor.execute(user_full_name_sqlstr);
	user_info_list  = cursor.fetchall();
	if len(user_info_list) > 0:
		user_full_name = ' '.join(user_info_list[0][1:3]);
	else:
		user_full_name = user_name;
	# print user_full_name;
	# print '================================================================================';
	# print doc_id, number_of_items;
	# print '================================================================================';

	update_lockup_info_sqlstr = "";
	if number_of_items==0:
		update_lockup_info_sqlstr = """UPDATE [xtr].[UI_Doc_User_Status] SET [Current_Status] = 'Processed', [Number_Of_Items] = 0 WHERE [Doc_ID] = """ + str(doc_id) + """;""";
	else:
		update_lockup_info_sqlstr = 'UPDATE [xtr].[UI_Doc_User_Status] SET ' ;
		update_lockup_info_sqlstr = update_lockup_info_sqlstr + '[Doc_ID] = \'' + str(doc_id) + '\' ,';
		update_lockup_info_sqlstr = update_lockup_info_sqlstr + '[Login_User_Name] = \'' + str(user_full_name) + '\',';
		update_lockup_info_sqlstr = update_lockup_info_sqlstr + '[Current_Status] = \'Processing\', ';
		update_lockup_info_sqlstr = update_lockup_info_sqlstr + '[Number_Of_Items] = ' + str(number_of_items) + ', ';	
		update_lockup_info_sqlstr = update_lockup_info_sqlstr + '[QC_Start_Time] = GETDATE() WHERE ';
		update_lockup_info_sqlstr = update_lockup_info_sqlstr + '[Doc_ID] = ' + str(doc_id);
		update_lockup_info_sqlstr = update_lockup_info_sqlstr + ' IF @@ROWCOUNT=0 ' + 'INSERT INTO [xtr].[UI_Doc_User_Status] VALUES (';
		update_lockup_info_sqlstr = update_lockup_info_sqlstr + str(doc_id) + ', \'' \
									+ str(user_full_name) + '\', GETDATE(), \'Processing\' , ' + str(number_of_items) + ');';

	cursor = connection.cursor();
	cursor.execute(update_lockup_info_sqlstr);
	transaction.commit();
	return;


def ajax_highlight(request, field_value_id):
	print 'HEHEHEHEHEH?';
	print field_value_id;
	print '';
	print '--------------';
	global fields_for_selected_PDF_list_global;

	for item in fields_for_selected_PDF_list_global:
		# print item.Field_Value_ID;
		if item.Field_Value_ID == int(field_value_id) and item.Doc_Page_Pic_ID != None:
			# print item.Doc_Page_Pic_ID;
			# print item.Pos_Minpoint_X,item.Pos_Minpoint_Y,item.Pos_Maxpoint_X,item.Pos_Maxpoint_Y;
			global page_pic_list_global;
			for page_pic in page_pic_list_global:
				if page_pic.Doc_Page_Pic_ID == item.Doc_Page_Pic_ID:
					from Show_highlight_Pic import draw_and_show_pic_without_dbquery;
					page_pic_bin = page_pic.Doc_Page_Pic_Bin;
					minpoint_X = item.Pos_Minpoint_X;
					minpoint_Y = item.Pos_Minpoint_Y;
					maxpoint_X = item.Pos_Maxpoint_X;
					maxpoint_Y = item.Pos_Maxpoint_Y;
					rotation_degree = item.Doc_Pic_Rotation_Degree;
					# print minpoint_X, minpoint_Y, maxpoint_X, maxpoint_Y, rotation_degree;
					binpic = draw_and_show_pic_without_dbquery(int(field_value_id),page_pic_bin, minpoint_X, minpoint_Y, maxpoint_X, maxpoint_Y, rotation_degree);
					pic_list = [];
				 	pic_list.append({"binpic" : binpic});
				 	pic_json = json.dumps(pic_list);
				 	response = HttpResponse();
				 	response['Content-Type'] = "text/javascript";
				 	response.write(pic_json);
				 	print 'hehe!';
				 	return response;


		if item.Field_Value_ID == int(field_value_id) and item.Doc_Page_Pic_ID == None and int(item.Pos_Minpoint_X) > 60 and int(item.Pos_Minpoint_Y) > 60:
			# print item.Doc_Page_Pic_ID;
			# print type(item.Doc_Page_Pic_ID);
			# print 'WAHR!?';
			from Show_highlight_Pic import show_special_pic;
			binpic = show_special_pic(int(field_value_id));	
			pic_list = [];
		 	pic_list.append({"binpic" : binpic});
		 	pic_json = json.dumps(pic_list);
		 	response = HttpResponse();
		 	response['Content-Type'] = "text/javascript";
		 	response.write(pic_json);
		 	print 'hehe!';
		 	return response;		

		if item.Field_Value_ID == int(field_value_id) and item.Doc_Page_Pic_ID == None and int(item.Pos_Minpoint_X) != 0 and int(item.Pos_Minpoint_Y) != 0:
			from Show_highlight_Pic import draw_wals_merge_pics;
			# global doc_id_global;	
			binpic = draw_wals_merge_pics(field_value_id, doc_id_global, int(item.Pos_Minpoint_X), int(item.Pos_Minpoint_Y));
			pic_list = [];
		 	pic_list.append({"binpic" : binpic});
		 	pic_json = json.dumps(pic_list);
		 	response = HttpResponse();
		 	response['Content-Type'] = "text/javascript";
		 	response.write(pic_json);
		 	print 'hehe!';
		 	return response;		





def show_contact_info(request):
	return render(request,'FieldView/contactinfo.html');




def fix_field(request, field_value_id):
	# print field_value_id,'*****************************';
	# print request.GET.get('field_value_id');
	# print request.GET.get('check_flag');
	# print request.GET.get('comments');
	# print request.GET.get('calcrt_value');
	# print os.environ.get( "USERNAME" );
	user_name = os.environ.get("USERNAME");
	check_flag = request.GET.get('check_flag');
	comments = request.GET.get('comments');

	calcrt_value = request.GET.get('calcrt_value');

	if calcrt_value=="None":
		calcrt_value = "NULL";
		insert_fix_entry_sql_str = """INSERT INTO [xtr].[UI_User_Action_Hist] VALUES ( """ + str(field_value_id) + """, \'""" + str(user_name) + """\','Fixed', GETDATE(),""" + str(check_flag) + """,""" + str(calcrt_value) + """,'""" + str(comments) + """');"""
	else:
		insert_fix_entry_sql_str = """INSERT INTO [xtr].[UI_User_Action_Hist] VALUES ( """ + str(field_value_id) + """, \'""" + str(user_name) + """\','Fixed', GETDATE(),""" + str(check_flag) + """,'""" + str(calcrt_value) + """','""" + str(comments) + """');"""
	# print '';
	# print insert_fix_entry_sql_str;
	# print '';

	cursor = connection.cursor();
	cursor.execute(insert_fix_entry_sql_str);
	transaction.commit();

	response = HttpResponse();
	response['Content-Type'] = "text/javascript";
	info_list = [];
	info_list.append({"" : "test"});
	info_json = json.dumps(info_list);
	response.write(info_json);
	# print '&&&&';
	release_file(request);
	# print '****';
	return response;


def false_field(request, field_value_id):
	# print field_value_id,'*****************************';
	# print request.GET.get('field_value_id');
	# print request.GET.get('check_flag');
	# print request.GET.get('comments');
	# print request.GET.get('calcrt_value');
	# print os.environ.get( "USERNAME" );
	user_name = os.environ.get("USERNAME");
	check_flag = request.GET.get('check_flag');
	comments = request.GET.get('comments');
	calcrt_value = request.GET.get('calcrt_value');
	if calcrt_value=="None":
		calcrt_value = "NULL";
		insert_fix_entry_sql_str = """INSERT INTO [xtr].[UI_User_Action_Hist] VALUES ( """ + str(field_value_id) + """, \'""" + str(user_name) + """\','False', GETDATE(),""" + str(check_flag) + """,""" + str(calcrt_value) + """,'""" + str(comments) + """');"""
	else:
		insert_fix_entry_sql_str = """INSERT INTO [xtr].[UI_User_Action_Hist] VALUES ( """ + str(field_value_id) + """, \'""" + str(user_name) + """\','False', GETDATE(),""" + str(check_flag) + """,'""" + str(calcrt_value) + """','""" + str(comments) + """');"""
	# print '';
	# print insert_fix_entry_sql_str;
	# print '';
	from django.db import connection, transaction;
	cursor = connection.cursor();
	cursor.execute(insert_fix_entry_sql_str);
	transaction.commit();

	response = HttpResponse();
	response['Content-Type'] = "text/javascript";
	info_list = [];
	info_list.append({"" : "test"});
	info_json = json.dumps(info_list);
	response.write(info_json);
	release_file(request);
	return response;

