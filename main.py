import os
import linux
import docker
import aws



os.system("tput setaf 4")
print("--------------------------------------------------------------------")
os.system("tput setaf 3")
print("\t\t\tWelcome to World Automation")
os.system("tput setaf 4")
print("--------------------------------------------------------------------")

os.system("tput setaf 1")

operating_sys = input("Where u want to run prog ? (local/Remote) : ")
print(operating_sys)

while True:
    os.system("clear")
    os.system("tput setaf 2")
    print("""
    Press 1 : To deal  with linux 
    Press 2 : To deal with Docker 
    Press 3 : To deal with Hadoop
    Press 4 : To deal with AWS(Cloud)
    Press 5 : To exit from Prog
    """)

    choice = int(input("Enter your Choice : "))
    print(choice)

    if operating_sys == "local":
        if choice == 1:
            os.system("clear")
            linux.linux()

        elif choice == 2:
            os.system("clear")
            docker.docker()

        elif choice == 3:
            os.system("clear")

        elif choice == 4:
            os.system("clear")
            aws.aws()

        elif choice == 5:
            os.system("clear")
            exit()

        else:
            print("Not Supported")

    elif operating_sys == "remote":
        ip = input("Enter remote ip :")
        print(ip)
        if choice == 1:
            os.system("clear")
            linux.linux_remote(ip)

        elif choice == 2:
            os.system("clear")
            docker.docker_remote(ip)

        elif choice == 3:
            os.system("clear")

        elif choice == 4:
            os.system("clear")
            print("aws not for remote beacuse we are working remotly")

        elif choice == 5:
            os.system("clear")
            exit()

        else:
            print("Not Supported")