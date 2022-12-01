'''DocString -

Purpose - Showcase Useful Python Functions and Libraries used for ETL Process

'''

import cx_Oracle
import os
#Creating a Credentials Object!
from Credentials import Credentials
from textwrap import dedent
import oracledb
oracledb.init_oracle_client(lib_dir="C:\Oracle\instantclient_21_3")
import pandas as pd

#Specify your Oracle Db Connection Information
dsn = cx_Oracle.makedsn(hostname, port, service_name);




#Function to send an Email
def send_email(message) :
#Send an Email utilize the Win32com library to access Outlook
 import win32com.client
 outlook = win32com.client.Dispatch('outlook.application')
 mail = outlook.CreateItem(0)
 #Creating a Mailing List for Multiple Users or Clients
 mail.To = ";".join(['example1@gmail.com','example2@gmail.com'])
 mail.Subject = 'Python Process - Description Here'
 mail.HTMLBody = '<h3>Add Some Text here</h3>'
#mail.Attachments.Add('c:\\sample.xlsx')

 mail.CC = 'Your Email Here'
 from datetime import datetime
 #Specifies information to be passed to the function especially for Data Related Counts and Numbers
 Stats = message
 disclaimer = '\n\n\nThis is an automated Email and is sent to whomever it may concern'
 developer_notes ='\nAdd some notes here for your self'
 
 mail.Body = "\n" + Stats + disclaimer + developer_notes
 mail.Send()

#Function that takes the name of the File as Input which then create a blank file and validate if the directory exists as well
def create_file(filename) :
#Use this to validate if a Directory or location already Exists
 import os
 #Creating a Date Stamp to keep track of when Something Runs
 from datetime import datetime
 time_stamp = datetime.now()
 stamp = str(time_stamp.year) + str(time_stamp.month) + str(time_stamp.day);
 file_name1 =  filename + stamp;
 path = 'C:\\PythonJobs\\Name of the Process or ETL here'+ stamp;
 #Checks if the Path already exists, if not you can push this variable to use Shell Scripting to Create the directory for you
 isExist = os.path.exists(path);
 try :
  if isExist :
   pass
  else :
   os.mkdir(path);
 except :
  print("Error: Creating Path Variable for Files");
  #Variable to include the path and file name with the file extension put in place
 final_file = path + '\\' + file_name1+ '.csv'
 #Create the File
 file = open(final_file,'w+')
 file.close()
 return final_file
 
 #Function that compliments the Create_file function above but will dump data from python for output to the file
 #Also takes Data (the information you wish to put inside the file
 #Please consult Pandas to_csv and other data output functions that may work for you
def data_dump(data,filename) :
 file = create_file(filename)
 #Creating the Headers of the File - Specify all the columns names
 contents = [('Column Name 1'),
             ('Column2 Name')
            ]
 data_new = data
 #Insert the headers into the data list to appended ot the created file
 data_new.insert(0, contents)
 print(data_new)
 #Csv Library
 import csv
 # opening the csv file in 'w+' mode
 file_t = open(file, 'a+', newline ='')
# writing the data into the file
 with file_t:    
    write = csv.writer(file_t)
    write.writerows(data_new)
 file_t.close();


 
def main() :
   
   
    from datetime import date,datetime, timedelta
    import datetime
   
    credentials = Credentials();
    password1 =  credentials.password; #Stores Password as a variable from External File
    username1 =  credentials.username; #Gets the Username
   
    conn = cx_Oracle.connect(user= username1, password= password1, dsn=dsn);
    cursor = conn.cursor();
   
    #Create Date Range to Pull Data from DB
    time_stamp = datetime.datetime.now()

    if time_stamp.day<10 :
     Today = '0' + str(time_stamp.day)
    else :
     Today = str(time_stamp.day )

    if time_stamp.month<10 :
     month = '0' + str(time_stamp.month)
    else :
     month = str(time_stamp.month)
    year = time_stamp.year

    startDt = str(time_stamp.year) + '-' + month + '-'+ '01'
    endDay = datetime.date(int(year),int(month)+1,1)- datetime.timedelta(days=1);
    endDt = str(endDay.year) + '-' + str(endDay.month) + '-' + str(endDay.day)

    print('Program starts on ' + startDt)

    print('Program Ends on ' + endDt)

  #Data Extraction -Paste your SQL Here to pull Data from Said DB
    sql = dedent('''
    select a.something
    from somethingTable a
    where dateColum in ('{startDt}' ,'{endDt}')
            '''.format(startDt =startDt, endDt = endDt));
             
    print(sql)
    #Execute the SQL over the db and be able to have the cursor connect to the results to be able to Fetch in the next step
    results = cursor.execute(sql1);
   
   
    #Store Data in Python
    data = results.fetchall();
    conn.close();
    #Data Extraction Finished
   
    #Put Data into a Dataframe in Pandas
    datatable = pd.DataFrame(data,columns = ['Column Names input here'], dtype = str)
    dataInsertionTuples = [tuple(x) for x in datatable.values]

   
    #print(data);
   
    #Example Pulling Contact Information for Marketing Campaign
    #Count of Total Records
    sql_stats = 'select count(distinct id) as Num_Recs from somethingTable'
    total_num = cursor.execute(sql_stats).fetchall();
   
    #Count of Total Emails
    sql_emails = 'select count(*) from somethingTable where trim(lower(email)) is not null'
    total_emails = cursor.execute(sql_emails).fetchall();
   
    #Count of Total Addresses
    sql_addr = 'select count(*) from somethingTable where trim(lower(address||city||country||postal_code)) is not null'
    total_addr = cursor1.execute(sql_addr).fetchall();
   
    #Count of Total Phones
    sql_phone = 'select count(*) from somethingTable where trim(lower(phone)) is not null'
    total_phone = cursor1.execute(sql_phone ).fetchall();
   
   #Sample how you can get counts from your data and push it to be displayed in your Email
    message = dedent('''Python Job for "Name of Data process " Data Extraction has been Completed and can be found in somethingTable table in AWA \nTotal Records {totalRecords}\nTotal Emails: {emails}
    \nTotal Addresses: {address}\nTotal Phones: {phone}'''.format(totalRecords = total_num[0][0], emails = total_emails[0][0], address = total_addr[0][0], phone = total_phone[0][0]));
    conn.commit(); #Commit Changes to Db
    conn.close(); #Close the DB Connection session
   
   
   
   
if __name__ == '__main__':
 main()
