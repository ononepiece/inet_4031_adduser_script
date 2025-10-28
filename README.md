# INET4031 Add Users Script and User List

## Program Description
This Python script automates the process of creating new user accounts on an Ubuntu system. Normally, a system administrator would manually use commands like adduser, passwd, and adduser <user> <group> for every user. This can be slow and prone to errors, especially when managing a large number of users.  

The **Add Users Script** makes this process faster by reading user data from a file (create-users.input) that lists usernames, passwords, names, and groups. The script then automatically executes the same Linux commands that an administrator would use — adding users, setting passwords, and assigning groups. This saves time and ensures consistency across systems.

---

## Program User Operation
The program reads user information from an input file and uses Linux commands to create accounts. It can be run in two ways:  
- **Dry Run Mode:** Shows which commands would run, without changing the system.  
- **Execution Mode:** Actually runs the commands to add users and assign groups.  

Before running, make the Python script executable:
bash
Before running, make the Python script executable:
bash
chmod +x create-users.py

Input File Format
The input file is just a list of users that need to be added. Each line in the file has five parts separated by colons. The order is as follows: username, password, last name, first name, and groups. The script reads each line and uses that information to create the users.


Command Execution
Before running the code, the Python file needs permission to run. You do that with the command chmod +x create-users.py. After that, the script can be run with ./create-users.py < create-users.input. The < symbol sends the list of users from the input file into the Python script so it can read them one by one.

Dry Run
A dry run means testing the code without actually adding any users. When you do a dry run, the script shows what commands would run, but it doesn’t make any real changes. 
