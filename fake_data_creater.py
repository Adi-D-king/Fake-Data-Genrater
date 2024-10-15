import pandas as pd
import numpy as np
import random as rd 
import seaborn as sns
from matplotlib import pyplot as plt
import city_state as cs
# from geopy.geocoders import Nominatim
from faker import Faker

import MySQLdb as db
conn =db.connect(user='root',password='Adity@4410',host='localhost',database='Aisect_dummy_data')
cursor = conn.cursor() # creating cursor
cursor.execute("use Aisect_dummy_data;")
print("Conection sucessfull")
print("using Aisect_dummy_data database !!")

# intinalizing faker
fake = Faker('en_IN')
# fake.seed(10)

# for creating random fake Phone_Number
def j():
    return rd.randint(0,9)
def number(n):
    str = ""
    lis = [j() for i in range(n)]
    for k in lis:
        n = "{}".format(k)
        str = str+n
    return str

#creating features
stud_det = {"Form_Number":[i for i in range(1,2001)],"First_name":[],"Last_name":[],
            "Mothers_full_name":[],"Fathers_full_name":[],
            "Gender":[rd.choice(["Male","Female"]) for i in range(1,2001)],
            "Category":[rd.choice(["GEN","SC","ST","OBC"]) for i in range(1,2001)],
            "Date_of_Birth":[fake.date_of_birth() for i in range(1,2001)],
            "Aadhar_Card_no":[number(12) for i in range(1,2001)],
            "Samagra_Id":[number(10) for i in range(1,2001)],
            "Place_of_Ressidence":[rd.choice(["Rural","Urban"]) for i in range(1,2001)],
            "Religion":[rd.choice(["Hindu","Sikh","Islam","christian"]) for i in range(1,2001)],
            "Prequalufing_Test":[rd.choice(["JEE","AJEE","CAT","MAT","Other"]) for i in range(1,2001)],
            "Score_in_Prequalufing_test":[rd.randint(250,750) for i in range(1,2001)],
            "STD_Code":[number(5) for i in range(1,2001)],
            "Telephone_No":["+91 "+number(10) for i in range(1,2001)],
            "Mobile_No":["+91 "+number(10) for i in range(1,2001)],
            "E_mail":[fake.email() for i in range(1,2001)],
            "Address":[fake.address() for i in range(1,2001)],
            "City":[],"State":[cs.state() for i in range(1,2001)],
            "Program_Type":[],"Courses_type":[]
            }

# Creating Fake data and inserting it
for i in range(1,2001):
    stud_det['First_name'].append(fake.first_name_male() if stud_det["Gender"][i-1]=="Male" else fake.first_name_female())
    last_name = fake.last_name()
    stud_det["Last_name"].append(last_name)
    stud_det["Mothers_full_name"].append(fake.first_name_female() + " " + last_name) 
    stud_det["Fathers_full_name"].append(fake.first_name_male() + " " + last_name) 
    stud_det["Program_Type"].append(rd.choice(["PG","UG","Diploma"]))
    if stud_det["Program_Type"][-1]== "PG":
        stud_det["Courses_type"].append(rd.choice(["M.tech","MCA","MBA"]))
    elif stud_det["Program_Type"][-1]== "UG":
        stud_det["Courses_type"].append(rd.choice(["B.tech","BCA","BBA"]))
    else:
        stud_det["Courses_type"].append(rd.choice(["Dp.CS","Dp.EC","Dp.EX","Dp.ME"]))
    stud_det["City"].append(cs.city(stud_det["State"][i-1]))
    

df = pd.DataFrame(stud_det)

df.to_excel("Main_Data.xlsx")



print(df.head(10))
for i in range(2000):
    str = '''insert into student_dummy_data(Form_Number, First_name, Last_name, 
    Mothers_full_name, Fathers_full_name, Gender, Category, Date_of_Birth, 
    Aadhar_Card_no, Samagra_Id, Place_of_Ressidence, Religion, Prequalufing_Test, 
    Score_in_Prequalufing_test, STD_Code, Telephone_No, Mobile_No, E_mail, Address, City, 
    State, Program_Type, Courses_type) values(
    {},'{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(stud_det['Form_Number'][i],
    stud_det['First_name'][i],stud_det['Last_name'][i],stud_det['Mothers_full_name'][i],stud_det['Fathers_full_name'][i],
    stud_det['Gender'][i],stud_det['Category'][i],stud_det['Date_of_Birth'][i],stud_det['Aadhar_Card_no'][i],stud_det['Samagra_Id'][i],
    stud_det['Place_of_Ressidence'][i],stud_det['Religion'][i],stud_det['Prequalufing_Test'][i],stud_det['Score_in_Prequalufing_test'][i],
    stud_det['STD_Code'][i],stud_det['Telephone_No'][i],stud_det['Mobile_No'][i],stud_det['E_mail'][i],stud_det['Address'][i],stud_det['City'][i],
    stud_det['State'][i],stud_det['Program_Type'][i],stud_det['Courses_type'][i])
    cursor.execute(str)
    conn.commit()