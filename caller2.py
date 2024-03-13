from ast import parse
import psycopg2
import platform
from supplier_convert2 import supplier_conv 
from supplier_convert2 import json_inserter

import psycopg2
import pandas
import sys
import argparse

pd = pandas
parser = argparse.ArgumentParser()
args = parser.parse_args()
g = (platform.uname())
source_system_id = g[0]+" "+ g[1]
print (source_system_id)
pgconn = psycopg2.connect(
    host= '0.0.0.0',
    user = 'postgres',
    password = 'mysecretpassword',
    database = 'inventory_managment',
    port = '5455')
pgcursor = pgconn.cursor()

#supplier_conv()
#product_func()
json_inserter('supplier_conv.json','convert_') 
#supplier_profile()

#json_inserter('supplier_profile.json','profile_') 

#supplier_questions()

#json_inserter('warehouse_profile.json','warehouse_profile')

