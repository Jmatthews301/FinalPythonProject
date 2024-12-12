import argparse
import csv
import os
import re
import random
import string

# Constants
CSV_FILE = 'passwords.csv'

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def add_password(service, password):
    """Add a new password to the CSV file."""
    if not is_valid_service_name(service):
        print("Invalid service name. Only alphanumeric characters and underscores are allowed.")
        return
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([service, password])
        print(f"Password for {service} added.")

def retrieve_password(service):
    """Retrieve a password for a given service."""
    if not os.path.exists(CSV_FILE):
        print("No passwords stored.")
        return None
    
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == service:
                return row[1]
    print("Service not found.")
    return None

def update_password(service, new_password):
    """Update an existing password."""
    rows = []
    found = False
    
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        for i, row in enumerate(rows):
            if row[0] == service:
                rows[i][1] = new_password
                found = True

    if found:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Password for {service} updated.")
    else:
        print("Service not found.")

def delete_password(service):
    """Delete a password for a given service."""
    rows = []
    
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        rows = [row for row in rows if row[0] != service]

        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Password for {service} deleted.")
    else:
        print("No passwords stored.")

def is_valid_service_name(service):
    """Validate the service name using a regular expression."""
    pattern = r'^[a-zA-Z0-9_]+$'
    return re.match(pattern, service) is not None

def main():
    parser = argparse.ArgumentParser(description="Password Manager")
    
    parser.add_argument('-a', '--add', nargs=2, metavar=('SERVICE', 'PASSWORD'), help="Add a new password")
    parser.add_argument('-r', '--retrieve', metavar='SERVICE', help="Retrieve a password")
    parser.add_argument('-u', '--update', nargs=2, metavar=('SERVICE', 'NEW_PASSWORD'), help="Update an existing password")
    parser.add_argument('-d', '--delete', metavar='SERVICE', help="Delete a password")
    parser.add_argument('-g', '--generate', metavar='SERVICE', help="Generate a random password for a service")

    args = parser.parse_args()

    if args.add:
        service, password = args.add
        add_password(service, password)
    
    elif args.retrieve:
        service = args.retrieve
        password = retrieve_password(service)
        if password:
            print(f"Password for {service}: {password}")
    
    elif args.update:
        service, new_password = args.update
        update_password(service, new_password)

    elif args.delete:
        service = args.delete
        delete_password(service)

    elif args.generate:
        service = args.generate
        new_password = generate_password()
        add_password(service, new_password)
        print(f"Generated password for {service}: {new_password}")

if __name__ == "__main__":
    main()
