import os


# Define a list of default packages
defaultPackages = "package1 package2 package3"

def install_or_remove_packages():
    iOrR = ""
    # Loop until the user selects either install or remove
    while iOrR != "I" and iOrR != "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR = input().upper()
    
    if iOrR == "I":
        action = "install"
    elif iOrR == "R":
        action = "remove"

    # Ask for the list of packages to install/remove
    print(f"Enter a list of packages to {action}.")
    print("The list should be separated by spaces, for example:")
    print(" package1 package2 package3")
    print(f"Otherwise, input 'default' to {action} the default packages listed in this program.")
    
    packages = input().lower()

    # Use default packages if user types 'default'
    if packages == "default":
        packages = defaultPackages
    
    # Install packages
    if action == "install":
        os.system(f"sudo apt-get install {packages}")
    
    # Remove packages
    elif action == "remove":
        while True:
            # Ask if the user wants to purge files after removal
            print("Purge files after removing? (Y/N)")
            choice = input().upper()
            if choice == "Y":
                os.system(f"sudo apt-get --purge remove {packages}")
                break
            elif choice == "N":
                os.system(f"sudo apt-get remove {packages}")
                break
        # Perform automatic removal of unnecessary dependencies
        os.system("sudo apt-get autoremove")

# Function to clean the environment
def clean_environment():
    os.system("sudo apt-get autoremove")
    os.system("sudo apt-get autoclean")

# Call the install/remove packages function
install_or_remove_packages()
