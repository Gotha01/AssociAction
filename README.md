# Associ'Action

## Badges
![Static Badge](https://img.shields.io/badge/Status-pre_deployment-blue)
![Static Badge](https://img.shields.io/badge/Version-1.0.0-blue)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

---
## Description

### Associ'Action opens the doors to a virtual agora, a dynamic marketplace for associations, enabling you to discover, join and benefit from the services offered by a multitude of organizations. Interact, share experiences and actively contribute to the associative life of your community.

## Summary


[**Overall operation**](#Overall-operation)  

[**For Local Use**](#For-Local-Use)  

[**About me**](#About-me)  

[**Links**](#Links)

[**Tools**](#Tools)  


## Overall operation
<a name="Overall-operation"></a>
Users can search for associations by name or city, and then access their details page to view information and events.

Users can also register on the site so that their information can be recorded and used to search for associations by region or sector.

What's more, registering will give you your own association directory, so you can access events more quickly.

If the user is a member of the association, there are three recognized categories: member, administrator, director; each of these roles has rights over the previous one.

Of course, to upgrade a member to the role of association director, a request must be made to the application administrator by email.


<a name="For-Local-Use"></a>

## 🏠 For Local Use

To use this project locally, follow these steps:

### 1. Project download

Download the project by clicking on the "Code" button at the top right of this page, then select "Download ZIP".  
Then unzip the downloaded ZIP file.

### 2. Python Version Check

Make sure you have Python installed on your machine. You can check your Python version using the following command:  

```bash
python --version
```

Make sure you have at least Python 3.8 or later.

### 3. Initializing the Virtual Environment

Before you begin, create a virtual environment using the following command:
```python
python -m venv venv
```

#### **Activate the virtual environment :**

On Windows :
```bash
venv\Scripts\activate
```

On macOS and Linux :
```bash
source venv/bin/activate
```

### 4. Dependencies installation
Install the required dependencies using the following command to read the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 5. Database creation
To create a MySQL database for your Django project named "dbassociation", follow these steps:

Install MySQL :  
If you haven't already done so, make sure you install MySQL on your system. You can download the appropriate version for your operating system from the official MySQL website (https://dev.mysql.com/downloads/). 

Create a Database :  
Once MySQL has been installed, you can create a new database using the command line interface.  
Open a terminal and connect to MySQL using an account with administrative privileges. You will be prompted to enter the account password.
```ps
mysql -u root -p
```

Once connected, you can create a new database using the following SQL command. Replace "dbassociation" with the name of your desired database.

```sql
CREATE DATABASE dbassociation;
```

You can check that the database has been created using the following command:

```sql
SHOW DATABASES;
```

**Configuring Database Information in Django:**  
In your Django project, open the settings.py file and locate the DATABASES section. You need to configure the database connection information as follows:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbassociation',
        'USER': 'votre_utilisateur_mysql',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',  # or the address of your MySQL server
        'PORT': '',  # Leave empty to use default port (3306)
    }
}
```
Be sure to replace **_'your_mysql_user'_** with **_'your_mysql_password'_**
with the appropriate login information for your MySQL server.

### 6.Database migrations
Make sure you have activated the virtual environment (previous step). Next, run the database migrations using the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7.Creating a Superuser
To access the Django administration interface, you need to create a superuser using the following command:
```bash
python manage.py createsuperuser
```
Follow the instructions to create the superuser, providing an e-mail address, user name, surname, first name and password.


### 8.Launching the Development Server
Start the Django development server with the following command:

```bash
python manage.py runserver
```
The server should start up, and you can access the application by opening a web browser and accessing http://localhost:8000/.
<a name="About Me"></a>

## 🚀 About Me

I'm a junior Python developer who try to code his life with a better framework than the one he used yesterday.

<a name="Links"></a>

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/quentin-faure-b818221b9/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Q_Faure/)

<a name="Tools"></a>

## Tools
<p align="top left">
  <img src="https://www.djangoproject.com/m/img/logos/django-logo-negative.svg" alt="Django" width="200" height="100">
</p>
<p align="top right">
  <img src="https://github.com/tus/official-images-docs/blob/master/mysql/logo.png?raw=true" alt="Django" width="200" height="90">
</p>