# receives a directory where a user wants to create a new file and creates the file in that directory
# !/usr/bin/env python3

import os
import os.path
import csv
import pandas

"""
directory = input('Enter the name of directory you want to open: ')

filename = input('Enter the name of file: ')


def new_directory():
    if not os.path.isdir(directory):
        os.mkdir(directory)
        # else:
        # os.chdir(directory)

        os.chdir(directory)
        # with open(filename, 'w') as file:
        # pass
        # return os.listdir(os.getcwd())
        if not os.path.isfile(filename):
            file_open = open(filename)
            return file_open


print(open(filename, 'w'))
"""

# print(os.mkdir(directory))


"""
def read_employees(csv_file_location):
    with open('employee.csv') as file:
        employee_file = csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
        rows = csv.DictReader(file)

        employee_list = []
        for data in employee_file:
            employee_list.append(data)
    return employee_list


employee_list = read_employees('employee.csv')
print(employee_list)


def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Sick Days remaining'])
        department_data = {}
        for department_name in set(department_list):
            department_data[department_name] = department_list.count(department_name)
    return department_data


employee_list = read_employees('employee.csv')
dictionary = process_data(employee_list)
# print(process_data(employee_list))
df = pandas.read_csv('employee.csv')
print(df)


def write_report(dictionary, report_file):
    with open(report_file, "a") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()


write_report(dictionary, 'employee.csv')
"""

# new


# !/usr/bin/env python3

# Import libraries
import csv
import re


def contains_domain(address, domain):
    """Returns True if the email address contains the given domain,in the domain position, false if not."""
    domain_pattern = r'[\w\.-]+@' + domain + '$'
    if re.match(domain_pattern, address):
        return True

    return False


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in the received address."""

    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address


def main():
    """Processes the list of emails, replacing any instances of the old domain with the new domain."""
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    csv_file_location = 'user_emails.csv'
    report_file = '/Program' + '/updated_user_emails.csv'
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []
    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]
        for email_address in user_email_list:
            if contains_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                replaced_email = replace_domain(email_address, old_domain, new_domain)
                new_domain_email_list.append(replaced_email)
                email_key = ' ' + 'Email Address'
                email_index = user_data_list[0].index(email_key)
                for user in user_data_list[1:]:
                    for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
                        if user[email_index] == ' ' + old_domain:
                            user[email_index] = ' ' + new_domain
                f.close()
                with open(report_file, 'w+') as output_file:
                    writer = csv.writer(output_file)
                    writer.writerows(user_data_list)
                    output_file.close()

    main()
