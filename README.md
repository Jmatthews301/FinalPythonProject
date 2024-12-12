# FinalPythonProject
# Password Manager

## Overview

Hey there! Welcome to my Password Manager project. This is a simple command-line tool written in Python that allows you to manage your passwords for different services. You can add, retrieve, update, and delete passwords stored in a CSV file. 

**Disclaimer:** This project is for educational purposes only! Storing passwords in plain text like this is a terrible idea from a security standpoint. Please do not use this in real life!

## Features

- Add new passwords for different services.
- Retrieve passwords for specific services.
- Update existing passwords.
- Delete passwords you no longer need.
- All data is stored in a CSV file (`passwords.csv`).

## Getting Started

### Prerequisites

To run this project, you'll need:

- Python 3.x installed on your machine.
- Basic knowledge of using the command line.

### Installation

1. **Clone the Repository**: First, clone this repository to your local machine using Git Bash or any terminal:

   ```bash
   git clone https://github.com/Jmatthews301/FinalPythonProject.git
Navigate to the Project Directory:
bash
cd FinalPythonProject
Check Python Installation: Make sure Python is installed by running:
bash
python --version
Usage
You can run the password manager script from the command line with various commands. Here’s how to use it:
1. Adding a Password
To add a new password, use the -a option followed by the service name and the password:
bash
python password_manager.py -a <service_name> <your_password>
Example:
bash
python password_manager.py -a DaytonFreight Pa$$w0rd
2. Retrieving a Password
To retrieve a password for a specific service, use the -r option:
bash
python password_manager.py -r <service_name>
Example:
bash
python password_manager.py -r DaytonFrieght
3. Updating a Password
If you need to update an existing password, use the -u option:
bash
python password_manager.py -u <service_name> <new_password>
Example:
bash
python password_manager.py -u DaytonFrieght newpassword456
4. Deleting a Password
To delete a password for a service, use the -d option:
bash
python password_manager.py -d <service_name>
Example:
bash
python password_manager.py -d DaytonFreight
5. Getting (Viewing) a Password
To get (view) a password for a service, you can use the -g option:
bash
python password_manager.py -g <service_name>
Example:
bash
python password_manager.py -g DaytonFreight
Viewing Stored Passwords
After running these commands, you can check the contents of passwords.csv to see if your passwords are being stored correctly:
bash
cat passwords.csv
Important Notes
Security Warning: This implementation stores passwords in plain text within a CSV file. This is not secure and should never be used in the real world or with real accounts! It's just for learning purposes.
CSV File Structure: The CSV file will have two columns: service and password. Make sure to keep it organized!
Conclusion
