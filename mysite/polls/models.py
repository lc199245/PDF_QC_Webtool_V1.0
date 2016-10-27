from __future__ import unicode_literals

from django.db import models

import datetime;

from django.utils import timezone;
from django.db import connection;


# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200);
	pub_date = models.DateTimeField('date published');


	def __str__(self):
		return self.question_text;


	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1);

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE);
	choice_text = models.CharField(max_length = 200);
	votes = models.IntegerField(default = 0);



	def __str__(self):
		return self.choice_text;

class Doc_Field_Value(models.Model):
	Field_Value_ID = models.IntegerField();
	Field_Name_ID = models.IntegerField();
	Field_Value = models.CharField(max_length=255);
	Field_Value_Is_Numeric = models.BooleanField();
	Calcrt_Value = models.CharField(max_length=255);
	Calcrt_ID = models.CharField(max_length=10);
	
	def get_test_field_values(self):
		with connection.cursor() as cursor:
			cursor.execute('SELECT TOP 100 * FROM [xtr].[Doc_Field_Value]');
			rows = cursor.fetchall();
		print '----------------------------------------------------';
		rows = list(rows);
		# print type(rows);
		for i in range(0, len(rows)):
			# print type(rows[i]);
			rows[i] = list(rows[i]);
			rows[i].append(str(rows[i][0]));

		return rows;


