# TRAVEL BLOG - DUSTY TRAVELER 
 README AND INSTALLATION INSTRUCTIONS

# Author: ZMOMEN
 95-882 Enterprise Web Development - Spring 2018. Carnegie Mellon University 

# Screenshots

![screen1](https://github.com/zmomen/travel_blog/tree/master/demo/screen1.png)

# SOURCES AND REFERENCES: 
 
 Django Tutorials
 https://www.youtube.com/watch?v=Fc2O3_2kax8&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj
 
 WYSIWYG - summernote
 https://github.com/summernote/django-summernote
 
 BOOTSRAP CSS and JS
 https://getbootstrap.com/
 
 FAVORITES
 https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html
 
 TAGGING
 https://github.com/alex/django-taggit


# Intro: 

This web project is developed using the python Django Framework. Before installing django, please follow the instructions below for installing Python3, pip3, and virtualenv. Please make sure to install those components in that order, before installing Django.


Note: virtualenv is a python virtual environment package that is very handy. It allows pip to install any packages necessary without worrying about system permissions or user access. Basically, once python3 and pip3 are intalled, the virtual environment can then be activated and used to run this project going forward. This is an important step as it saves a lot of time and effort for installing any future packages.   


# Installing python3 and pip3: 

Please get the latest python3 version from https://www.python.org/downloads/ and install it on your machine. 
Then depending on your OS, follow guidelines for installing pip3. 
Usually in terminal on a unix-based machine (Mac, Linux) use: sudo apt install python3-pip

Once pip3 (or just pip) is installed, proceed to the next section for installing the packages necessary to run this project. 

Installing and Activating virtualenv: 
	
virtualenv is a python package that allows the user to work in an isolated python environment where they can install and run extra python packages without worrying about system permissions. To install virtualenv, do the following: 

1. make sure python and pip are installed. (to check, run python -V. Also run pip -V to see the versions)
2. run: pip install virtualenv
3. once virtualenv is installed, create a new virtual environment by running: "virtualenv venv" or any name you like. You virtual environment will have a folder called venv.
4. Activating the environment: change to the directory where 'venv' was created and run: source venv/bin/activate
You should see (venv) in your terminal window like this: 

$ source venv/bin/activate
(venv) $ 

This means that you are now working in the python virtual environment. Proceed to the next section to install packages in this venv environment. 

Note: Everytime you stop the django server, restart the machine, turn off the computer, when you come back, you will need to activate the venv environment again by running the command source venv/bin/activate. Remember to always work from within the virtual environment. This project will install django and all the other packages inside the virtual environment.


# Installing Django. 

For django, pip has a quick way for intalling it. First make sure you are in the virtual environment and your command prompt should look like 
source venv/bin/activate
(venv) zaids-air:~ zaidal-momen$ 

Then, run: pip install django. 
Once django is installed successfully, proceed to the next section to intall the necessary packages for DUSTY TRAVELER. 

# Installing python packages for DUSTY TRAVELER. 

 The package named are all stored in a file called 'requirements.txt' for ease of install. pip provides an easy way to go through all the packages in that file and install them automatically. The requirements.txt file is included as part of the project deliverable, in the travel_blog.zip file. 

The requirements.txt contains: 
Django==2.0.4
django-summernote==0.8.8.6
django-taggit==0.22.2
Pillow==5.1.0
pytz==2018.4 

There are three important packages in addition to Django: 
- summernote which is a WYSIWYG editor for blog entry. CREDIT: https://github.com/summernote/django-summernote
- taggit a helper packages for creating and organizing tags. CREDIT: https://github.com/alex/django-taggit
-  Pillow for image upload. 

- Follow these steps:
1. cd to the directory where requirements.txt is located
2. activate your virtualenv 
	source venv/bin/activate
	(venv) zaids-air:~ zaidal-momen$ 
3. run:  pip install -r requirements.txt in your shell

You should now have all the packages necessary and you are now ready to deploy and run the DUSTY TRAVELER web project. double check they are installed by running 'pip freeze'

# RUNNING DUSTY TRAVELER: 

The DUSTY TRAVELER web project is a django project under the name 'travel_blog'. It is the main folder in the zip file. After following this README.txt and installing django and all other components, you are ready to deploy the travel_blog project. 

the travel_blog project can live anywhere in your system. In order to run the project, do the following: 
cd travel_blog/
python manage.py runserver 

This will kick off the django server and deploy your project locally on port 8000. The URL to access the website is:
http://localhost:8000/ which will automatically redirect to the login page: http://localhost:8000/account/login




