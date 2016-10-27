from PIL import Image;
from PIL import ImageDraw;
import PIL;
from PIL import ImageFont;
import os;
import sys;
from django.db import connection;
import pyodbc;
import base64;
import io;
import cStringIO;

def execute_pure_query_to_pddf(query_sql):   
    try:
        result_df = pd.read_sql(query_sql, global_db_conn);
        return result_df;
    except:
        e = sys.exc_info();
        print '';
        print e;
        print ' SQL:  ', query_sql;
    

def show_special_pic(field_value_id):
    page_pic_sqlstr = 'SELECT * FROM [xtr].[Doc_Special_Pic] WHERE [Field_Value_ID] = ' + str(field_value_id) + ';';
    with connection.cursor() as cursor:
        cursor.execute(page_pic_sqlstr);
        page_pic_df = cursor.fetchall();

    page_pic_df = list(page_pic_df);

    if len(page_pic_df) > 0:
        page_pic_df[0] = list(page_pic_df[0]);
        ablob = page_pic_df[0][1];
        im = Image.open(io.BytesIO(ablob));
        buffer = cStringIO.StringIO();
        im.save(buffer, format="JPEG");
        binpic = base64.b64encode(buffer.getvalue());
        return binpic;


def draw_and_show_pic_without_dbquery(field_value_id, page_pic_bin, minpoint_X, minpoint_Y, maxpoint_X, maxpoint_Y, rotation_degree):
    ablob = page_pic_bin;
    im = Image.open(io.BytesIO(ablob));
    im = im.convert('RGB');
    print '-';
    x, y =  im.size;
    draw = ImageDraw.Draw(im);
    draw.line(((minpoint_X,minpoint_Y),(minpoint_X,maxpoint_Y)),width = 4,fill='red');
    draw.line(((minpoint_X,maxpoint_Y),(maxpoint_X,maxpoint_Y)),width = 4,fill='red');
    draw.line(((maxpoint_X,maxpoint_Y),(maxpoint_X,minpoint_Y)),width = 4,fill='red');
    draw.line(((maxpoint_X,minpoint_Y),(minpoint_X,minpoint_Y)),width = 4,fill='red');  
    im = im.rotate(rotation_degree,expand=1);
    # print type(im);
    print '-';
    buffer = cStringIO.StringIO();
    print '-';
    im.save(buffer, format="JPEG");
    binpic = base64.b64encode(buffer.getvalue());
    return binpic;


def draw_wals_merge_pics(field_value_id, doc_id, start_page_number, end_page_number):
    merge_img_file_list = [];
    for i in range(start_page_number, end_page_number+1):
        page_pic_sqlstr = 'SELECT * FROM [xtr].[Doc_Page_Pic] WHERE [Doc_ID] = ' + str(doc_id) + ' and [Doc_Page_Pic_PageNum] = ' + str(i) + '; ';
        with connection.cursor() as cursor:
            cursor.execute(page_pic_sqlstr);
            page_pic_df = cursor.fetchall();
            
        page_pic_df = list(page_pic_df);
        if len(page_pic_df) > 0:
            page_pic_df[0] = list(page_pic_df[0]);
            ablob = page_pic_df[0][2];
            im = Image.open(io.BytesIO(ablob));
            im = im.convert('RGB');
            x, y =  im.size;
            if page_pic_df[0][4] == 1:
                im = im.rotate(270,expand=1); 
            buffer = cStringIO.StringIO();
            im.save(buffer, format="JPEG");              
            merge_img_file_list.append(buffer);
    
    images = map(Image.open,merge_img_file_list);
    widths, heights = zip(*(i.size for i in images));
    max_width = max(widths);
    total_height = sum(heights);

    new_im = Image.new('RGB', (max_width, total_height));

    y_offset = 0;

    for im in images:
        new_im.paste(im, (0, y_offset));
        y_offset += im.size[1];

    # new_im.save('test_merge.jpg');  
    # os.startfile('test_merge.jpg'); 
    print '-BELLAAAAAAAAAAAAAAAAAAAA';
    buffer = cStringIO.StringIO();
    print '-';
    new_im.save(buffer, format="JPEG");
    binpic = base64.b64encode(buffer.getvalue());
    return binpic;        


