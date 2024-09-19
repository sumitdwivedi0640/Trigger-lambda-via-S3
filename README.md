 **S3 to Lambda Text Conversion Automation**
This repository demonstrates a serverless solution using AWS Lambda triggered by Amazon S3 to convert the content of text files from lowercase to uppercase. When a file is uploaded to a specified S3 folder, the Lambda function automatically processes the file, converts the text, and stores it in a different folder within the same S3 bucket.


**1. What is AWS Lambda?**
AWS Lambda is a serverless compute service that runs code in response to events and automatically manages the underlying compute resources. It’s a cost-effective way to execute code only when needed, without provisioning or managing servers.

**Why Use Lambda?**
--Serverless: Focus on your code, not infrastructure.
--Scalability: Automatically scales with workload size.
--Cost-Efficient: Pay only for the compute time your code consumes.
--Event-Driven: Ideal for event-based architectures like file uploads, database updates, and HTTP requests.


**2. Project Overview**
This project utilizes AWS Lambda and S3 to:
-Trigger a Lambda function upon file upload to an S3 folder.
-Convert the file’s content from lowercase to uppercase.
-Store the converted file in a different folder within the same S3 bucket.

**Flow of Execution:**
-A text file is uploaded to the lowercase-folder/ of the S3 bucket.
-The Lambda function reads the file, processes it, and converts the text to uppercase.
-The converted file is saved to the uppercase-folder/ in the same S3 bucket.


**3. Architecture Flowchart**
   This flowchart shows how the S3 upload triggers AWS Lambda to convert text files:

       flowchart.png


**4. Implementation Steps**  
**4.1 AWS Resources Utilized:**
-Amazon S3: Used for storing files.
-AWS Lambda: Processes the files and converts the text.
-IAM Role: Grants Lambda permissions to access S3.

**4.2 Lambda Function Code:**
-The Lambda function is written in Python and is triggered by S3 events (i.e., file uploads). 
-It reads the uploaded file, converts the content to uppercase, and stores the new file in a different folder.


**5. How to Set Up This Project**
Step 1: Create an S3 Bucket
-In your AWS Console, create an S3 bucket (e.g., text-conversion-bucket).
-Create two folders inside this bucket:
-lowercase-folder/ (for input files)
-uppercase-folder/ (for converted files)

Step 2: Create the Lambda Function
-In the AWS Console, go to Lambda and create a new function.
-Choose Python as the runtime and paste the provided Python code.
-Set up an S3 trigger for the lowercase-folder/ so that the function runs when a file is uploaded.

Step 3: Assign IAM Permissions
-Ensure that your Lambda function has an execution role with the necessary permissions to access your S3 bucket.
-Attach the AmazonS3FullAccess policy to the Lambda role.


**6. How to Use This Project**
-Upload a Text File:
-Upload a text file with lowercase text to the lowercase-folder/ in the S3 bucket.
-Lambda Trigger:
-The Lambda function is triggered upon file upload and processes the file.
-Check the Uppercase Folder:
-The converted file will appear in the uppercase-folder/ with all content in uppercase.


**7. Conclusion**
This project demonstrates how to leverage AWS Lambda and S3 for serverless automation, enabling real-time file processing. The solution is scalable, cost-efficient, and requires minimal maintenance, making it ideal for event-driven architectures.


Notes:
Ensure that the bucket and folder names used in your S3 setup match the ones defined in the Lambda function.
The architecture can be expanded for more complex file processing scenarios.
