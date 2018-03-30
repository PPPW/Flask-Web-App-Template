# Flask Web App Template

## Overview
Flask is a light-weight backend framework. Unlike Django, Flask haven't defined a standard app structure. This empty Flask web app template follows the structures recommended in the official documentation:   
[Patterns for Flask](http://flask.pocoo.org/docs/0.12/patterns/)

The app structure is: 

```
.
+-- myapp/
|   +-- static/
|   |   +-- style.css
|   +-- templates/
|   |   +-- general/
|   |   |   +-- index.html
|   |   +-- 404.html
|   |   +-- layout.html
|   +-- views/
|   |   +-- __init__.py
|   |   +-- general.py
|   +-- __init__.py
|   +-- config.py
+-- migrations/
+-- tests/
+-- manage.py
+-- setup.py
```

To run this app, install dependencies (actually, only need to install Flask):

```
pip install -r requirements.txt
```

Then:

```
python manage.py runserver
```

Then visit "http://127.0.0.1:5000/" to see the website: 

![](/images/hello.png)

To run unit tests:

```
python manage.py test
```

## The Structure

* manage.py:

Use command line commands. By default, we have this command to run the app:
```
python manage.py runserver
```

You can apply the "@manager.command" decorator to your own functions to add commands. In this example, I have defined the "create_db" command to create database, and the "test" to run unit test. 

* "myapp" folder:    

config.py: set configurations for the app. For example, you may want to use a different configuration for testing. Two configurations, "development" and "testing" are defined in this file, you can add more customized configurations.

\_\_init\_\_.py: create and initialize the app. Blueprints are also registered in here. 

* "myapp/static" folder:   

This folder contains static files, such as "css", "js", etc. If you use a front-end framework, such as React, Angular, Vue, etc., you can place the app files in this folder. 

* "myapp/templates" folder:   
This folder contains the view templates. 

   * layout.html: the master layout for the whole website. All other views will be inserted to the "body" block. 

   * 404.html: the 404 error page. 

* "myapp/views" folder:   

This folder contains the view controllers. In here, each view controller has a Blueprint, which can be used for routing in the same way as the Flask application class. You can define multiple view controllers, just register the Blueprint in the "create_app" function, and put the corresponding templates under "templates/your_view_controller/". By using Blueprint, you can break down the app into smaller components. 

general.py: an example of a view controller. 

* "migrations" folder:

This is the default folder for migrations. 

* "tests" folder:

This folder contains test files. The test runner will look for all files in this folder. 
