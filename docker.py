import os


def docker():
    chh = 0
    while chh != 12:
        print("""
                                 Press 1 : To start docker
                                 Press 2 : To stop docker
                                 Press 3 : To check docker info
                                 Press 4 : To check docker help
                                 Press 5 : To download image 
                                 Press 6 : To check list of all images
                                 Press 7 : To run docker os  
                                 Press 8 : To run docker os in background
                                 Press 9 : To run docker os for single command
                                 Press 10 : To check current running os
                                 Press 11 : To check all running os 
                                 Press 12 : To go back
                                 """)
        ch = int(input("Enter what  u want to do : "))

        if ch == 1:
            os.system("systemctl start docker")
            input()

        elif ch == 2:
            os.system("systemctl stop docker")
            input()

        elif ch == 3:
            os.system("docker info")
            input()

        elif ch == 4:
            os.system("docker --help")
            input()
        elif ch == 5:
            print("""
                        image example 
                        1. Centos 
                        2. Fedora
                        3. Ubuntu
                        ...etc..
                             """)
            image = input("Enter the name of image ")
            os.system("docker pull {}".format(image))

        elif ch == 6:
            os.system("docker images")
            input()
        elif ch == 7:
            name = input("Enter the name of os")
            img = input("Enter the name of img")
            os.system("docker run -it --name {} {}".format(name, img))
        elif ch == 8:
            name = input("Enter the name of os")
            img = input("Enter the name of image")
            os.system("docker run -dit --name {} {}".format(name, img))
        elif ch == 9:
            name = input("Enter the name of os")
            img = input("Enter the name of image")
            cmd = input("Enter the command u want to run ")
            os.system("docker run -it --name {} {} {}".format(name, img, cmd))
            input()
        elif ch == 10:
            os.system("docker ps")
            input()
        elif ch == 11:
            os.system("docker ps -a")
            input()
        elif ch == 11:
            exit()
        else:
            print("Not supported ")


def docker_remote(ip):
    print("""
                             Press 1 : To start docker
                             Press 2 : To stop docker
                             Press 3 : To check docker info
                             Press 4 : To check docker help
                             Press 5 : To download image 
                             Press 6 : To check list of all images
                             Press 7 : To run docker os  
                             Press 8 : To run docker os in background
                             Press 9 : To run docker os for single command
                             Press 10 : To check current running os
                             Press 11 : To check all running os 
                             Press 12 : To exit 
                             """)
    ch = input("Enter what  u want to do : ")

    if int(ch) == 1:
        os.system("ssh {} systemctl start docker".format(ip))
        input()

    elif int(ch) == 2:
        os.system("ssh {} systemctl stop docker".format(ip))
        input()

    elif int(ch) == 3:
        os.system("ssh {} docker info".format(ip))
        input()

    elif int(ch) == 4:
        os.system("ssh {} docker --help".format(ip))
        input()
    elif int(ch) == 5:
        print("""
                    image example 
                    1. Centos 
                    2. Fedora
                    3. Ubuntu
                    ...etc..
                         """)
        image = input("Enter the name of image ")
        os.system("ssh {} docker pull {}".format(ip, image))

    elif int(ch) == 6:
        os.system("ssh {} docker images".format(ip))
        input()
    elif int(ch) == 7:
        name = input("Enter the name of os")
        img = input("Enter the name of os")
        os.system("ssh {} docker run -it --name {} {}".format(ip, name, img))
    elif int(ch) == 8:
        name = input("Enter the name of os")
        img = input("Enter the name of image")
        os.system("ssh {} docker run -dit --name {} {}".format(ip, name, img))
    elif int(ch) == 9:
        name = input("Enter the name of os")
        img = input("Enter the name of image")
        cmd = input("Enter the command u want to run ")
        os.system("ssh {} docker run -it --name {} {} {}".format(ip, name, img, cmd))
        input()
    elif int(ch) == 10:
        os.system("ssh {} docker ps".format(ip))
        input()
    elif int(ch) == 11:
        os.system("ssh {} docker ps -a".format(ip))
        input()
    elif int(ch) == 12:
        exit()
    else:
        print("Not supported ")


