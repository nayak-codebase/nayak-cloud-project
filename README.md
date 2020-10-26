nayak-cloud-project - The video file can be accessed at the following link https://drive.google.com/file/d/1owXqV1D3CpjggYc6yjzdcwKq_EkwW9im/view?usp=sharing


**Cloud Project 1 - awscloudservice.com**
==================================


The requirement is to build a 3 tier web application by making use of the cloud services and is accessible over the public internet through a registered domain
This project has made use of Amazon Web Services as cloud service.




***Project Details :***
--------------------------------
A 3 tier web application built on python and Django framework on below features:

> **Features :**

> - Upload objects to S3 buckets via UI
> - List and Browse the contents of S3 bucket in UI
> - Update the file object 
> - Delete the file object from S3 bucket
> - Leveraging aws cloudfront to download the file objects
> - Aws Rds service for storing the object metadata information

> **Workflow :**
> Authentication and Browsing files  :
> - User logs in to the web application http://awscloudservice.com:8000/admin/  with his credentials "user : admin" , "password :password@123", the user is authenticated and provided with the options to Browse, List and Update file objects.
> - List of file information such as user who uploaded the file, filename, upload url, timestamp, last updated time, file description and download url as shown below


> Upload the files  :
> - Authenticated users when click on the upload url, the user will be redirected to http://awscloudservice.com/upload/
> - Uploaded file will be moved to S3 bucket hosted on Aws


>Delete the files  :
> - Delete the already uploaded files and the file will get get deleted and user will not have the access to download the file.

>Download the files  :
> - User is provided with the download url, which is leveraging the cloud front service to provide fast download



> **Technologies:**

> - Python 3.5.2
> - Virtualenv setup for the project
> - Django 1.11.2
> - Apache server
> - Html, Css, Jquery and Ajax for the UI

Pre-requisite setup on Aws : 

 1. Amazon Ec2 : Created an ubuntu 16.04 Ec2 free tier instance to deploy the application
 2. Elastic Load balancers : Set the Ec2 instance behind Elastic load balancer for uniform distribution of traffic
 3. AutoScaling Group : To manage high traffic Ec2 instances have been added to the autoscaling group to automatically scale when there is high traffic 
 4. Lambda : Create a lambda function which is triggered when an object is created and logs are shared to cloudwatch.
 5. S3 : Used to store the objects uploaded by the user from the application's UI
 6. CloudFront : For quicker download's link is provided to user leveraging Cloudfront
 7. S3 Transfer Acceleration : S3 TA is enabled to speed up the uploading and downloading of files into the bucket
 8. S3 Lifecycle Policy : Setup a lifecycle policy for the objects to move from :S3 Standard to IA : 75 days,  IA to Glacier : 365 days Object expiry : 730 days
 9. Cross region replication : The S3 bucket is replicated across another region to provide a highly available service
 10. Multi AZ RDS : A aws postgresql Rds instance is created to store the objects metadata information
 11. Route53 : A domain ‘awscloudservice.com’ is registered in the route53, and a hosted zone is created for the domain
 12. CloudWatch : CloudWatch is enabled and an alarm is triggered when a file object is uploaded into S3.
 13. SNS : SNS is enabled to notify me when the file object is uploaded to S3 via email
 
 
> **Local configurations to setup and run the project:**

> - ssh to the ec2 instance using the .pem key
> - Install apache server : sudo apt-get install apache2
> - install python : sudo apt-get update && sudo apt-get install python3
> - Set up virtual environment : virtualenv -p python3 .
> - Activate the virtual environment : source bin/activate
> - Install pip install boto boto3 cryptography urllib3 requests
> - Install Django : pip install django==1.11.2
> - Download the src folder and cd src/
> - Run the Django server :  python manage.py runserver ec2_instance:8000
> - Go to browser : ec2_instace:8000/admin/
> - Enter the username : admin and password : password@123
