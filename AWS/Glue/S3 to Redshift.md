### Create a S3 bucket and redshift preparation 

#### 1. create a role: 
S3readonlyaccess / DMSRedshiftS3Role / RedshiftDataFullAccess

#### 2. create redshift cluster (using the role created before)
#### 3. create S3 bucket for data storage 


### Create table in Redshift using SQL
##### Example: 
    create table venue(
        venueid smallint not null distkey sortkey,
        venuename varchar(100),
        venuecity varchar(30),
        venuestate char(2),
        venueseats integer);
        
#### Fullfill data from S3 bucket into tables
* credentials == role's ARN 

        copy venue from 's3://awssampledbuswest2/tickit/venue_pipe.txt' 
        credentials 'aws_iam_role=<iam-role-arn>' 
        delimiter '|' region 'us-west-2';

#### save query in Redshift in case you will use next time 
