# flask_e2e_project

# MedBooking

## Web service explanation
The web service I created is a Healthcare Information System. Originally, I wanted to create this app for the patients to be able to book appointments and review labs results and prescriptions, but after many difficulties, this app is good for healthcare providers to look for patients, appointments, labs and prescriptions. 
For this project, I created a virtual machine in Azure.
MySql workbench to create the database, and tables.
Used flask to deploy the app locally.
Sqlalchemy to populate the tables. 
Faker to create the fake data.
Google Shell to create the codes.

## Steps to run it.
1. Locally: first go to the directory Flask_e2e_project, and then to the folder App. run the command app.py and the app with open.
2. Deploy to the cloud in Azure: Instructiosn bellow
3. To run it with Ducker locally: Create the image, then run the command run -p 5000:5000 and the name of the image. Make sure to change the port to be able to run the app. 

# Instructions I followed to run it into the cloud with Azure. 
First, make sure the directory were the app is located is open and ready for all these commands. 
1. curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash : to begin the installation.
2. az : to make sure it was install. 
3. az login --use-device-code : to get the code to start the login process. 
4. az group list : to verify the name of the group I was going to be using for this process.(My resource group was connected to my Azure student account already. 
5. az webapp up --resource-group <mygroupname> --name <myappname> --runtime <PYTHON:3.10> --sky B1: to create the app services.
6. az webapp up : to push the changes.

Unfortunately, the app did not deploy. everything workded perfect, I received the completed messages but it did not deploy. (Pictures are added to prove it)

