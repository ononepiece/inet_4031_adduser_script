# INET4031
# Hayat
# 10/27/25
#!/usr/bin/python3

import os
import re
import sys

def main():
    for line in sys.stdin:

        # Check if the line starts with '#' which means it's just a comment line to skip.
        match = re.match("^#",line)

        # Split the input line into separate fields based on the ":" format.
        fields = line.strip().split(':')

        # Skip lines that are comments or do not have exactly 5 fields of data.
        if match or len(fields) != 5:
            continue

        # Store username and password, and format the full name into the GECOS field.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split group information  in case multiple groups are assigned.
        groups = fields[4].split(',')

        # Display which account is being created.
        print("==> Creating account for %s..." % (username))

        # Create the account with no password yet and include user info.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        print(cmd)
        os.system(cmd)

        # Show that its  are now setting the user's password.
        print("==> Setting the password for %s..." % (username))

        # Send the pssword to the passwd command to set it automatically.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        print(cmd)
        os.system(cmd)

        for group in groups:
            # If a group name is provided (not '-'), add the user to that group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
