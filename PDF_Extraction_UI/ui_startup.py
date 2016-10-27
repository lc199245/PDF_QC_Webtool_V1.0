from django.db import connection, transaction;


def clean_file_lockup_info():
	clean_file_lockup_info_sqlstr = """DELETE FROM [xtr].[Doc_Lockup_Info] WHERE [xtr].[Doc_Lockup_Info].[Current_Status]='Processing';""";
	cursor = connection.cursor();
	cursor.execute(clean_file_lockup_info_sqlstr);
	transaction.commit();
