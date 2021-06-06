from database import *
from algorithm import *
from IOprocess import *
import os.path

conn = create_db_connection()

filepath = os.getcwd() #Gets the current working directory
filepath = os.chdir('uploads')

a = convertCSV('data.csv')
# b = list(a[0].keys())
# print(b[0])
jsonarray, exectime = selectionsort(a, 0, 'desc')
for i in jsonarray:
    print(i)


data = getdata(conn,10)
print(data)
# print(getLastId())