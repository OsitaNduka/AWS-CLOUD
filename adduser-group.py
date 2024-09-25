import os
import subprocess

def add_user_to_group():
    # Get the username to add to groups
    username = input("Enter the name of the user that you want to add to a group: ")

    # Get the list of all available groups on the system
    available_groups = subprocess.Popen('cut -d: -f1 /etc/group', shell=True, stdout=subprocess.PIPE).communicate()[0]
    available_groups = available_groups.decode('utf-8')

    # Display the available groups to the user
    print("The available groups are:\n" + available_groups)

    # Get the list of groups to add the user to
    print("Enter a list of groups to add the user to.")
    print("The list should be separated by spaces, for example:\n group1 group2 group3")
    chosen_groups = input("Groups: ")

    # Add the user to the chosen groups using the 'usermod' command
    os.system(f"sudo usermod -a -G {chosen_groups} {username}")

    print(f"User '{username}' has been added to the following groups: {chosen_groups}")

# Run the function
add_user_to_group()
