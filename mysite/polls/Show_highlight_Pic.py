from PIL import Image;
from PIL import ImageDraw;
import PIL;
from PIL import ImageFont;
import os;
import sys;
from django.db import connection;
import pyodbc;
import base64;

def execute_pure_query_to_pddf(query_sql):   
    try:
        result_df = pd.read_sql(query_sql, global_db_conn);
        return result_df;
    except:
        e = sys.exc_info();
        print '';
        print e;
        print ' SQL:  ', query_sql;


def draw_and_show_pic(field_value_id):
    highlighted_pic_info_sqlstr = 'SELECT * FROM [xtr].[Doc_Field_Pic_Info] WHERE [Doc_Field_Value_ID] = ' + str(field_value_id) + ';';
    # highlighed_pic_info_df = execute_pure_query_to_pddf(highlighted_pic_info_sqlstr);
    
    with connection.cursor() as cursor:
            cursor.execute(highlighted_pic_info_sqlstr);
            highlighed_pic_info_df = cursor.fetchall();

    highlighed_pic_info_df = list(highlighed_pic_info_df);

    if len(highlighed_pic_info_df) > 0 :
        highlighed_pic_info_df[0] = list(highlighed_pic_info_df[0]);
        doc_page_pic_id = highlighed_pic_info_df[0][1];
        doc_field_value_id = highlighed_pic_info_df[0][2];
        rotation_degree = highlighed_pic_info_df[0][3];
        minpoint_X = highlighed_pic_info_df[0][4];
        minpoint_Y = highlighed_pic_info_df[0][5];
        maxpoint_X = highlighed_pic_info_df[0][6];
        maxpoint_Y = highlighed_pic_info_df[0][7];

        if doc_page_pic_id == None:
            doc_page_pic_id = 0;

        page_pic_sqlstr = 'SELECT * FROM [xtr].[Doc_Page_Pic] WHERE [Doc_Page_Pic_ID] = ' + str(doc_page_pic_id) + ';';
        with connection.cursor() as cursor:
            cursor.execute(page_pic_sqlstr);
            page_pic_df = cursor.fetchall();

        page_pic_df = list(page_pic_df);

        if len(page_pic_df) > 0:
            page_pic_df[0] = list(page_pic_df[0]);
            ablob = page_pic_df[0][2];
            dir_path = os.path.dirname(os.path.realpath(__file__))
            # print dir_path;
            temp_jpg_file = dir_path + '\static\\TempPics\\' + str(field_value_id) +'_temp.jpg';
            print temp_jpg_file;
            with open(temp_jpg_file,'wb') as output_file:
                output_file.write(ablob);
            im = Image.open(temp_jpg_file);
            print im.mode;
            im = im.convert('RGB');
            print im.mode;
            x, y =  im.size;
            print im.size;
            draw = ImageDraw.Draw(im);
            draw.line(((minpoint_X,minpoint_Y),(minpoint_X,maxpoint_Y)),width = 4,fill='red');
            draw.line(((minpoint_X,maxpoint_Y),(maxpoint_X,maxpoint_Y)),width = 4,fill='red');
            draw.line(((maxpoint_X,maxpoint_Y),(maxpoint_X,minpoint_Y)),width = 4,fill='red');
            draw.line(((maxpoint_X,minpoint_Y),(minpoint_X,minpoint_Y)),width = 4,fill='red');  
            im = im.rotate(rotation_degree,expand=1);
            im.save(temp_jpg_file);  
            # os.startfile(temp_jpg_file);         
            # os.remove(temp_jpg_file);
            output_file.close();
            bindata = open(temp_jpg_file, 'rb').read();
            binparams = pyodbc.Binary(bindata)
            os.remove(temp_jpg_file);
            binpic = base64.b64encode(bindata);
            return binpic;


        else:
            print 'Nothing returned for this doc page id.';
            special_pic_sqlstr = 'SELECT * FROM [xtr].[Doc_Special_Pic] WHERE [Field_Value_ID] = ' + str(doc_field_value_id) + ' ;';
            special_pic_df = execute_pure_query_to_pddf(special_pic_sqlstr);
            if len(special_pic_sqlstr) > 0:
                ablob = special_pic_df.iloc[0]['Doc_Special_Pic_Bin'];
                temp_jpg_file = 'Pics\\' + str(field_value_id) +'.jpg';
                with open(temp_jpg_file,'wb') as output_file:
                    output_file.write(ablob);
                os.startfile(temp_jpg_file);
            else:
                print special_pic_sqlstr;
    else:
        print 'Nothing returned for this field value id.';        



def draw_and_show_pic_without_dbquery(field_value_id):
    highlighted_pic_info_sqlstr = 'SELECT * FROM [xtr].[Doc_Field_Pic_Info] WHERE [Doc_Field_Value_ID] = ' + str(field_value_id) + ';';
    # highlighed_pic_info_df = execute_pure_query_to_pddf(highlighted_pic_info_sqlstr);
    
    with connection.cursor() as cursor:
            cursor.execute(highlighted_pic_info_sqlstr);
            highlighed_pic_info_df = cursor.fetchall();

    highlighed_pic_info_df = list(highlighed_pic_info_df);

    if len(highlighed_pic_info_df) > 0 :
        highlighed_pic_info_df[0] = list(highlighed_pic_info_df[0]);
        doc_page_pic_id = highlighed_pic_info_df[0][1];
        doc_field_value_id = highlighed_pic_info_df[0][2];
        rotation_degree = highlighed_pic_info_df[0][3];
        minpoint_X = highlighed_pic_info_df[0][4];
        minpoint_Y = highlighed_pic_info_df[0][5];
        maxpoint_X = highlighed_pic_info_df[0][6];
        maxpoint_Y = highlighed_pic_info_df[0][7];

        if doc_page_pic_id == None:
            doc_page_pic_id = 0;

        page_pic_sqlstr = 'SELECT * FROM [xtr].[Doc_Page_Pic] WHERE [Doc_Page_Pic_ID] = ' + str(doc_page_pic_id) + ';';
        with connection.cursor() as cursor:
            cursor.execute(page_pic_sqlstr);
            page_pic_df = cursor.fetchall();

        page_pic_df = list(page_pic_df);

        if len(page_pic_df) > 0:
            page_pic_df[0] = list(page_pic_df[0]);
            ablob = page_pic_df[0][2];
            dir_path = os.path.dirname(os.path.realpath(__file__))
            # print dir_path;
            temp_jpg_file = dir_path + '\static\\TempPics\\' + str(field_value_id) +'_temp.jpg';
            print temp_jpg_file;
            with open(temp_jpg_file,'wb') as output_file:
                output_file.write(ablob);
            im = Image.open(temp_jpg_file);
            print im.mode;
            im = im.convert('RGB');
            print im.mode;
            x, y =  im.size;
            print im.size;
            draw = ImageDraw.Draw(im);
            draw.line(((minpoint_X,minpoint_Y),(minpoint_X,maxpoint_Y)),width = 4,fill='red');
            draw.line(((minpoint_X,maxpoint_Y),(maxpoint_X,maxpoint_Y)),width = 4,fill='red');
            draw.line(((maxpoint_X,maxpoint_Y),(maxpoint_X,minpoint_Y)),width = 4,fill='red');
            draw.line(((maxpoint_X,minpoint_Y),(minpoint_X,minpoint_Y)),width = 4,fill='red');  
            im = im.rotate(rotation_degree,expand=1);
            im.save(temp_jpg_file);  
            # os.startfile(temp_jpg_file);         
            # os.remove(temp_jpg_file);
            output_file.close();
            bindata = open(temp_jpg_file, 'rb').read();
            binparams = pyodbc.Binary(bindata)
            os.remove(temp_jpg_file);
            binpic = base64.b64encode(bindata);
            return binpic;


        else:
            print 'Nothing returned for this doc page id.';
            special_pic_sqlstr = 'SELECT * FROM [xtr].[Doc_Special_Pic] WHERE [Field_Value_ID] = ' + str(doc_field_value_id) + ' ;';
            special_pic_df = execute_pure_query_to_pddf(special_pic_sqlstr);
            if len(special_pic_sqlstr) > 0:
                ablob = special_pic_df.iloc[0]['Doc_Special_Pic_Bin'];
                temp_jpg_file = 'Pics\\' + str(field_value_id) +'.jpg';
                with open(temp_jpg_file,'wb') as output_file:
                    output_file.write(ablob);
                os.startfile(temp_jpg_file);
            else:
                print special_pic_sqlstr;
    else:
        print 'Nothing returned for this field value id.';        



