
from ast import parse
import psycopg2
import platform
from first import file_inventory_creator
from first import json_inserter
from first import max_dates_func
import psycopg2
import pandas
import sys
import argparse

pd = pandas
parser = argparse.ArgumentParser()
parser.add_argument('file' , metavar = 'file' , type=str , help='enter file number')
args = parser.parse_args()
file_maker = args.file
g = (platform.uname())
source_system_id = g[0]+" "+ g[1]
print(source_system_id)
pgconn = psycopg2.connect(
    host= '0.0.0.0',
    user = 'postgres',
    password = 'mysecretpassword',
    database = 'postgres',
    port = '5455')
pgcursor = pgconn.cursor()
print(pgcursor.execute('select * from public."max_dates" where run_id in (select max(run_id) from public.max_dates where source_system_id=' + "'" + source_system_id + "') and source_system_id='" + source_system_id+"'" ) )  
result = pgcursor.fetchall()  
result_len = len(result)  
            

if result_len == 0 : 
    max_a_time= '1970-01-01 18:05:03.96823' 
    max_m_time= '1970-01-01 18:05:03.96823' 
    max_c_time= '1970-01-01 18:05:03.96823'   
    run_id= 1 
else:     
    max_a_time= result [0][1] 
    max_m_time= result [0][2] 
    max_c_time= result [0][3]  
    run_id= result [0][4]+ 1 
    print("c-date" + max_c_time)
print(run_id)
print(source_system_id)
file_inventory_creator('/users/ayan/pngwork/','/users/ayan/file_inventory/data/' + file_maker + '.json',max_a_time,max_m_time,max_c_time,run_id,source_system_id)

json_inserter('' + file_maker + '.json','file_inventory')

max_dates_func(str(run_id),source_system_id)
