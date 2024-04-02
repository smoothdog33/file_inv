import json
product_list = []
supplier_list = []   

def supplier_conv():

    with open("/Users/ayan/py_conv/supplier_profile.json","r") as file:
        for jsonObj in file:
            supplier_dictionary = json.loads(jsonObj)
            
            supplier_list.append(supplier_dictionary)
            a = (supplier_dictionary.get('supplier_id'))
            with open("/Users/ayan/py_conv/product.json","r") as file:
                for jsonObj in file:
                    product_dictionary = json.loads(jsonObj)
                    product_list.append(product_dictionary)
                    p = (product_dictionary.get('product_id'))

                    with open("/Users/ayan/py_conv/questions.json","r") as file:
                            for jsonObj in file:
                                question_dictionary = json.loads(jsonObj)
                                d = (question_dictionary.get('question_id'))
                                new_dict = {"supplier_1":a,"product_id":p,"question_id":d}
                                with open('supplier_conv.json', 'a') as f:     
                                            json.dump(new_dict, f)
                                            f.write('\n')


import psycopg2
import pandas
pd = pandas
def json_inserter(file_name,table_name):
        pgconn = psycopg2.connect(
        host= '0.0.0.0',
    user = 'postgres',
    password = 'mysecretpassword',
    database = 'inventory_managment',
    port = '5455')
        pgcursor = pgconn.cursor()
       
        df = pd.read_json (file_name,lines=True)
        from sqlalchemy import create_engine
        engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@0.0.0.0:5455/inventory_managment')
        print(engine)
        
        df.to_sql(table_name, engine, if_exists = 'append', index=False)
                                    

