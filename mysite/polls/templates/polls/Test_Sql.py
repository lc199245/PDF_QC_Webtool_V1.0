from django.db import connection;

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT TOP 50 * FROM [xtr].[Doc_Field_Value]");
        row = cursor.fetchall()

    return row