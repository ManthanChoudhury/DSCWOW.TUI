import time
import os


def linux():
    print("""
                 Press 1 : To run date
                 Press 2 : To run calendar
                 Press 3 : To check free ram
                 Press 4 : To check ip address
                 Press 5 : To exit from Prog
                 """)
    ch = int(input("Enter what  u want to do : "))

    if ch == 1:
        os.system("date")
        input()
    elif ch == 2:
        os.system("cal")
        input()

    elif ch == 3:
        os.system("free -m")
        input()

    elif ch == 4:
        os.system("ifconfig enp0s3")
        input()

    elif ch == 5:
        exit()

    else:
        print("Not Supported")
        input()


def linux_remote(ip):
    print("""
                     Press 1 : To run date
                     Press 2 : To run calendar
                     Press 3 : To check free ram
                     Press 4 : To check ip address
                     Press 5 : To exit from Prog
                     """)
    ch = int(input("Enter what  u want to do : "))

    if ch == 1:
        os.system("ssh  {} date".format(ip))
        input()
    elif ch == 2:
        os.system("ssh {} cal".format(ip))
        input()

    elif ch == 3:
        os.system("ssh {} free -m".format(ip))
        input()

    elif ch == 4:
        os.system("ssh {} ifconfig enp0s3".format(ip))
        input()

    elif ch == 5:
        input()

    else:
        print("Not Supported")
        input()
