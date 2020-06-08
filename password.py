import random

def password(name):
    #code
    
     Upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
     lower_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
     
     numers=['0','1','2','3','4','5','6','7','8','9']
     special=['!','@','#','$','%','^','&','*','(',')','~','`']


     password=name+random.choice(Upper_case)+random.choice(lower_case)+random.choice(numers)+random.choice(special)
     
     if len(password)<8:
         print("Week paswword\nPassword should be atleast 8 char")
     else:
         print("strong password")

     return password

email=str(input("Enter the email Id"))
a=str(email[0:5])
print(password(a))


 
