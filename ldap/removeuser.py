#!/usr/bin/python

import os
import sys
import string

#lets work with the user/username first

file = open('/etc/openldap/tmp/remove.ldif', 'w')
username = raw_input('What is the user name that is to be removed? ')
group = raw_input('What group does this user belong to (admins, d-duplicate, savanna)? ')
f = file.write('cn=' + username + ',ou=People,dc=xxxx,dc=xxxx' + '\n')
file.close()
os.system('ldapdelete -x -D "cn=xxxx,dc=xxxx,dc=xxxx" -w xxxx -f /etc/openldap/tmp/remove.ldif')

# now we need to remove them from their group membership

file2 = open('/etc/openldap/tmp/usergroup.ldif', 'w')
f = file2.write('dn: cn=' + group + ',ou=group,dc=xxxx,dc=xxxx' + '\n')
f = file2.write('changetype: modify' + '\n')
f = file2.write('delete: memberuid' + '\n')
f = file2.write('memberuid: ' + username + '\n')
file2.close()
os.system('ldapmodify -x -D "cn=root,dc=xxxx,dc=xxxx" -w xxxx -f /etc/openldap/tmp/usergroup.ldif')

# Now that is the done deed, let's let everyknow what we just nuked

print ('This is what we changed: we removed ' + username + ' from ldap and removed their group membership to: ' + group + '. Have a fine day.')
