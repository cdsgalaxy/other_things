#!/usr/bin/python

import os
import sys
import string 

username = raw_input('What is the user id that needs group modification? ')
group = raw_input('What group will this user need to be removed from? ')

file2 = open('/etc/openldap/tmp/usergroup.ldif', mode='w')
f = file2.write('dn: cn=' + group + ',ou=group,dc=xxx,dc=xxx' + '\n')
f = file2.write('changetype: modify' + '\n')
f = file2.write('delete: memberuid' + '\n')
f = file2.write('memberuid: ' + username + '\n')
file2.close()
## We also have to add the user group they belong to

os.system('ldapmodify -x -D "cn=xxx,dc=xxx,dc=xxx" -w xxx -f /etc/openldap/tmp/usergroup.ldif') 

