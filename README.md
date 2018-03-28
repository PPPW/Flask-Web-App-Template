# Flask Web App Template

## Overview
Flask is a light-weight backend web framework. Unlike Django, Flask is very flexible, it doesn't have a standard folder structure. This empty Flask web app follows the folder structures recommended in the official documentation:   
[Patterns for Flask](http://flask.pocoo.org/docs/0.12/patterns/)

The folder structure is: 

```
.
+-- myapp
|   +-- static
|   |   +-- style.css
|   +-- templates
|   |   +-- general
|   |   |   +-- index.html
|   |   +-- 404.html
|   |   +-- layout.html
|   +-- views
|   |   +-- __init__.py
|   |   +-- general.py
|   +-- __init__.py
|   +-- config.py
+-- run.py
+-- setup.py
```

To run this app, install dependencies (actually, only need to install Flask):

```
pip install -r requirements.txt
```

Then:

```
python run.py
```

Then visit "http://127.0.0.1:5000/" to see the website: 

![](/images/hello.png)

## The Structure

* "myapp" folder:    

config.py: set configurations for the app. For example, you may want to use a different configuration for testing. Two configurations, "development" and "testing" are defined in this file, you can add more customized configurations.

\_\_init\_\_.py: create and initialize the app. Blueprints are also registered in here. 

* "static" folder:   

This folder contains static files, such as "css", "js", etc. If you use a front-end framework, such as React, Angular, Vue, etc., you can place the app files in this folder. 

* "templates" folder:   
This folder contains the view templates. 

   * layout.html: the master layout for the whole website. All other views will be inserted to the "body" block. 

   * 404.html: the 404 error page. 

* "views" folder:   

This folder contains the view controllers. In here, each view controller has a Blueprint, which can be used for routing in the same way as the Flask application class. You can define multiple view controllers, just register the Blueprint in the "create_app" function, and put the corresponding templates under "templates/your_view_controller/". By using Blueprint, you can break down the app into smaller components. 

general.py: an example of a view controller. 

