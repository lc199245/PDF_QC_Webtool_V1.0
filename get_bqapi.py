import bqapi as bq
import  json
import  csv
from email.header import UTF8




def get_bqapi_isin_data( id_Record_List ):

    in_Sec_List = []
    
    field_List = \
    [
        'ID_BB_GLOBAL',
        'NAME',
        'TICKER',
        'EXCH_CODE',
        'COMPOSITE_ID_BB_GLOBAL',
        'ID_BB_UNIQUE',
        'SECURITY_TYP',
        'MARKET_SECTOR_DES',
        'ID_BB_GLOBAL_SHARE_CLASS_LEVEL',
        'UNIQUE_ID_FUT_OPT'
    ]
    
    field_List_Map = \
    {
        'ID_BB_GLOBAL' : 'figi',
        'NAME'         : 'name',
        'TICKER'       : 'ticker',
        'EXCH_CODE'    : 'exchCode',
        'COMPOSITE_ID_BB_GLOBAL' : 'compositeFIGI',
        'ID_BB_UNIQUE' : 'uniqueID',
        'SECURITY_TYP' : 'securityType',
        'MARKET_SECTOR_DES' : 'marketSector',
        'ID_BB_GLOBAL_SHARE_CLASS_LEVEL' : 'shareClassFIGI',
        'UNIQUE_ID_FUT_OPT' : 'uniqueIDFutOpt'    
     }
    

    for id_Tuple in id_Record_List:
        id_Key_Value = id_Tuple[1]
    
        if 'ID_ISIN' in id_Key_Value['idType']:
            #print id_Key_Value['idType']
    
            if 'exchCode' in id_Key_Value.keys():
                sec =  '/ISIN/' + id_Key_Value['idValue'] +  ' ' + id_Key_Value['exchCode']
            else:
                sec =  '/ISIN/' + id_Key_Value['idValue']            
    
            in_Sec_List.append(sec)
                
    sess = bq.Session()
    
    out_List =  sess.get_data(in_Sec_List, field_List , ignore_errors=True, format=bq.dictionary)
    
    id_Data_List      = []
    id_Miss_Data_List = []
    idx = 0
    
    out_Dict = {}
    
    for each_Dict in out_List:         
               
        for each_Key in each_Dict:
              
            if each_Dict.keys()[0] == 'Security': 
                # id with missing data
                id_Miss_Data_List.append((id_Record_List[idx][0], id_Record_List[idx][1]))
            else:
                if each_Key != 'Security':                                   
                    out_Dict[ field_List_Map[each_Key] ] = each_Dict[each_Key]
        
        id_Data_List.append((id_Record_List[idx][0], out_Dict))
            
        idx += 1   
    
    return tuple( id_Miss_Data_List), tuple(id_Data_List)  

if __name__ == "__main__": 
    
    
    id_Record_List = []
    get_bqapi_isin_data( id_Record_List )

    '''
    ##### https://jonlabelle.com/snippets/view/python/json-to-csv
    output_csv_file='\\\\Corp.bloomberg.com\\ww-dfs\\All Offices\\Princeton\\Global Data\\Financial Data\\Common\\Mortgage Tech\\Dumps\\Ajay\\ajay_test.csv'
    input_json_file='\\\\Corp.bloomberg.com\\ww-dfs\\All Offices\\Princeton\\Global Data\\Financial Data\\Common\\Mortgage Tech\\Dumps\\Ajay\\STORM_Test2.json'

    json_data = []
    data = None
    write_header = True
    item_keys = []
 
    with open(input_json_file, "r") as json_file:
        json_data = json_file.read()
 
    try:
        data = json.loads(json_data)
    except Exception as e:
        raise e
 
    with open(output_csv_file, 'wb') as csv_file:
        writer = csv.writer(csv_file)
 
        for item in data:
            item_values = []
            for key in item:
                if write_header:
                    item_keys.append(key)
                    
 
                    
                value = item.get(key, '')
                if isinstance(value, StringTypes):
                    item_values.append(value.encode('utf-8'))
                else:
                    item_values.append(value)
                    
        
 
            if write_header:
                writer.writerow(item_keys)
                write_header = False
 
            writer.writerow(item_values)

    
    
    print 'okay'
    
    output_csv_file='\\\\Corp.bloomberg.com\\ww-dfs\\All Offices\\Princeton\\Global Data\\Financial Data\\Common\\Mortgage Tech\\Dumps\\Ajay\\ajay_test.csv'
    input_json_file='\\\\Corp.bloomberg.com\\ww-dfs\\All Offices\\Princeton\\Global Data\\Financial Data\\Common\\Mortgage Tech\\Dumps\\Ajay\\STORM_Test2.json'

    f = open(input_json_file)
    data = json.load(f)
    f.close()
    
    f=csv.writer(open(output_csv_file,'wb+'))
    
    for item in data:
        f.writerow([item['pk'], item['model']] + item['fields'].values())

    
    print 'Completed!'
    '''
