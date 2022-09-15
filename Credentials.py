'''
<DocString>
Purpose: For any DB Connection or Login Credentials Requires Username and Password,
         the following class extracts password and username from an external file 
         and assign it as two data members of a Credential Class
         Two member functions that read the file to assign them to the members
         Also two Member functions that can be used to Prompt the User using the getpass Library in order to make the class
         Format of the Creds.txt is two lines with your credentials saved in a text file like so:
         
         EinsteinAlb  <--Username
         Emc2 <--Password
'''
class Credentials(object): 
 def retreivePassword() :
  with open('Creds.txt') as file :
   contents = [next(file) for x in range(2)]
  password = contents[1]
  return password
 def retreiveUsername() :
  with open('Creds.txt') as file :
   contents = [next(file) for x in range(2)]
  username = contents[0].strip('\n')
  return username
 #Function that pushes to the User to Input their Login Credentials
 def getPassword(self) :
  try :
   import getpass
   self.password = getpass.getpass(prompt = "Please enter your password: ")
  except Exception as error :
   print("Error", error)
  else :
   print('Password has been stored')
  #return password
 
 def getUsername(self) :
  try :
   import getpass
   self.username = getpass.getuser()
  except Exception as error :
   print("Error", error)
  else :
   print('Username has been stored')
  #return userName  
 def updateCredentials(self):
  contents = [self.username,"\n" + self.password] 
  with open('Creds.txt', 'w') as file :
   for i in range(0, len(contents)) :
    file.write(contents[i])
  #Constructor that auto assigns 
 def __init__(self, password = retreivePassword() , username = retreiveUsername()):
   self.password = password
   self.username = username
