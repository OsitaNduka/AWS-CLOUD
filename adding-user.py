'''
import os

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add: ")
        print(f"Use the username '{username}'? (Y/N)")
        confirm = input().upper()

    # Execute the sudo command to add the user
    os.system(f"sudo adduser {username}")

new_user()
'''
import os

def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ")
        print(f"Remove the user: '{username}'? (Y/N)")
        confirm = input().upper()

    # Execute the sudo command to delete the user and remove their home directory (-r)
    os.system(f"sudo userdel -r {username}")

remove_user()
 
 
