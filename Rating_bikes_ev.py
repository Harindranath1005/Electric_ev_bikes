import os
from dotenv import load_dotenv, dotenv_values
import streamlit as st
import mysql.connector
import pandas as pd
#connection to database using .env variables
load_dotenv()

DB_HOST = st.secrets['DB_HOST']
DB_PORT = st.secrets['DB_PORT']
DB_NAME = st.secrets['DB_NAME']
DB_USER = st.secrets['DB_USER']
DB_PASSWORD = st.secrets['DB_PASSWORD']
mydb = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

mycursor=mydb.cursor()
mycursor.execute("select * from electric_bikes_csv")
#to get column name and values from the table we follow below syntax
rows = mycursor.fetchall()
columns = mycursor.column_names
df=pd.DataFrame(rows,columns=columns)

#Normalization of parameters using min max scaling
#adding normalized values to the data frame using apply method
l=[
    'Price',
    'battery_capacity_kwh',
    'Power torque',
    'riding_range_km',
    'top_speed_kmph',
    'charging_time_0_100_hrs',
]
def scaling(x,col):
  min_val=df[col].min()
  max_val=df[col].max()
  return (x-min_val)/(max_val-min_val)

for i in l:
  df[i+"_scaledvalue"]=df[i].apply(lambda x:scaling(x,i))

#Reversing the scaled values for price and charaging time
# since user prefers smaller values for these parameters
def reverse_scaling(x):
  return 1-x

reverse_scaling_list=[
    "Price_scaledvalue",
    "charging_time_0_100_hrs_scaledvalue"
]

for i in reverse_scaling_list:
  df[i+"_reverse_scaling"]=df[i].apply(lambda x:reverse_scaling(x))
#collecting user preferences
Preference_list=["Price","Charging time","Torque","Range","Top speed","Battery Capacity"]
demo_list=["Price","Charging time","Torque","Range","Top speed","Battery Capacity"]
EV_List=["Price_scaledvalue_reverse_scaling",
         "charging_time_0_100_hrs_scaledvalue_reverse_scaling",
         "Power torque_scaledvalue",
         "riding_range_km_scaledvalue",
         "top_speed_kmph_scaledvalue",
         "battery_capacity_kwh_scaledvalue"]
user_choice=[]
def removing_from_list(x):
  Preference_list.remove(x)
  user_choice.append(x)
col1, col2 = st.columns(2)
with col1:
  First_pref=st.selectbox("Select your first preference",Preference_list)
  removing_from_list(First_pref)
  second_pref=st.selectbox("Select your second preference",Preference_list)
  removing_from_list(second_pref)
with col2:
  Third_pref=st.selectbox("Select your third preference",Preference_list)
  removing_from_list(Third_pref)
  fourth_pref=st.selectbox("Select your fourth preference",Preference_list)
  removing_from_list(fourth_pref)

for i in range(len(Preference_list)):
  user_choice.append(Preference_list[i])

#st.write( user_choice[0])
# 
df["Rating"]=round(((df[EV_List[demo_list.index(user_choice[0])]]*0.25)
+(df[EV_List[demo_list.index(user_choice[1])]]*0.25)
+(df[EV_List[demo_list.index(user_choice[2])]]*0.2)
+(df[EV_List[demo_list.index(user_choice[3])]]*0.2)
+(df[EV_List[demo_list.index(user_choice[4])]]*0.05)
+(df[EV_List[demo_list.index(user_choice[5])]]*0.5))*10,1)

df=df.sort_values(["Rating"],ascending=False)
User_prefered_data=df[['Variant','Rating','Price','battery_capacity_kwh','Power torque', 'riding_range_km','top_speed_kmph','charging_time_0_100_hrs']].head().reset_index(drop=True).copy()
User_prefered_data.insert(0,"SNo",User_prefered_data.index+1)
st.dataframe(User_prefered_data,hide_index=True)
#function to print suggestion for user as per there input
def o_p_data(Sno,index):
  columns=['Variant','Rating','Price','battery_capacity_kwh','Power torque', 'riding_range_km','top_speed_kmph','charging_time_0_100_hrs']
  output_data=User_prefered_data.query(Sno)
  for i in columns:
    #data_frame_name.at[index_value, col_name]--> this is used get only value from
    #the particular column as per the index value mentioned so column name is excluded in output
    a=output_data.at[index,i] 
    st.write(i+"->",a)
#Giving suggestion to user
colm1,colm2,colm3,colm4,colm5=st.columns(5)
with colm1:
  st.write("First Suggestion")
  o_p_data("SNo==1",0)
with colm2:
  st.write("Seocnd Suggestion")
  o_p_data("SNo==2",1)
with colm3:
  st.write("Third Suggestion")
  o_p_data("SNo==3",2)
with colm4:
  st.write("Fourth Suggestion")
  o_p_data("SNo==4",3)
with colm5:
  st.write("Fifth Suggestion")
  o_p_data("SNo==5",4)
