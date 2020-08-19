# Code Institute - Final Project

Final Project for Code Institute - Issue Tracker

## Summary

It is hard to keep track of bug reports and new feature suggestions when you are working on few projects
at the same time and have to prioritize one task over another. The purpose of this project website is to make
it easy to keep track of both bugs and features of all your projects and also to prioritize these tasks
that your users/clients are the most interested into.


### Prerequisites

What things you need to install/create before running this software:

```
- Python 3.6 or newer
- PostgreSQL database
- Stripe account
- Environment variables
```

##### *Python 3.6 installation*

Open terminal/command line and type `python --version` or `python3 --version` if you can see e.g. `Python 3.6.10`
or newer version you can skip to the next step.

If you see errors you need to install Python 3.6 or newer version on your computer.
Go to the official [Python website](https://www.python.org/downloads/)
and follow the installation instructions for your system.

##### *PostgreSQL installation*

Open terminal/command line and type `postgres --version` if you can see e.g. `postgres (PostgreSQL) 10.13`
or newer version you can skip to the next step.

If you see errors you need to install newer version of PostgreSQL on your computer.
Go to the official [PostgreSQL website](https://www.postgresql.org/download/)
and follow the installation instructions for your system.

If you are not familiar with PostgreSQL read documentation how to: 
[create user](https://www.postgresql.org/docs/10/sql-createuser.html),
[create database](https://www.postgresql.org/docs/10/sql-createdatabase.html),
[run postresql server](https://www.postgresql.org/docs/10/server-start.html)
or just google how to do above things on your system.
Your PostgreSQL database and user parameters should be the same as in the `DATABASES` section
in the `/Code-Institute---Final-Project/issue_tracker/settings.py` file.

##### *Stripe account creation*

Create [Stripe account](https://dashboard.stripe.com/register)
to be able to do donations.

##### *Environmental variables creation*

You need to create 3 environmental variables on your system:
```
1) SECRET_KEY -> Django SECRET_KEY that is created automaticaly with each new Django project.
2) STRIPE_SECRET_KEY -> Go to your stripe account you created. Open Developers/API keys tab.
                        Copy the Secret key value.
3) STRIPE_PUBLISHABLE_KEY -> Go to your stripe account you created. Open Developers/API keys tab.
                             Copy the Publishable key value.
```
You can find out how to create environmental variables on your system in 
[this article](https://www.schrodinger.com/kb/1842).

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the repository:
```
git clone https://github.com/AnestIwata/Code-Institute---Final-Project
```

Create virtual env:

```
$ virtualenv env
```

Activate env:
(This will be different for non windows OS)
```
$ .\env\Scripts\activate.bat
```
Install dependencies:

```
$ pip install -r requirements.txt
```

Run Postgres database using psql:
(use password you provided during installation, everything else can be left to default)
```
$ psql
```

## Deployment

Deployed to Heroku. [Link](https://django-project-codeins.herokuapp.com/)

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Heroku](https://www.heroku.com/) - Deployment platform
* [Sentry](https://sentry.io/welcome/) - Used to capture errors

## Acknowledgments

Used free Bootstrap template 
- [Boostrap Business Frontpage](https://startbootstrap.com/templates/business-frontpage/)
- [Django Login/Registration tutorial](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/)
- [Django Docs](https://www.djangoproject.com/start/overview/)
- [Django Stripe Tutorial](https://testdriven.io/blog/django-stripe-tutorial/)