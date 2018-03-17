#! /usr/bin/python3
import getpass
usrlist = ['Tyler', 'Krysta'] #List of Usernames
Passwdlist = ['Carroll513', 'Krysta'] #List of Passwords

Usrname = str(input('Enter Username here: '))
Passwd = getpass.getpass('Enter your Password: ')

def UsrCheck():
	print('Hello and Welcome to Business.net Server!')
	print('')
	
	if (Usrname, Passwd) == (usrlist[0], Passwdlist[0]): #Checks for username 'Tyler' and Password 'Carroll513'
		print('Hello Tyler')
		main()
	elif (Usrname, Passwd) == (usrlist[1], Passwdlist[1]): #Checks for username 'Krysta' and Password 'Krysta'
		print('Hello Krysta')

def main():
	if Usrname == usrlist[0]:


UsrCheck()