#!/usr/bin/python 

import os
import random
import string
import sys
import itertools
import hashlib
import crypt

import os, random, string

## need this lines later on, don't forget to move it to the end 

length = 10
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

newpass = ''.join(random.choice(chars) for i in range(length))
hash = crypt.crypt(newpass)
#print newpass
#print hash

## this ends the silliness of making a password.

## Now let's start making an ldif file for our new user

username = raw_input('What is your user id to be? ')
file = open("/etc/openldap/tmp/" + username + ".ldif", mode="w")
shell = raw_input('What shell do you like using? ')
uid = raw_input('What is the User ID number? ')
gid = raw_input('What is the default group id? (should be the same as UID, in most cases)? ')
group = raw_input('Which group will this user belong to? ')
print ('\n')
#print username
#print shell
#print uid
#print gid
#print group

f = file.write('dn: cn=' + username + ',ou=xxx,dc=xxx,dc=xxx\n')
f = file.write('uid: ' + username + '\n')
f = file.write('cn: ' + username + '\n')
f = file.write('objectClass: account\n')
f = file.write('objectClass: posixAccount\n')
f = file.write('objectClass: top\n')
f = file.write('objectClass: shadowAccount\n')
f = file.write('userPassword: {crypt}' + hash + '\n')
f = file.write('shadowLastChange: 15807\n')
f = file.write('shadowMax: 99999\n')
f = file.write('shadowWarning: 7\n')
f = file.write('loginShell: /bin/' + shell + '\n')
f = file.write('uidNumber: ' + uid + '\n')
f = file.write('gidNumber: ' + gid + '\n')
f = file.write('homeDirectory: /home/' + username + '\n')
file.close()
file2 = open('/etc/openldap/tmp/usergroup.ldif', mode='w')
f = file2.write('dn: cn=' + group + ',ou=xxx,dc=xxx,dc=xxx' + '\n')
f = file2.write('changetype: modify' + '\n')
f = file2.write('add: memberuid' + '\n')
f = file2.write('memberuid: ' + username + '\n')
file2.close()

## now that we have written the base file, we can start adding things into the database.

os.system('ldapadd -x -D "cn=xxx,dc=xxx,dc=xxx" -w xxx -f /etc/openldap/tmp/' + username + '.ldif')

## We also have to add the user group they belong to

os.system('ldapmodify -x -D "cn=xxxx,dc=xxxx,dc=xxxx" -w xxxx -f /etc/openldap/tmp/usergroup.ldif') 

## let's remind the user of their new password

print ('Here is the password for the new user: '  + newpass + '\n')
