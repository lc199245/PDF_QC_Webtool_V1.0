from __future__ import unicode_literals

from django.db import models

import datetime;

from django.utils import timezone;
from django.db import connection;


# Create your models here.
# class Doc_PDF(models.Model):
# 	Doc_ID = models.IntegerField(primary_key=True);
# 	Import_Date_Time = models.TimeField();
# 	URL = models.CharField(max_length=255);
# 	Agency_Name = models.CharField(max_length=255);
# 	PDF_File_Name = models.CharField(max_length=255);
# 	Doc_Type_ID = models.IntegerField();
# 	Doc_Version = models.CharField(max_length=255);


class Doc_PDF(models.Model):
	Doc_ID = models.IntegerField(primary_key=True);
	Agency_Name = models.CharField(max_length=255);
	Doc_Version = models.CharField(max_length=255);
	PDF_File_Name = models.CharField(max_length=255);
	Import_Date_Time = models.TimeField();
	Login_User_Name = models.CharField(max_length=255);
	QC_Start_Time = models.TimeField();
	Current_Status = models.CharField(max_length=255);
	Number_Of_Items = models.IntegerField();
	
	
	


	# def get_doc_pdf_all(self):
	# 	with connection.cursor() as cursor:
	# 		cursor.execute('SELECT * FROM [xtr].[Doc_PDF] ORDER BY [Doc_ID] DESC');
	# 		rows = cursor.fetchall();
	# 	print '----------------------------------------------------';
	# 	rows = list(rows);
	# 	result_rows = [];
	# 	for i in range(0, len(rows)):
	# 		rows[i] = list(rows[i]);
	# 		temp_row = [];
	# 		temp_row.append(rows[i][0]);
	# 		temp_row.append(rows[i][1]);
	# 		temp_row.append(rows[i][3]);
	# 		temp_row.append(rows[i][4]);
	# 		temp_row.append(rows[i][7]);
	# 		result_rows.append(temp_row);
	# 		print temp_row;
	# 	return result_rows;

class Doc_Field_Value(models.Model):
	Field_Value_ID = models.IntegerField(primary_key=True);
	Field_Name_ID = models.IntegerField();
	Field_Value = models.CharField(max_length=255);
	Field_value_Is_Numeric = models.BooleanField();
	Calcrt_Value = models.CharField(max_length=255);
	Calcrt_Value_Sent_DT = models.TimeField();
	Calcrt_ID = models.CharField(max_length=255);
	Check_Flag = models.IntegerField();
	Doc_Field_Pic_Info_ID = models.IntegerField();
	Doc_Page_Pic_ID = models.IntegerField();
	Doc_Pic_Rotation_Degree = models.IntegerField();
	Pos_Minpoint_X = models.FloatField();
	Pos_Minpoint_Y = models.FloatField();
	Pos_Maxpoint_X = models.FloatField();
	Pos_Maxpoint_Y = models.FloatField();
	Tranche_ID = models.IntegerField();
	Deal_ID = models.IntegerField();
	Tranche_Name = models.CharField(max_length=255);
	Cusip = models.CharField(max_length=255);



class Doc_Page_Pic(models.Model):
	Doc_Page_Pic_ID = models.IntegerField(primary_key=True);
	Doc_Page_Pic_PageNum = models.IntegerField();
	Doc_Page_Pic_Bin = models.CharField(max_length=255);
	Doc_ID = models.IntegerField();
	Is_Vertical = models.BooleanField();

class User_Details_View(models.Model):
	User_Details_View_ID = models.IntegerField(primary_key=True);
	UUID = models.CharField(max_length=20);
	First_Name = models.CharField(max_length=20);
	Last_Name = models.CharField(max_length=20);
	Corp_User_Name = models.CharField(max_length=20);


class Doc_Lockup_Info(models.Model):
	Doc_Lockup_Info_ID = models.IntegerField(primary_key=True);
	Doc_ID = models.IntegerField();
	Login_User_Name = models.CharField(max_length=50);
	QC_Start_Time = models.TimeField();
	Current_Status = models.CharField(max_length=10);