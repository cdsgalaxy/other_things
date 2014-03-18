#!/usr/bin/python

import os
import sys
import string 

username = raw_input('What is the user id that needs group modification? ')
group = raw_input('Which additional group will this user belong to? ')

file2 = open('/etc/openldap/tmp/usergroup.ldif', mode='w')
f = file2.write('dn: cn=' + group + ',ou=group,dc=xxxx,dc=xxxx' + '\n')
f = file2.write('changetype: modify' + '\n')
f = file2.write('add: memberuid' + '\n')
f = file2.write('memberuid: ' + username + '\n')
file2.close()
## We also have to add the user group they belong to

os.system('ldapmodify -x -D "cn=root,dc=xxxx,dc=xxxx" -w xxxx -f /etc/openldap/tmp/usergroup.ldif') 

