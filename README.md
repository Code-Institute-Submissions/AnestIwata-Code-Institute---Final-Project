# Code Institute - Final Project

Final Project for Code Institute - Issue Tracker

## Quick Description

This is a website that tracks both bugs and features for my project and lets users vote and create new tickets
for both bugs and features, it also allows them to donate in order to suggest new feature to be developed.


### Technologies Used

```
- Python3
- Django 2.2
- Postgres Heroku
- Sentry
- Travis CI
- Stripe
- Jinja2
- Bootstrap
```

### Prerequisites

What things you need to install before running this software:

```
- Django 2.2
- Python3
- Pip
- Postgres
```

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