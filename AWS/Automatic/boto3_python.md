### BOTO3 concepts
* Session 
* Resource
* Client 
* Meta
* Collections
* Waiters
* Paginators


### Creat AWS credential 
* root account: awsAccesskey / AWSSecretKey
* create user for ec2 and S3 access key & SecretKey: 
    * user1_ec2—— create "ec2_developer"  for ec2fullaccess (policy)
    * user2_s3 —— create "s3_developer" for s3fullaccess 

```python3

pip3 install boto3
pip3 install awscli

```

* configure aws on windoew:
```
# aws root KEY
aws configure -- profile root  
# AWS EC2 KEY
aws configure -- profile ec2_developer 
# AWS S3 KEY
aws configure -- profile s3_developer

# find the configure files
cd %HOMEPATH%
cd .aws   # will find the configure files 

```

* list aws IAM users name using python

```python

import boto3

aws_mag_con=boto3.session.Session(profile_name="root")  #profile name == 上面的profile name

# resource 
iam_con=aws_mag_con.resource('iam')  # service_name: The name of a service, e.g. 's3' or 'ec2'. You
                                    # can get a list of available services


for each_user in iam_con.users.all():
    print(each_user.name)             ## output： ec2_developer & s3_developer

# S3 resource & list all the buckets in S3
aws_mag_con = boto3.session.Session(profile_name="root")
s3_con = aws_mag_con.resource('s3')

for each_buk in s3_con.buckets.all():
    print(each_buk)

```

* EC2 action (start/stop/terminate/exit) using ec2 client in boto3
```python
import boto3
import sys
aws_mag_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

while True:
	print("This script performs the following actions on ec2 instance")
	print("""
		1. start
		2. stop
		3. terminate
		4. Exit""")
	opt=int(input("Enter your option: "))
	if opt==1:
            instance_id=input('Enter your EC2 Instance Id: ')
            #print(dir(my_req_instance_object))
            print("Starting ec2 instance.....")
            ec2_con_cli.start_instances(InstanceIds=[instance_id])
	elif opt==2:
            instance_id=input('Enter your EC2 Instance Id: ')
            print("Stopping ec2 instance.....")
            ec2_con_cli.stop_instances(InstanceIds=[instance_id])
	elif opt==3:
            instance_id=input('Enter your EC2 Instance Id: ')
            print("Terminating ec2 instance.....")
            ec2_con_cli.terminate_instances(InstanceIds=[instance_id])
	elif opt==4:
            print("Thank you for using this script")
            sys.exit()
	else:
	    print("Your option is invalid. Please try once again")

```

* check instance state: running  (if the instance start running successful)
    * use get_waiter("instance_running")
    
```python

import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

np_sers_ids=[]
f1 = {"Name": "tag:Name", "Values":['Non_Prod']}
for each_item in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
	for each_in in each_item['Instances']:
		np_sers_ids.append(each_in['InstanceId'])
print(np_sers_ids)

print("Starting intances with ids of : ",np_sers_ids)
ec2_con_cli.start_instances(InstanceIds=np_sers_ids)
waiter=ec2_con_cli.get_waiter('instance_running')  # while the state : running 就是如果成功run了后就会跳到下一步
waiter.wait(InstanceIds=np_sers_ids)
print("Your np instances are up and running....")

```

* Lambda Function 
