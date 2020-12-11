import os


def aws():
    print("""
        Press 1: To create Instance
        Press 2: To start instance
        Press 3: To stop Instance
        Press 4: To create Volume
        Press 5: To Attach Volume
        Press 6: To create IAM
        Press 7: To create S3 
        Press 8: To create configure
        Press 9: To Exit
        """)

    ch = int(input("Enter your choice"))
    print(ch)

    if ch == 1:
        iid = input("ENter your Instance ID: ")
        sgid = input("Enter Security Group id: ")
        keyName = input("Enter key Name: ")
        os.system(
            "aws ec2 run-instances --image-id " + iid + "  --instance-type t2.micro --count 1 --subnet-id subnet-2e717a46 --security-group-ids " + sgid + " --key-name " + keyName)
    elif ch == 2:
        iid = input("ENter your Instance ID: ")
        os.system("aws ec2 start-instances --instance-ids " + iid)
    elif ch == 3:
        iid = input("ENter your Instance ID: ")
        os.system("aws ec2 stop-instances --instance-ids " + iid)
    elif ch == 4:
        size = input("Enter size of volume in gb: ")
        az = input("Enter az (a,b,b)")
        os.system("aws ec2 create-volume  --volume-type gp2 --size " + size + " --availability-zone ap-south-1" + az)
    elif ch == 5:
        volId = input("Enter volume ID: ")
        InstanceId = input("Enter Instance ID: ")
        device = input("/dev/xvd[a-z] ")
        os.system("aws ec2 attach-volume --device /dev/xvd" + device + " --volume-id " + volId + " --instance-id " + InstanceId)
    elif ch == 6:
        UserName = input("Enter User-name")
        os.system("aws iam create-user --user-name  " + UserName)
    elif ch == 7:
        bucketName = input("Enter Bucket Name: ")
        os.system("aws s3 mb s3://" + bucketName + " --region ap-south-1")
    elif ch == 8:
        os.system("aws configure")
    elif ch == 9:
        exit()
    else:
        print("Not supported")

