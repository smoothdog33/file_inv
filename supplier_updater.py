import json
import os
import pandas as pd
import datetime
from datetime import datetime
import psycopg2  
from faker import Faker
fake = Faker()


                        
                                          

pgconn = psycopg2.connect(
        host= '0.0.0.0',
    user = 'postgres',
    password = 'mysecretpassword',
    database = 'inventory_managment',
    port = '5455')
pgcursor = pgconn.cursor()
pgcursor.execute('select responses_id from public."responses_from_supplier"')
result = pgcursor.fetchall()     
#supplier_address= result [0][1]
print(result.count(1))
i=1
Faker.seed(0)
for r in result:
    i=i+1
    print(i)
    print(result[i])
    pgcursor1 = pgconn.cursor()
    can_supply_test = fake.boolean(chance_of_getting_true=50)
    sql = "INSERT INTO public.responses_from_supplier(supplier_address, supplier_contact, supplier_company, product_name, product_discription, question, supplier_id, product_id, cost, price, question_id) VALUES ('" + supplier_address + "','" + supplier_contact + "','" + supplier_company + "','" + product_name +"','"+ product_discription +"','" + question +"','"+ str(supplier_id) +"','" + str(product_id)+"','"+ str(cost) + "','" + str(price) + "','"+ str(question_id) + "');"
    sql = "UPDATE public.responses_from_supplier SET can_supply="can_supply_test", offer_price="offer_price;"              

    #in this forloop  we are going to use the reswponse id to update the table  and set the offer price and can supply to some randomm responses     
    
    
    #write another sql statement that will update the same table and set those 2 columns with random values
    # go make another create script for update sql
    # after i have the update sql reday in python execte the sql in that forloop
#max_m_time= result [0][2]     
##max_c_time= result [0][3]   
#run_id= result [0][4] 
                             
                            
        
                                    
                        
